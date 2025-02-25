import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




data = pd.read_csv("amazon_data.csv")


data['rating'] = data['rating'].str.extract(r"([\d\.]+)").astype(float)


data['reviews'] = data['reviews'].str.replace(",", "").str.extract(r"(\d+)")

data["reviews"] = pd.to_numeric(data["reviews"].str.extract(r"(\d+)")[0], errors="coerce").fillna(0).astype(int)

# Simplify availability status
data['availability'] = data['availability'].apply(lambda x: "Limited Stock" if "Only" in x else "In Stock")

data = data.fillna(0)

print(data["rating"])
print(data["reviews"])
print(data["availability"])


# - Distribution of Ratings -
plt.figure(figsize=(8, 5))
sns.histplot(data['rating'], bins=10, kde=True, color='blue')
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# - Top 5 Products by Reviews -
top_reviews = data.nlargest(5, 'reviews')
plt.figure(figsize=(10, 6))
sns.barplot(data=top_reviews, x='reviews', y='title', palette='viridis')
plt.title("Top 5 Products by Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Product Title")
plt.show()

# - Availability Status -
availability_counts = data['availability'].value_counts()
plt.figure(figsize=(7, 5))
availability_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'skyblue'])
plt.title("Stock Availability Distribution")
plt.ylabel("")  # Remove y-axis label
plt.show()

# - Reviews vs Rating Scatter Plot -
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='rating', y='reviews', hue='availability')
plt.title("Reviews vs Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.legend(title='Availability')
plt.show()
