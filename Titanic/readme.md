# Résum du projet

## Objectif
L'objectif de ce projet est d'analyser les données du Titanic, de les préparer pour l'entraînement de modèles de machine learning, et d'évaluer plusieurs algorithmes de classification pour prédire la survie des passagers.

---

## Étapes réalisées

### 1. Chargement et exploration des données
- Les données ont été chargées depuis les fichiers `train.csv` et `test.csv`.
- Exploration initiale des données avec les méthodes `head()`, `shape`, `info()`, et `describe()` pour comprendre la structure et les caractéristiques des données.

### 2. Analyse des valeurs manquantes
- Calcul des pourcentages de valeurs manquantes pour chaque colonne.
- Suppression de la colonne `Cabin` en raison d'un grand nombre de valeurs manquantes.
- Imputation des valeurs manquantes dans la colonne `Age` avec la médiane.
- Suppression des lignes avec des valeurs manquantes dans la colonne `Embarked`.

### 3. Analyse exploratoire des données (EDA)
- Visualisation de la distribution de la variable cible `Survived` avec un `countplot`.
- Analyse des corrélations entre les variables numériques et la survie avec une heatmap.
- Analyse bivariée entre `Sex` et `Survived`, ainsi qu'entre `Embarked` et `Survived` avec des barplots.

### 4. Préparation des données
- Encodage des variables catégoriques (`Sex` et `Embarked`) avec `LabelEncoder`.
- Normalisation de la colonne `Fare` avec `StandardScaler`.
- Sélection des caractéristiques pertinentes (`Embarked`, `Sex`, `Pclass`) pour l'entraînement des modèles.

### 5. Entraînement et évaluation des modèles
#### Modèles testés :
1. **Random Forest Classifier**
    - Précision : 0.80
    - Rapport de classification et matrice de confusion affichés.
    - Optimisation des hyperparamètres avec `GridSearchCV` pour trouver les meilleurs paramètres :
      - `n_estimators`: 50
      - `max_depth`: None
      - `min_samples_split`: 2

2. **Decision Tree Classifier**
    - Précision : 0.80
    - Rapport de classification et matrice de confusion affichés.

3. **K-Nearest Neighbors (KNN)**
    - Précision : 0.95
    - Optimisation des hyperparamètres avec `GridSearchCV` :
      - `n_neighbors`: 3
      - `weights`: uniform
      - `algorithm`: auto

4. **Autres modèles**
    - Plusieurs autres modèles ont été testés (SVM, GaussianNB, AdaBoost, etc.) dans une boucle pour comparer leurs performances sur des jeux de données synthétiques.

### 6. Visualisation des résultats
- Comparaison des résultats prédits et attendus pour le modèle KNN avec un graphique linéaire.
- Visualisation des frontières de décision pour différents modèles sur des jeux de données synthétiques.

---

## Résultats principaux
- **Random Forest** a obtenu les meilleures performances avec une précision de 83% après optimisation des hyperparamètres.
- **Decision Tree** et **KNN** ont également montré des performances acceptables, mais légèrement inférieures.
- Les analyses exploratoires ont révélé que le sexe et la classe (`Pclass`) sont des facteurs importants pour prédire la survie.

---

## Conclusion
Ce projet a permis de mettre en œuvre un pipeline complet de machine learning, depuis l'exploration des données jusqu'à l'évaluation des modèles. Les résultats montrent que les modèles basés sur des arbres de décision, comme Random Forest, sont bien adaptés à ce type de problème.
```