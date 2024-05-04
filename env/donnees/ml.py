# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:20:04 2024

@author: pauli
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import accuracy_score


df = pd.read_csv("donnees_voiture_ml.csv",sep=";")
#print(df.head())


from sklearn.preprocessing import LabelEncoder,OneHotEncoder

def categorical_features(df):
    cols = ['Marque', 'Modele','Energie','Transmission','Couleur']
    label_encoder = LabelEncoder()
    for col in cols:
        df[col] = label_encoder.fit_transform(df[col])
    return df

df = categorical_features(df)
#print(df.info())

y = df['Prix']

X = df.drop('Prix', axis=1)
#X = df[['Marque', 'Modele','Annee','Energie','Transmission','Nombres de portes','Puissance','Kilometrage','Nombre de places','Consommation de carburant','Emission de CO2','Couleur']]
#print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "RandomForestRegressor": RandomForestRegressor(),
    "LinearRegression": LinearRegression(),
    "GradientBoostingRegressor": GradientBoostingRegressor(),
    "RidgeCV": RidgeCV(),
    "DecisionTreeRegressor": DecisionTreeRegressor(),
    #"Meilleur résultat": GradientBoostingRegressor(n_estimators=19,random_state=5),
    "Nouveau résultat":RandomForestRegressor(n_estimators=10,random_state=1),
    #"Nouveau nouveau résultat":RandomForestRegressor(max_depth=10, min_samples_leaf= 1, min_samples_split= 2, n_estimators= 300)

}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred, squared=False)
    rmse=(mse)**(1/2)
    
    r2 = r2_score(y_test, y_pred)
    results[name] = {"RMSE": rmse, "R2 Score": r2}


print("Résultats :")
for name, result in results.items():
    print(f"Modèle : {name}")
    print(f"RMSE : {result['RMSE']:.2f}")
    print(f"R2 Score : {result['R2 Score']:.2f}")
    print()
    
"""   
from sklearn.model_selection import GridSearchCV
import numpy as np
import numpy

#on déclare un espace hyperparamétrique pour nos 2 hyperparamètres
C_random=np.arange(0, 20)
C_estimateurs=np.arange(0,20)

#on déclare la grille de valeurs pour les 2 hyperparamètres ,'n_estimators':C_estimateurs
param_grid={'random_state':C_random,'n_estimators':C_estimateurs}

rf=RandomForestRegressor()
#Gb=GradientBoostingRegressor()
rf.fit(X_train,y_train)

#on crée un objet 'reg_cv' de la classe GridSearchCV avec un validation croisée de 5
reg=GridSearchCV(rf, param_grid,cv=5)
reg.fit(X,y) #on entraine sur les données X,y

print('Best Paramètres : {}'.format(reg.best_params_))
print('Best score : {}'.format(reg.best_score_))

#Best Paramètres : {'n_estimators': 15, 'random_state': 21}
#Best score : 0.6241795268013356

#Best Paramètres : {'n_estimators': 14, 'random_state': 9}
#Best score : 0.6203228133780226
"""

"""
model = GradientBoostingRegressor()
model.fit(X_train, y_train)
train_predictions = model.predict(X_train)
train_accuracy = r2_score(y_train, train_predictions)
print("Accuracy on training set:", train_accuracy)

# Évaluer les performances sur l'ensemble de test
test_predictions = model.predict(X_test)
test_accuracy = r2_score(y_test, test_predictions)
print("Accuracy on test set:", test_accuracy)
"""