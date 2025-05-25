import streamlit as st
import joblib
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load("xgboost_titanic_model.pkl")

# Titre de l'application
st.title("Prédiction de survie sur le Titanic")

# Formulaire pour saisir les données utilisateur
st.sidebar.header("Entrer les caractéristiques du passager :")

pclass = st.sidebar.selectbox("Classe du billet (Pclass)", [1, 2, 3])
sex = st.sidebar.selectbox("Sexe", ["male", "female"])
age = st.sidebar.slider("Âge", 0, 80, 30)
sibsp = st.sidebar.slider("Nombre de frères/soeurs/conjoints (SibSp)", 0, 8, 0)
parch = st.sidebar.slider("Nombre de parents/enfants (Parch)", 0, 6, 0)
fare = st.sidebar.slider("Tarif payé (Fare)", 0.0, 500.0, 32.0)
embarked = st.sidebar.selectbox("Port d'embarquement (Embarked)", ["C", "Q", "S"])

# Prétraitement des données utilisateur
sex_male = 1 if sex == "male" else 0
embarked_C = 1 if embarked == "C" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

# Créer un tableau des caractéristiques
features = np.array([[pclass, age, sibsp, parch, fare, sex_male, embarked_C, embarked_Q]])

# Prédire la survie
if st.button("Prédire la survie"):
    prediction = model.predict(features)
    result = "Survécu" if prediction[0] == 1 else "Non survécu"
    st.write(f"Résultat de la prédiction : **{result}**")