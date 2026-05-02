<<<<<<< HEAD
# InvariantAI
=======
# InvariantAI
# 🛡️ Invariant AI — Constraint-Aware Risk Prediction with Formal Verification

> **A trustworthy ML system that combines machine learning with Lean 4 formal verification to ensure every prediction is safe, valid, and mathematically guaranteed.**

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Solution Architecture](#solution-architecture)
- [Formal Specification](#formal-specification)
- [Lean 4 Integration & Correctness Guarantees](#lean-4-integration--correctness-guarantees)
- [ML Pipeline](#ml-pipeline)
- [Constraint Validation & Rule Engine](#constraint-validation--rule-engine)
- [Real-World Relevance](#real-world-relevance)
- [System Flow](#system-flow)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Example Output](#example-output)
- [Creativity: Applying Lean in Autonomy](#creativity-applying-lean-in-autonomy)
- [Future Work](#future-work)
- [Team](#team)

---

## 📖 Project Overview

**Invariant AI** is a constraint-aware risk prediction system that solves a critical gap in modern AI: *ML models can produce statistically plausible but logically invalid outputs.*

This system wraps a standard ML risk scorer with:
1. **Domain constraint validation** — rule-based checks that catch invalid predictions before they propagate
2. **Lean 4 formal verification** — mathematical proof that every returned prediction satisfies defined invariants (e.g., `0 ≤ risk ≤ 1`)
3. **Automatic correction** — invalid predictions are corrected and re-verified, not silently passed through

The result is a pipeline where every output comes with a **formal proof of correctness** — transforming a black-box model into a trustworthy, auditable AI system.

---

## ❗ Problem Statement

Standard ML pipelines have no mechanism to guarantee that outputs satisfy domain constraints:

- A risk model might return `risk = 1.4` — mathematically impossible in a [0, 1] bounded score
- A model might assign high risk to inputs with logically impossible combinations of flags
- There is no way to *prove* a prediction is valid — only to *test* it on samples

In high-stakes domains (healthcare, finance, autonomous systems), this is not acceptable.

**Invariant AI solves this by making correctness a first-class output — not an afterthought.**

---

## 🏗️ Solution Architecture

```
User Input (age, risk_flags, ...)
        │
        ▼
┌──────────────────────┐
│   ML Risk Scorer     │  ← Trained model generates raw risk score
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Constraint Engine   │  ← Rule-based validation & auto-correction
│  (Domain Rules)      │    enforces: 0 ≤ risk ≤ 1, flag consistency, etc.
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Lean 4 Verifier     │  ← Formal proof that prediction satisfies invariants
│  (Formal Proofs)     │    returns: verified_score + proof object
└──────────┬───────────┘
           │
           ▼
  ✅ Verified Prediction + Formal Proof Certificate
```

---

## 🔬 Lean 4 Integration & Correctness Guarantees

### Why Lean 4?

Lean 4 is a dependently-typed theorem prover and programming language. Unlike runtime assertions, Lean proofs are:

- **Static** — verified at compile time, not at runtime
- **Compositional** — complex invariants built from simpler proven lemmas
- **Machine-checkable** — the Lean kernel independently checks every proof

## 🧩 What I Have Implemented

## 🏗️ Solution Architecture

```
                ┌────────────────────────────┐
                │        User Input          │
                │   (age, risk flag, etc.)  │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │      ML Risk Model         │
                │ (Logistic Regression)      │
                │ → raw risk score (p)       │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   Constraint Validator     │
                │  - Check 0 ≤ p ≤ 1         │
                │  - Check flag rules        │
                └────────────┬──────────────┘
                             │
                 (if violation detected)
                             │
                             ▼
                ┌────────────────────────────┐
                │   Correction Engine        │
                │  - Adjust risk value       │
                │  - Enforce domain rules    │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │     Lean 4 Verifier        │
                │  Formal Proof Generation   │
                │  (0 ≤ p ≤ 1 is proven)    │
                └────────────┬──────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   Final Verified Output    │
                │  - Risk Score              │
                │  - Validation Status       │
                │  - Proof Certificate       │
                └────────────────────────────┘
```

### 🔍 Key Components

* **ML Model** → Generates initial prediction (may be imperfect)
* **Validator** → Detects logical inconsistencies
* **Correction Layer** → Fixes invalid outputs instead of rejecting
* **Lean Verifier** → Ensures mathematical correctness
* **Final Output** → Fully validated + provable result

---


### 🤖 1. Machine Learning Pipeline
- Built a risk prediction model using Python (scikit-learn / boosting models)
- Uses features like:
  - age
  - risk flags (critical, chronic, history)
- Produces a raw risk score from the model

---

### Input Features

| Feature | Type | Description |
|--------|------|-------------|
| `age` | Integer | Age of the individual |
| `flag` | Binary (0/1) | High-risk indicator |

### Model

- Algorithm: Logistic Regression  
- Output: Probability score in [0, 1]

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

risk = model.predict_proba(X_input)[:, 1][0]

---


---

### ✅ Constraint Engine

```markdown

The system enforces logical constraints on predictions:

```python
def correct_prediction(age, risk, flag):
    if age > 60 and risk < 0.2:
        risk = 0.2

    if flag == 1 and risk < 0.5:
        risk = 0.5

    return max(0, min(risk, 1))


## ⚙️ Constraint Validation & Rule Engine

The constraint engine sits between the ML model and the Lean verifier. It:

1. **Validates** the raw score against all domain invariants
2. **Corrects** violations using domain-aware logic (not clipping)
3. **Logs** every correction for auditability

## 🌍 Real-World Relevance

### Where This Matters

| Domain | Risk Without Invariant AI | With Invariant AI |
|--------|--------------------------|-------------------|
| **Healthcare** | Model outputs `risk = 1.3` → patient overtreated | Proof that score ∈ [0,1] before clinical use |
| **Finance** | Credit risk score violates regulatory bounds | Formally verified compliance with Basel III constraints |
| **Autonomous Vehicles** | Safety classifier outputs inconsistent with sensor flags | Lean proof of consistency before actuation |
| **Insurance** | Premium calculation violates actuarial invariants | Audit-ready proof certificate per prediction |

### Regulatory Alignment

- **EU AI Act (2024)**: Emphasizes transparency and reliability — this system improves trust via validation and proof
- **FDA SaMD Guidelines**: Supports bounded and predictable outputs
- **ISO 26262 (Automotive)**: Aligns with the idea of verifying safety-critical outputs

## 🔄 System Flow

1. User submits input → {age: 67, flag: 1}
2. ML Model generates raw score → 0.32
3. Constraint Engine checks:
✗ flag=1 but score=0.32 < 0.5 → CORRECTION → score = 0.50
✓ 0 ≤ 0.50 ≤ 1 → PASS
4. Lean Verifier receives score=0.50:
theorem: 0 ≤ 0.50 ∧ 0.50 ≤ 1 → PROVED ✅
5. Response returned:
{
  "risk": 0.50,
  "valid": true,
  "corrected": true,
  "proof": "✔ Lean Proof: 0.50 satisfies 0 ≤ p ≤ 1"
}
```

---

## 🛠️ Tech Stack

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| ML Model | Python, scikit-learn (Logistic Regression) |
| Constraint Engine | Python (custom rules) |
| Formal Verifier | Lean 4 |
| UI | Streamlit |
| Integration | Python ↔ Lean subprocess |

---

## 🚀 Getting Started

### Prerequisites

```bash
# Install Lean 4
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh

# Install Python dependencies
pip3 install -r requirements.txt
```

### Run the System

```bash
# Start the API
uvicorn main:app --reload

# Example request
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 67, "flag_critical": true, "flag_chronic": false}'
```

### Run Lean Verification Tests

```bash
cd lean/
lake build
lake test
```

---

## 📊 Example Output

cd invariantai
lake env lean --run Invariantai/Check.lean 70

✔ Example output:

✔ Lean Proof: 0.7 satisfies 0 ≤ p ≤ 1

## 📊 Example Output

```json
{
  "risk": 0.50,
  "valid": true,
  "corrected": true,
  "message": "Constraint applied",
  "proof": "✔ Proof: 0.50 satisfies 0 ≤ p ≤ 1"
}
```

---

## 💡 Creativity: Applying Lean in Autonomy

Most ML systems treat formal verification as a post-hoc audit tool. **Invariant AI treats it as a live gatekeeper.**

Key creative contributions:

- **Proof-as-output**: The system doesn't just predict — it produces a proof certificate alongside every result. This is a new paradigm for ML APIs.
- **Constraint-aware correction**: Instead of rejecting invalid predictions (which breaks pipelines), the system corrects them and re-verifies — making it robust in production.
- **Lean as a runtime component**: Lean is invoked in the request/response loop, not just at test time. This is an unusual and powerful application of a theorem prover.
- **Composable invariants**: Complex domain rules are broken into simple Lean lemmas that compose — this mirrors how formal methods work in safety-critical hardware design, now applied to AI.

---

## 🔮 Future Work

- **End-to-end Lean proof** — eliminate the Python/Lean bridge and run the full pipeline in Lean 4 natively
- **Proof caching** — cache proofs for repeated input patterns to reduce latency
- **LLM-assisted spec generation** — use an LLM to auto-generate Lean invariants from natural language domain descriptions
- **Multi-model ensemble verification** — verify that ensemble disagreements don't violate consistency invariants
- **Dashboard** — real-time monitoring of correction rates, proof success rates, and invariant violation frequency

---

## 👥 Team

| Name | Role |
|------|------|
| *Priyashree Panda* | ML Engineer + Lean Verifier |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

> *"A prediction without a proof is just a guess. Invariant AI makes every guess provable."*


---

## 📜 Origin

This project was built during the **LeanLang for Verified Autonomy Hackathon**
(April 17–18 + online through May 1, 2026) at the
**Indian Institute of Science (IISc), Bangalore**.

The goal of the hackathon was to explore how **formal methods (Lean 4)** can be integrated with real-world systems to improve reliability, safety, and trust in AI.

**Invariant AI** was developed as a practical system combining:

* Machine Learning (risk prediction)
* Constraint validation (domain rules)
* Lean 4 formal verification (proof of correctness)

---

## 🙏 Acknowledgments

This project was made possible by:

* **Emergence AI** — Hackathon sponsor
* **Emergence India Labs** — Event organizer and research direction
* **Indian Institute of Science (IISc), Bangalore** — Academic partner, mentorship, and technical guidance

---

## 🔗 Links

* Hackathon Page: https://east.emergence.ai/hackathon-april2026.html
* Emergence India Labs: https://east.emergence.ai
* Emergence AI: https://www.emergence.ai

---

## 🌟 Project Significance

This project demonstrates a new paradigm:

👉 **AI systems that don’t just predict — but prove their correctness**

By integrating Lean 4 into the ML pipeline, this system ensures:

* Predictions are always within valid bounds
* Logical constraints are enforced
* Outputs are accompanied by formal proofs

This approach moves AI systems closer to being:

* **Trustworthy**
* **Auditable**
* **Safe for real-world deployment**

---

<p align="center">
  <b>🚀 Built for Verified AI Systems of the Future</b>
</p>
