import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Sample Product Data
# -----------------------------
data = {
    "Product": [
        "Laptop",
        "Gaming Mouse",
        "Wireless Mouse",
        "Mechanical Keyboard",
        "USB Cable",
        "Laptop Stand",
        "Monitor",
        "Webcam"
    ],
    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Accessories",
        "Accessories",
        "Accessories",
        "Electronics",
        "Accessories"
    ],
    "Price": [50000, 1500, 1200, 3500, 300, 2000, 12000, 2500]
}

df = pd.DataFrame(data)

# -----------------------------
# Convert Category into Numbers
# -----------------------------
df["Category_Code"] = df["Category"].astype("category").cat.codes

# Features for similarity
features = df[["Category_Code", "Price"]]

# Calculate Similarity
similarity = cosine_similarity(features)

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(product_name):
    if product_name not in df["Product"].values:
        print("Product not found!")
        return

    index = df[df["Product"] == product_name].index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended Products for '{product_name}':\n")

    count = 0
    for i in scores[1:]:
        print(df.iloc[i[0]]["Product"])
        count += 1
        if count == 5:
            break

# -----------------------------
# User Input
# -----------------------------
product = input("Enter Product Name: ")
recommend(product)