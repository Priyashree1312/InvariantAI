import streamlit as st
from utils import run_full_pipeline

# Page config
st.set_page_config(page_title="Invariant AI", layout="wide")

# Title
st.title("🔐 Invariant AI")
st.subheader("Constraint-Aware Risk Prediction System")

st.markdown("---")

# 🔥 SIDEBAR INPUTS
st.sidebar.header("📥 Input Features")
age = st.sidebar.slider("🎂 Age", 18, 80, 30)
flag = st.sidebar.selectbox("🚨 High Risk Flag", [0, 1])

st.sidebar.markdown("---")
st.sidebar.info("This system ensures predictions follow strict logical constraints.")

# 🔥 MAIN PIPELINE
st.markdown("### ⚙️ System Pipeline")
st.info("Prediction → Validation → Correction → Proof → Final Output")

# BUTTON
if st.button("🚀 Run Prediction"):

    result = run_full_pipeline(age, flag)
    risk = result["risk"]

    st.markdown("## 📊 Prediction Dashboard")

    col1, col2 = st.columns(2)

    # 📊 LEFT SIDE
    with col1:
        st.metric("Risk Score", f"{risk:.2f}")

        # Progress bar
        st.progress(int(risk * 100))
        st.caption(f"Risk Level: {int(risk*100)}%")

        # Color classification
        if risk < 0.3:
            st.success("🟢 Low Risk")
        elif risk < 0.7:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")

    # 🧠 RIGHT SIDE
    with col2:
        if result["corrected"]:
            st.warning("⚠️ Prediction was corrected")

        if result["valid"]:
            st.success("✔ Final prediction is VALID")
        else:
            st.error("❌ Still INVALID")

    st.markdown("---")

    # 🧾 PROOF SECTION
    st.markdown("### 🧾 Formal Verification")
    st.code(result["proof"])

    # 🧠 CONSTRAINT DISPLAY
    st.markdown("### 🧠 Lean Constraint")
    st.code("∀ p, 0 ≤ p ≤ 1")

    # 💡 EXPLANATION BOX
    st.markdown("### 💡 Why this matters")
    st.info(
        "Traditional AI models can produce inconsistent predictions. "
        "Invariant AI ensures that every output is logically valid using formal constraints and verification."
    )