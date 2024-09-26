from django.shortcuts import render
from joblib import load

model = load(r'./saved_models/model.joblib')

# Create your views here.
def predictor(request):
    return render(request, 'index.html')

def formInfo(request):
    if request.method == 'POST':
        Pregnancies = int(request.POST.get('pregnancies', 1))
        Glucose = float(request.POST.get('glucose'))
        Blood_Pressure = int(request.POST.get('bloodpressure'))
        Skin_Thickness = int(request.POST.get('skinthickness'))
        Insulin = int(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        dpf = float(request.POST.get('diabetespedigreefunction'))
        age = int(request.POST.get('age'))

        # Ensure all values are provided
        if None in [Pregnancies, Glucose, Blood_Pressure, Skin_Thickness, Insulin, bmi, dpf, age]:
            return render(request, 'result.html', {'error': 'Please fill in all fields.'})

        prediction = model.predict([[Pregnancies, Glucose, Blood_Pressure, Skin_Thickness, Insulin, bmi, dpf, age]])[0]

        # Handle the prediction result (e.g., display in a human-readable format)
        if prediction == 1:
          prediction_message = "High Risk!!!"
        else:
          prediction_message = "Low Risk!"
        print(prediction)

        return render(request, 'result.html', {'prediction': prediction_message})
    else:
        return render(request, 'index.html')