import os
import joblib
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .ml_model.features import extract_features

model_path = os.path.join(os.path.dirname(__file__), 'ml_model/model.pkl')
model = joblib.load(model_path)

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url', '')
        features = extract_features(url)
        prediction = model.predict([features])[0]
        return JsonResponse({'result': 'Phishing' if prediction == 1 else 'Legitimate'})
    return JsonResponse({'error': 'Invalid request'}, status=400)