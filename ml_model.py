import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ==========================
# Load Dataset
# ==========================
df = pd.read_excel("data/sample_-_superstore.xls")

print("Dataset Loaded Successfully!")
print(df.head())

# ==========================
# Data Cleaning
# ==========================
df = df.fillna(0)
df = df.drop_duplicates()

print("\nDataset Shape:")
print(df.shape)

# ==========================
# Select Features & Target
# ==========================
X = df[["Sales", "Quantity", "Discount"]]
y = df["Profit"]

# ==========================
# Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Train Model
# ==========================
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Make Predictions
# ==========================
y_predictions = model.predict(X_test)

# ==========================
# Evaluate Model
# ==========================
mae = mean_absolute_error(y_test, y_predictions)
r2 = r2_score(y_test, y_predictions)

print("\n========== MODEL RESULTS ==========")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# ==========================
# Show Sample Predictions
# ==========================
print("\nFirst 10 Predictions:")
for i in range(10):
    print(
        f"Actual Profit: {round(y_test.iloc[i],2)} | "
        f"Predicted Profit: {round(y_predictions[i],2)}"
    )