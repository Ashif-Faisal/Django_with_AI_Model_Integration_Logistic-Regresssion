from django.http import HttpResponse
from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd
import joblib


# Create your views here.
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            age = request.POST.get('age')
            print(age)
            df = pd.DataFrame({'age': [age]})
            print(df)
            model = joblib.load('model_prediction/logistic_regression_model.pkl')
            news = model.predict(df)
            print(news)

            if news[0]==0:
                return HttpResponse('Unmarride')
            else:
                return HttpResponse('Marride')
    else:
        form = PredictionForm()
    return render(request, "predict.html", {"form": form})
