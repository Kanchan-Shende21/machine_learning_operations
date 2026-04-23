import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Create dataset inside code (no CSV needed)
data = {
    "Age": [25, 30, 35, 40, 22, 28, 50, 45],
    "Salary": [50000, 60000, 80000, 90000, 40000, 52000, 100000, 85000],
    "Purchased": [0, 1, 1, 1, 0, 0, 1, 1]
}

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Convert DataFrame → dataset (NumPy)
dataset = df.values
print("Dataset:\n", dataset)

# 4. Split features and target
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 6. Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# 7. Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)