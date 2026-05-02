import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv("data/processed/processed_data.csv")

X = df[["age", "high_risk_flag"]]
y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("models/saved_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")

