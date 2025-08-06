import random
import pandas as pd

def generate_user(user_id, age=None, user_type=None):
    if user_type is None:
        user_type = random.choices(["Salaried", "Freelancer", "Student"], weights=[0.6, 0.25, 0.15])[0]
    if age is None:
        age = random.randint(18, 45)

    location_type = random.choices(["Metro", "Tier-2", "Rural"], weights=[0.5, 0.3, 0.2])[0]

    income_range = {
        "Salaried": (30000, 150000),
        "Freelancer": (15000, 120000),
        "Student": (0, 10000)
    }
    income = random.randint(*income_range[user_type])

    base_expense = income * random.uniform(0.4, 0.7)
    location_multiplier = {"Metro": 1.2, "Tier-2": 1.0, "Rural": 0.8}
    expense = int(base_expense * location_multiplier[location_type])

    rent = 0
    if user_type in ["Salaried", "Freelancer"]:
        rent_range = {
            "Metro": (12000, 35000),
            "Tier-2": (7000, 20000),
            "Rural": (3000, 8000)
        }
        rent = random.randint(*rent_range[location_type])

    emi = 0
    if user_type in ["Salaried", "Freelancer"] and income > 40000:
        emi = random.randint(2000, int(income * 0.25))

    dependents = 0 if user_type == "Student" else random.randint(0, 4)
    insurance = 0 if user_type == "Student" else 500 + (dependents * random.randint(800, 2000))

    tuition = 0

    base_goal = random.randint(500000, 3000000)
    inflation_rate = 0.06
    years = random.randint(5, 15)
    goal_present_value = int(base_goal / ((1 + inflation_rate) ** years))

    investment_preference = random.choices(["Conservative", "Moderate", "Aggressive"], weights=[0.3, 0.5, 0.2])[0]

    obligations = rent + emi + insurance
    savings = max(0, income - expense - obligations)

    return {
        "user_id": user_id,
        "age": age,
        "user_type": user_type,
        "location_type": location_type,
        "income": income,
        "expense": expense,
        "rent": rent,
        "emi": emi,
        "insurance": insurance,
        "dependents": dependents,
        "savings": savings,
        "goal_present_value": goal_present_value,
        "goal_horizon_years": years,
        "investment_preference": investment_preference
    }


def generate_synthetic_dataset(n=100):
    users = []
    for i in range(n):
        user = generate_user(
            user_id=f"user_{i+1}",
            age=random.randint(18, 45),
            user_type=random.choice(["student", "salaried", "freelancer"])
        )
        users.append(user)
    return pd.DataFrame(users)
