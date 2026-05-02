from models.predict import predict_risk
from constraints.validator import validate_all
from constraints.correction import correct_prediction

def run_pipeline(age, flag):
    risk = predict_risk(age, flag)
    print(f"Raw Prediction: {risk:.2f}")

    valid, msg = validate_all(age, risk, flag)

    if not valid:
        print(f"❌ Constraint Failed: {msg}")
        risk = correct_prediction(age, risk, flag)
        print(f"🔧 Corrected Risk: {risk:.2f}")

        valid, msg = validate_all(age, risk, flag)

    print(f"✔ Final Risk: {risk:.2f} ({msg})")

# Example run
run_pipeline(70, 1)