# 🌱 Boolean Logic Based Crop Condition Classifier
https://sri-shalini.github.io/boolean-crop-condition-classifer/
A simple Streamlit web application that classifies crop conditions using Boolean logic based on important agricultural factors.

## 📌 Project Description

This project checks whether the required conditions for healthy crop growth are satisfied.

The application takes four crop conditions as input:

- 🌧️ Sufficient Rainfall
- 💧 Good Soil Moisture
- 🌡️ Suitable Temperature
- ☀️ Sufficient Sunlight

Based on these conditions, the application classifies the crop condition.

## 🧠 Logic Used

The crop is considered to have a **Good Crop Condition** when all the required conditions are satisfied:

```text
Rainfall AND Soil Moisture AND Temperature AND Sunlight
