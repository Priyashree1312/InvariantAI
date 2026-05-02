import sys
import os
import subprocess

# ✅ Fix import paths
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models.predict import predict_risk
from constraints.validator import validate_all
from constraints.correction import correct_prediction


# 🔥 REAL LEAN INTEGRATION
def get_lean_proof(p):
    try:
        # Convert 0.72 → 72 for Lean
        scaled = int(p * 100)

        result = subprocess.run(
            ["lake", "env", "lean", "--run", "invariantai/Invariantai/Check.lean", str(scaled)],
            capture_output=True,
            text=True
        )

        proof_output = result.stdout.strip()

        if proof_output == "":
            return "⚠️ Lean did not return output"

        return proof_output

    except Exception as e:
        return f"❌ Lean Error: {str(e)}"


def run_full_pipeline(age, flag):
    # Step 1: Prediction
    risk = predict_risk(age, flag)

    # Step 2: Validation
    is_valid, message = validate_all(age, risk, flag)

    # Step 3: Correction
    corrected = False
    if not is_valid:
        risk = correct_prediction(age, risk, flag)
        corrected = True

    # Step 4: Re-validate AFTER correction
    is_valid_after, _ = validate_all(age, risk, flag)

    # 🔥 Step 5: REAL Lean Proof (replaces fake proof)
    proof = get_lean_proof(risk)

    return {
        "risk": risk,
        "valid": is_valid_after,
        "corrected": corrected,
        "message": message,
        "proof": proof
    }