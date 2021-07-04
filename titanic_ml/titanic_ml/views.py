from django.shortcuts import render
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
def prediction(Pclass,Sex,Age,Sibsp,Parch,Fare,Embarked,Title):
    x=[[Pclass,Sex,Age,Sibsp,Parch,Fare,Embarked,Title]]
    rf=pickle.load(open('ml_model.sav','rb'))
    predictions=rf.predict(x)
    return predictions
def index (requests):
    return render(requests,'index.html')

def results(requests):
    user_age=int(requests.GET['Age'])
    user_name=int(requests.GET['Salutation'])
    user_sex=int(requests.GET['Sex'])
    user_fare=int(requests.GET['Fare'])
    user_embarked=int(requests.GET['Embarked'])
    user_sibsp=int(requests.GET['sibsp'])
    user_parch=int(requests.GET['Parch'])
    user_pclass=int(requests.GET['Pclass'])
    output=prediction(user_pclass,user_sex,user_age,user_sibsp,user_parch,user_fare,user_embarked,user_name)

    return render(requests,'result.html',{'predictions':output})
