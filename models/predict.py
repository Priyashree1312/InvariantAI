import pickle

# Load model
with open("models/saved_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_risk(age, high_risk_flag):
    prob = model.predict_proba([[age, high_risk_flag]])[0][1]
    return float(prob)