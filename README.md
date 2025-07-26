**Project Overview**
This project provides a real-time churn prediction API for the telecommunications industry. 
By leveraging a pre-trained machine learning model and incorporating insights extracted from customer interaction notes using Generative AI, it aims to accurately identify customers at risk of churning. 
The solution is packaged as a lightweight Flask API, ready for deployment.

**Key Features**
Accurate Churn Prediction: Utilizes a finely tuned machine learning model (e.g., XGBoost, specified in model.json) to predict customer churn based on structured customer data.

Generative AI for Feature Enhancement: Integrates Generative AI to analyze unstructured customer interaction notes, extracting key sentiments and risk labels. 
These AI-derived insights enhance the model's predictive capabilities.

Real-time Inference API: Provides a robust Flask API endpoint for real-time churn predictions, allowing seamless integration into business applications.

Simplified Deployment: Designed for straightforward deployment as a web service.

**Problem Statement**
Customer churn represents a significant revenue loss for telecom companies. 
While traditional models use structured data, valuable contextual information often resides in unstructured customer support interactions. 
This project addresses this by demonstrating how Generative AI can unlock these hidden insights, providing a more comprehensive and accurate churn prediction system accessible via a simple API.

**Architecture**
The solution operates as a single-endpoint API:

API Request: An incoming POST request to the /predict endpoint contains both structured customer data and an InteractionNotes field.

Generative AI Processing: The InteractionNotes are processed by a GenAI component (integrated within app.py) to extract relevant sentiment and risk features.

Feature Combination: These GenAI-derived features are combined with the structured input data.

Model Inference: The combined features are fed into the pre-trained machine learning model (model.json) for churn prediction.

API Response: The API returns the churn prediction, probability, and the GenAI-extracted insights.

**Technologies Used**
Programming Language: Python

Machine Learning: Scikit-learn, Pandas, NumPy, XGBoost

Generative AI: OpenAI API

Web Framework: Flask

**Getting Started**
This section will guide you through setting up and running the Flask API locally, and how to interact with it using Postman.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x

pip

Postman

**Installation**
Clone the Repository:

Bash

git clone https://github.com/your_username/Telecom_Churn_Analysi.git
cd Telecom_Churn_Analysis


Install Dependencies:

Bash

pip install -r requirements.txt

Running the Flask Application Locally
Once the dependencies are installed, you can start the Flask API:

Bash

python app.py


**Making Predictions with Postman**
You can use Postman to send requests to the running Flask API and get churn predictions.

Open Postman: Launch the Postman application.

Create a New Request:

Click the + icon to open a new tab.

Set the HTTP Method to POST.

Enter the Request URL: http://127.0.0.1:5000/predict

Configure Request Body:

Go to the Body tab.

Select raw and choose JSON from the dropdown.

Enter the input data for prediction in JSON format. The keys must match the column names your model expects, including InteractionNotes.

Example JSON Body

JSON

{
    "CustomerID": "C12345",
    "Surname": "Doe",
    "NetworkForRegion": "North",
    "Gender": "Male",
    "Age": 30,
    "Tenure": 24,
    "MonthlyCharges": 75.5,
    "NumOfProducts": 2,
    "HasInternetService": "Yes",
    "IsActiveMember": "Yes",
    "EstimatedSalary": 55000.00,
    "InteractionNotes": "Customer called regarding a billing discrepancy. Very frustrated with the recent service quality."
}
Send the Request:

Click the Send button.

View the Response:

The API's response will appear in the response section of Postman. It should include the churn prediction and any GenAI-extracted details.

Example JSON Response:

JSON

{
  "churn_prediction": "Yes",
  "churn_probability": 0.72,
  "genai_sentiment": "Negative",
  "genai_risk_tags": ["Billing Discrepancy", "Service Quality Issue"]
}

Project Structure
.
├── app.py                   # Flask application for the API endpoint, model loading, and GenAI processing
├── model.json               # Pre-trained machine learning model artifact (or whatever format your model is saved in)
├── requirements.txt         # Python dependencies
└── README.md                # This file
