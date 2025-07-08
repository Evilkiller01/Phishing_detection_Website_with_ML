import joblib
from xgboost import XGBClassifier
import numpy as np
import os

# Get the absolute path to save the model
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'model.pkl')

# Training data
X_train = np.array([
    [1, 50, 0, 0, 3],  # Phishing
    [0, 30, 0, 0, 2],  # Legitimate
    [1, 70, 1, 1, 5],  # Phishing
    [0, 25, 0, 0, 1],  # Legitimate
    [1, 60, 0, 1, 4],  # Phishing
    [0, 35, 0, 0, 2],  # Legitimate
    [1, 55, 1, 0, 3],  # Phishing
    [0, 40, 0, 0, 3],  # Legitimate
])

y_train = np.array([1, 0, 1, 0, 1, 0, 1, 0])  # 1 = Phishing, 0 = Legitimate

try:
    print("Training model...")
    model = XGBClassifier()
    model.fit(X_train, y_train)
    
    print(f"Saving model to {model_path}...")
    joblib.dump(model, model_path)
    
    # Verify the file was created
    if os.path.exists(model_path):
        print("Success! model.pkl created successfully.")
    else:
        print("Error: model.pkl was not created. Check directory permissions.")
except Exception as e:
    print(f"Error occurred: {str(e)}")