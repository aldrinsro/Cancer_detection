# Application de Prédiction du Cancer du Sein 🏥

Une application web interactive basée sur **Streamlit** pour prédire si une tumeur mammaire est bénigne ou maligne à partir de mesures de noyaux cellulaires.

## 📋 Description

Cette application utilise un modèle d'apprentissage automatique entraîné pour analyser les mesures de 30 caractéristiques cytologiques (rayons, textures, périmètres, etc.) et prédire la probabilité qu'une masse mammaire soit bénigne ou maligne.

### Caractéristiques mesurées

L'application analyse trois catégories de mesures :
- **Moyenne (mean)** : Valeurs moyennes des 10 caractéristiques
- **Écart-type (se)** : Erreurs standards des 10 caractéristiques
- **Pire (worst)** : Pires valeurs des 10 caractéristiques

Les 10 caractéristiques principaux :
1. Rayon (Radius)
2. Texture (Texture)
3. Périmètre (Perimeter)
4. Aire (Area)
5. Lissage (Smoothness)
6. Compacité (Compactness)
7. Concavité (Concavity)
8. Points concaves (Concave points)
9. Symétrie (Symmetry)
10. Dimension fractale (Fractal dimension)

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd Cancer_detection
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Structurer les fichiers**
   Assurez-vous que le projet a la structure suivante :
   ```
   Cancer_detection/
   ├── app/
   │   └── main.py
   ├── data/
   │   └── data.csv
   ├── model/
   │   ├── main.py
   │   ├── model.pkl
   │   └── scaler.pkl
   ├── requirements.txt
   └── README.md
   ```

## 💻 Utilisation

### Lancer l'application

Depuis le dossier `app/` :
```bash
streamlit run main.py
```

L'application s'ouvrira dans votre navigateur par défaut à `http://localhost:8501`

### Comment utiliser

1. **Ajuster les mesures** : Utilisez les curseurs dans la barre latérale gauche pour entrer les 30 mesures cellulaires
2. **Visualiser les données** : Un graphique radar affiche les mesures normalisées
3. **Obtenir une prédiction** : L'application affiche :
   - Le diagnostic (bénigne ou maligne)
   - La probabilité de bénignité
   - La probabilité de malignité

## 📊 Architecture du projet

### Structure des fichiers

- **app/main.py** : Application Streamlit principale
- **model/main.py** : Script d'entraînement du modèle
- **model/model.pkl** : Modèle d'apprentissage automatique sérialisé
- **model/scaler.pkl** : Objet de normalisation des données
- **data/data.csv** : Données d'entraînement
- **requirements.txt** : Dépendances Python

### Fonctions principales

| Fonction | Description |
|----------|-------------|
| `get_clean_data()` | Charge et nettoie les données |
| `get_scaled_values()` | Normalise les valeurs entre 0 et 1 |
| `add_sidebar()` | Crée l'interface des curseurs latéraux |
| `get_radar_chart()` | Génère le graphique radar 3D |
| `add_prediction()` | Charge le modèle et affiche la prédiction |

## ⚠️ Avertissements importants

> **Cette application peut assister les professionnels de la santé pour le diagnostic, mais ne doit pas être utilisée comme substitution à un diagnostic médical réel.**

- Les prédictions doivent être validées par un professionnel médical
- Les résultats sont indicatifs uniquement
- Ne pas utiliser à des fins diagnostiques définitives sans consultation médicale

## 📦 Dépendances

- `streamlit` : Framework web pour l'application
- `pickle` : Sérialisation du modèle et du scaler
- `pandas` : Manipulation et analyse de données
- `plotly` : Visualisations interactives
- `numpy` : Calculs numériques
- `scikit-learn` : Modèle d'apprentissage automatique

## 🔧 Configuration

### Modifier le modèle

Pour réentraîner le modèle avec de nouvelles données :
```bash
python model/main.py
```

Cela générera les fichiers :
- `model/model.pkl`
- `model/scaler.pkl`

## 📈 Performance

- **Entrées** : 30 mesures de noyaux cellulaires
- **Sortie** : Diagnostic binaire (bénigne/maligne) + probabilités
- **Temps de prédiction** : < 1 seconde

## 👥 Contribution

## 📝 Licence

Ce projet est fourni à titre éducatif

## 📧 Support

Pour toute question ou problème, veuillez vérifier :
1. Que tous les fichiers `.pkl` sont présents dans le dossier `model/`
2. Que le fichier `data.csv` existe dans le dossier `data/`
3. Que tous les paquets requis sont installés

---
