#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import pickle
import numpy as np


# In[2]:


# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)


# In[3]:


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




