from django.shortcuts import render
from Prediction import utils  # 👈 import your helper functions

def predict_crop(request):
    if request.method == 'POST':
        n = float(request.POST['nitrogen'])
        p = float(request.POST['phosphorus'])
        k = float(request.POST['potassium'])
        temp = float(request.POST['temperature'])
        hum = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rain = float(request.POST['rainfall'])

        features = [n, p, k, temp, hum, ph, rain]
        prediction = utils.predict_result(features)  # 👈 call the helper function

        return render(request, 'crop.html', {'Prediction': prediction})

    return render(request, 'crop.html')
