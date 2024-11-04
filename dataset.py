import pandas as pd
import random
from datetime import datetime, timedelta

# Define categories and descriptions for synthetic expense data
categories = ["Food", "Transportation", "Utilities", "Entertainment", "Healthcare", "Shopping"]
descriptions = {
    "Food": ["Groceries", "Restaurant", "Coffee shop", "Fast food", "Supermarket"],
    "Transportation": ["Uber", "Bus ticket", "Train ticket", "Gas station", "Car rental"],
    "Utilities": ["Electricity bill", "Water bill", "Internet bill", "Phone bill", "Gas bill"],
    "Entertainment": ["Movie ticket", "Concert", "Streaming service", "Bowling", "Gaming"],
    "Healthcare": ["Pharmacy", "Doctor visit", "Gym membership", "Therapy", "Vitamins"],
    "Shopping": ["Clothes", "Electronics", "Books", "Home decor", "Gift"]
}

# Generate a list of dates for the past 2 months
start_date = datetime.now() - timedelta(days=60)
dates = [start_date + timedelta(days=i) for i in range(60)]

# Generate synthetic data
data = []
for date in dates:
    # Randomly select number of expenses per day
    num_expenses = random.randint(1, 4)
    for _ in range(num_expenses):
        category = random.choice(categories)
        description = random.choice(descriptions[category])
        amount = round(random.uniform(5, 150), 2)  # Random expense amount between 5 and 150
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "description": description,
            "amount": amount,
            "category": category
        })

# Convert to DataFrame
expense_data = pd.DataFrame(data)
# Save the full synthetic expense data for the past 2 months to a CSV file
file_path = 'expenseData.csv'
expense_data.to_csv(file_path, index=False)

file_path


