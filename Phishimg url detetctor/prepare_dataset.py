import pandas as pd
from extract_features import extract_features

# Load dataset
df = pd.read_csv("sample_urls.csv")  # Create or download a dataset with 'url' and 'label' columns

# Extract features
feature_data = [extract_features(url) for url in df['url']]
features_df = pd.DataFrame(feature_data)

# Add labels
features_df['label'] = df['label'].map({'legitimate': 0, 'phishing': 1})

# Save processed data
features_df.to_csv("url_features.csv", index=False)
print("Feature extraction complete. Saved to 'url_features.csv'")