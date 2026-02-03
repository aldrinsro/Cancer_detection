import streamlit as st 
import pickle
import pandas as pd 
import plotly.graph_objects as go 
import numpy as np 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CSS_FILE = BASE_DIR.parent / "assets" / "style.css"
DATA= BASE_DIR.parent / "data" / "data.csv"
MODEL = BASE_DIR.parent / "model" / "model.pkl"
SCALER = BASE_DIR.parent / "model" / "scaler.pkl"


def get_clean_data():
    data = pd.read_csv(DATA)
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    data['diagnosis'] = data['diagnosis'].map({ 'M': 1, 'B': 0 })
    
    return data

def get_scaled_values(inpuct_dict):
    data = get_clean_data()

    X = data.drop(['diagnosis'], axis=1)

    scaled_dict = {}
    for key ,value in inpuct_dict.items():
        max_val=X[key].max()
        min_val=X[key].min()
        scaled_dict[key] = (value - min_val) / (max_val - min_val) if max_val > min_val else 0

    return scaled_dict

def add_sidebar() :
    st.sidebar.title("Paramètres des caractéristiques")
    data = get_clean_data()

    slider_labels = [
        ("Rayon (moyenne)", "radius_mean"),
        ("Texture (moyenne)", "texture_mean"),
        ("Périmètre (moyenne)", "perimeter_mean"),
        ("Aire (moyenne)", "area_mean"),
        ("Lissage (moyenne)", "smoothness_mean"),
        ("Compacité (moyenne)", "compactness_mean"),
        ("Concavité (moyenne)", "concavity_mean"),
        ("Points concaves (moyenne)", "concave points_mean"),
        ("Symétrie (moyenne)", "symmetry_mean"),
        ("Dimension fractale (moyenne)", "fractal_dimension_mean"),
        ("Rayon (écart-type)", "radius_se"),
        ("Texture (écart-type)", "texture_se"),
        ("Périmètre (écart-type)", "perimeter_se"),
        ("Aire (écart-type)", "area_se"),
        ("Lissage (écart-type)", "smoothness_se"),
        ("Compacité (écart-type)", "compactness_se"),
        ("Concavité (écart-type)", "concavity_se"),
        ("Points concaves (écart-type)", "concave points_se"),
        ("Symétrie (écart-type)", "symmetry_se"),
        ("Dimension fractale (écart-type)", "fractal_dimension_se"),
        ("Rayon (pire)", "radius_worst"),
        ("Texture (pire)", "texture_worst"),
        ("Périmètre (pire)", "perimeter_worst"),
        ("Aire (pire)", "area_worst"),
        ("Lissage (pire)", "smoothness_worst"),
        ("Compacité (pire)", "compactness_worst"),
        ("Concavité (pire)", "concavity_worst"),
        ("Points concaves (pire)", "concave points_worst"),
        ("Symétrie (pire)", "symmetry_worst"),
        ("Dimension fractale (pire)", "fractal_dimension_worst"),
    ]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
        label,
        min_value=float(0),
        max_value=float(data[key].max()),
        value=float(data[key].mean())
        )
    
    return input_dict

def get_radar_chart(input_data) :
    input_data = get_scaled_values(input_data)

    categories = [
        "rayon", "texture", "périmètre", "aire", "lissage",
        "compacité", "concavité", "points concaves", "symétrie",
        "dimension fractale"
    ]
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data["radius_mean"],
            input_data["texture_mean"],
            input_data["perimeter_mean"],
            input_data["area_mean"],
            input_data["smoothness_mean"],
            input_data["compactness_mean"],
            input_data["concavity_mean"],
            input_data["concave points_mean"],
            input_data["symmetry_mean"],
            input_data["fractal_dimension_mean"]
        ],
        theta=categories,
        fill="toself",
        name="Valeur de la moyenne"
    ))  

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data["radius_se"],
            input_data["texture_se"],
            input_data["perimeter_se"],
            input_data["area_se"],
            input_data["smoothness_se"],
            input_data["compactness_se"],
            input_data["concavity_se"],
            input_data["concave points_se"],
            input_data["symmetry_se"],
            input_data["fractal_dimension_se"]
        ],
        theta=categories,
        fill="toself",
        name=" Valeur d'écart-type"
    ))
    fig.add_trace(go.Scatterpolar(
        r= [
            input_data['radius_worst'],
            input_data['texture_worst'],
            input_data['perimeter_worst'],
            input_data['area_worst'],
            input_data['smoothness_worst'],
            input_data['compactness_worst'],
            input_data['concavity_worst'],
            input_data['concave points_worst'],
            input_data['symmetry_worst'],
            input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill="toself",
        name="Valeur la plus mauvaise"
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,1]
            )
        ),
        showlegend=True
    )

    return fig 


def add_prediction(input_data) :
    model = pickle.load(open(MODEL,'rb'))
    scaler = pickle.load(open(SCALER,'rb'))
    input_array = np.array([list(input_data.values())])

    input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)

    st.subheader("Prédiction du cluster cellulaire")
    st.write("Le cluster cellulaire est prédit comme étant :")

    if prediction[0]==0:
        st.write("<span class='diagnosis begin'>Tumeur béigne détectée .</span>",unsafe_allow_html=True)
    else : 
        st.write("<span class='diagnosis Malicious'>Tumeur maligne détectée.</span>",unsafe_allow_html=True)

    st.write("la probabilité qu'elle soit bénigne :", model.predict_proba(input_array)[0][0])
    st.write("la probabilité qu'elle soit maligne :", model.predict_proba(input_array)[0][1])

    st.write(" Cette application peut assiter des professionnels medical pour diagnostiquer" \
    ",mais ne doit pas être utilisée comme une substitution pour réel diagnostic médical.")


def main():
    st.set_page_config(
        page_title="Dectecteur de Cancer du Sein",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
        )
    
    with open(CSS_FILE) as f :
        st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

    input_data = add_sidebar()
  
    
    with st.container() : 
        st.title("Application de Prédiction du Cancer du Sein")
        st.write("Veuillez connecter ceci à votre laboratoire de cytologie pour aider à diagnostiquer le cancer du sein à partir d'un échantillon tissulaire. " \
        "Cette application prédit à l'aide d'un modèle d'apprentissage automatique si une masse mammaire est bénigne ou maligne en fonction des " \
        "mesures qu'elle reçoit de votre laboratoire de cytologie. Vous pouvez également mettre à jour les mesures manuellement en utilisant les curseurs dans la barre latérale.")

    col1, col2 = st.columns([4,1])

    with col1 : 
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2 :
        add_prediction(input_data)
       


if __name__ == '__main__':
    main()