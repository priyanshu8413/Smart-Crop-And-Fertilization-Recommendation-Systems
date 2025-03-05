import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from catboost import CatBoostClassifier

# Load dataset
input_file = "Purba_Medinipur_Labelled_filtered_dataset.csv"
df = pd.read_csv(input_file)

# Drop missing values if any
df.dropna(inplace=True)

# Separate features (X) and target (y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1].values.ravel()  # 🔥 FIXED: Ensures 1D shape

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save label encoder for later use
with open("label_encoder.pkl", "wb") as le_file:
    pickle.dump(label_encoder, le_file)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Identify categorical features
cat_features = [col for col in X.columns if X[col].dtype == "object"]

# Train CatBoost model
clf = CatBoostClassifier(iterations=1000, depth=6, learning_rate=0.1, random_state=42, verbose=0)
clf.fit(X_train, y_train, cat_features=cat_features)

# Save the trained model
with open("catboost_model.pkl", "wb") as model_file:
    pickle.dump(clf, model_file)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Verify encoded label mapping
print("✅ Encoded Labels Mapping:", dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))))
