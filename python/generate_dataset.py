from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import random

fake = Faker("en_IN")
products = [
    "Laptop", "Mobile", "Headphones", "Keyboard", "Mouse",
    "Monitor", "Printer", "Chair", "Table", "Camera",
    "Smart Watch", "Speaker", "Router", "Hard Disk", "SSD"
]

categories = {
    "Laptop": "Electronics",
    "Mobile": "Electronics",
    "Headphones": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Monitor": "Electronics",
    "Printer": "Electronics",
    "Chair": "Furniture",
    "Table": "Furniture",
    "Camera": "Electronics",
    "Smart Watch": "Electronics",
    "Speaker": "Electronics",
    "Router": "Networking",
    "Hard Disk": "Storage",
    "SSD": "Storage"
}
data = []

for i in range(1, 1001):

    product = random.choice(products)
    category = categories[product]

    quantity = random.randint(1, 5)
    sales = random.randint(500, 50000)
    profit = round(sales * random.uniform(0.05, 0.30), 2)

    data.append({
        "Order_ID": i,
        "Order_Date": fake.date_between(start_date='-1y', end_date='today'),
        "Customer_Name": fake.name(),
        "State": fake.state(),
        "Category": category,
        "Product_Name": product,
        "Quantity": quantity,
        "Sales": sales,
        "Profit": profit
    })
    df = pd.DataFrame(data)
    import os
    os.makedirs("../Dataset",exist_ok=True)
    from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"
DATASET_DIR.mkdir(exist_ok=True)

df.to_csv(DATASET_DIR / "ecommerce_advanced.csv", index=False)

print("✅ Advanced Dataset Created Successfully!")
print(df.head())
print("Shape:", df.shape)
    