#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import numpy as np
from xgboost import XGBClassifier


# In[2]:

app = Flask(__name__)

# Load XGBoost model from JSON (version-safe)
model = XGBClassifier()
model.load_model("model.json")

# In[3]:

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input features from request
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(features)

        # Return prediction as JSON
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# In[ ]:


if __name__ == '__main__':
    app.run(debug=True)

# In[ ]:




