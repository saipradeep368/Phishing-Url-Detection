import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load feature data
data = pd.read_csv("url_features.csv")
X = data.drop('label', axis=1)
y = data['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("\nModel Evaluation:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "phishing_model.pkl")
print("\nModel saved to 'phishing_model.pkl'")