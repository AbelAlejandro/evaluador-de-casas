import pandas as pd

# Load the Excel file
data = pd.read_excel("~/Downloads/casas/2024_here_we_come.xlsx")

# Convert boolean columns to integers
for column in ["Parrilla", "Hogar a Leña", "Agua Potable", "Dormitorios separados", "Sauna", "Jacuzzi", "Pool"]:
    data[column] = data[column].apply(lambda x: 1 if x == "Si" else 0)

# Define weights for each feature
weights = {
    "Dormitorios separados": 4,
    "Costo por persona": -1,  # Negative because a lower cost is better
    "Distancia a BCN": -1,  # Negative because a lower distance is better
    "Parrilla": 3,
    "Hogar a Leña": 3,
    "Agua Potable": 3,
    "Sauna": 2,
    "Jacuzzi": 1,
    "Pool": 3
}

# Calculate score for each property
data["Score"] = 0
for feature, weight in weights.items():
    data["Score"] += data[feature] * weight * -1

# Sort by score in descending order
data = data.sort_values("Score", ascending=True)

# Print the names and scores of the top 10 properties
print(data[["#", "Nombre", "Score"]].head(10).to_string(index=False))
