import pandas as pd
from faker import Faker
import random
import numpy as np

# Initialize Faker
faker = Faker()

# Number of records to generate
num_records = 30000

import random
from faker import Faker
import pandas as pd

faker = Faker()

# List of occupations based on the screenshots
occupations = [
    "Accountant", "Architect", "Developer", "Doctor", "Engineer", 
    "Entrepreneur", "Journalist", "Lawyer", "Manager", "Mechanic", 
    "Media_Manager", "Musician", "Scientist", "Teacher", "Writer"
]

customers = []

for _ in range(num_records):
    is_male = random.choice([True, False])
    first_name = faker.first_name_male() if is_male else faker.first_name_female()
    last_name = faker.last_name()
    
    # Additional columns
    age = random.randint(22, 60)  # Age between 22 and 60
    gender = 'Male' if is_male else 'Female'
    account_creation_date = faker.date_this_decade()
    
    # Generating SSN in the format xxx-xx-xxxx
    ssn = f"{random.randint(100, 999)}-00-{random.randint(1000, 9999)}"
    
    # Generate annual income between 30,000 and 120,000
    annual_income = random.randint(30000, 120000)
    
    # Monthly in-hand salary (assuming 12 months in a year)
    monthly_inhand_salary = annual_income / 12
    
    # Assign a random occupation from the list
    occupation = random.choice(occupations)
    
    cities = [faker.city() for _ in range(200)] 
    city = random.choice(cities)
    
    customers.append({
    "customer_id": _ + 1,
    "first_name": first_name,
    "last_name": last_name,
    "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
    # "address": faker.address().replace("\n", " ").replace(",", ""),  # Remove commas
    "city": city, 
    "state": faker.state(),
    "postal_code": faker.zipcode(),
    "phone_number": faker.phone_number(),
    "gender": gender,
    "age": age,
    "account_creation_date": account_creation_date,
    "ssn": ssn,  # Adding SSN column
    "annual_income": annual_income,  # Adding Annual_Income column
    "monthly_inhand_salary": monthly_inhand_salary,  # Adding Monthly_Inhand_Salary column
    "occupation": occupation  # Adding Occupation column
})


customers_df = pd.DataFrame(customers)
customers_df.to_csv('DimCustomers.csv', index=False)

# Generate DimCustomers with more realistic names and emails
customers = []
for _ in range(num_records):
    first_name = faker.first_name_male() if random.choice([True, False]) else faker.first_name_female()
    last_name = faker.last_name()
    customers.append({
        "customer_id": _ + 1,
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
        "address": faker.address().replace("\n", ", "),
        "city": faker.city(),
        "state": faker.state(),
        "postal_code": faker.zipcode(),
        "phone_number": faker.phone_number()
    })
customers_df = pd.DataFrame(customers)
customers_df.to_csv('DimCustomers.csv', index=False)

# Generate DimLoan with realistic loan types and interest rates
loans = []
for _ in range(num_records):
    loan_type = random.choice(["Personal", "Auto", "Mortgage", "Student"])
    loans.append({
        "loan_id": _ + 1,
        "loan_type": loan_type,
        "loan_amount": round(random.uniform(1000, 50000), 2),
        "interest_rate": round(random.uniform(3.0, 6.0) if loan_type == "Mortgage" else random.uniform(1.0, 5.0), 2)
    })
loans_df = pd.DataFrame(loans)
loans_df.to_csv('DimLoan.csv', index=False)

# Generate DimAccount with realistic balances and credit scores
accounts = []
for _ in range(num_records):
    accounts.append({
        "account_id": _ + 1,
        "account_number": faker.bban(),
        "customer_id": random.randint(1, num_records),  # Linking to a customer
        "account_type": random.choice(["Savings", "Checking", "Credit"]),
        "account_balance": round(abs(random.gauss(2000, 1500)), 2),  # More realistic balances
        "credit_score": round(np.clip(random.gauss(700, 50), 300, 850))  # More realistic credit score distribution
    })
accounts_df = pd.DataFrame(accounts)
accounts_df.to_csv('DimAccount.csv', index=False)

# Generate FactTransactions with realistic amounts based on transaction type
transaction_types = [
    {"transaction_type_id": 1, "description": "Deposit"},
    {"transaction_type_id": 2, "description": "Withdrawal"},
    {"transaction_type_id": 3, "description": "Transfer"},
    {"transaction_type_id": 4, "description": "Payment"},
    {"transaction_type_id": 5, "description": "Wire Transfer"},
    {"transaction_type_id": 6, "description": "ATM Withdrawal"},
    {"transaction_type_id": 7, "description": "Online Purchase"},
    {"transaction_type_id": 8, "description": "Bill Payment"},
    {"transaction_type_id": 9, "description": "Interest Payment"},
    {"transaction_type_id": 10, "description": "Refund"}
]

transaction_types_df = pd.DataFrame(transaction_types)
transaction_types_df.to_csv('DimTransactionType.csv', index=False)

transactions = []
for _ in range(num_records):
    txn_type_id = random.randint(1, len(transaction_types))
    transactions.append({
        "transaction_id": _ + 1,
        "customer_id": random.randint(1, num_records),
        "txn_date_id": random.randint(1, 365),
        "channel_id": random.randint(1, 5),  # Channel linking to DimChannel
        "account_id": random.randint(1, num_records),
        "txn_type_id": txn_type_id,
        "txn_amount": round(random.uniform(100, 500) if txn_type_id == 1 else random.uniform(10, 200), 2),  # Realistic amounts based on type
        "txn_status": random.choice(["Completed", "Pending", "Failed"])
    })
transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv('FactTransactions.csv', index=False)

# Continue for other dimensions and facts as needed...
# Generate DimDate (keeps original logic)
dates = []
for day in range(1, 366):  # Assuming a non-leap year
    date = faker.date_this_year()
    dates.append({
        "date_id": day,
        "date": date,
        "day": date.day,
        "month": date.month,
        "year": date.year,
        "quarter": (date.month - 1) // 3 + 1,
        "weekday": date.strftime("%A")
    })
dates_df = pd.DataFrame(dates)
dates_df.to_csv('DimDate.csv', index=False)

# Generate DimChannel (keeps original logic)
channels = [
    {"channel_id": 1, "channel_name": "Online"},
    {"channel_id": 2, "channel_name": "Mobile"},
    {"channel_id": 3, "channel_name": "Branch"},
    {"channel_id": 4, "channel_name": "ATM"},
    {"channel_id": 5, "channel_name": "Phone"}
]
channels_df = pd.DataFrame(channels)
channels_df.to_csv('DimChannel.csv', index=False)

# Generate DimLocation with more realistic locations
locations = []
for _ in range(num_records):
    locations.append({
        "location_id": _ + 1,
        "address": faker.street_address(),
        "city": faker.city(),
        "state": faker.state(),
        "country": faker.country(),
        "postal_code": faker.postcode()
    })
locations_df = pd.DataFrame(locations)
locations_df.to_csv('DimLocation.csv', index=False)

# Generate DimCurrency (keeps original logic)
currencies = [
    {"currency_id": 1, "name": "US Dollar", "iso3_code": "USD", "active": True},
    {"currency_id": 2, "name": "Euro", "iso3_code": "EUR", "active": True},
    {"currency_id": 3, "name": "British Pound", "iso3_code": "GBP", "active": True},
    {"currency_id": 4, "name": "Japanese Yen", "iso3_code": "JPY", "active": True},
    {"currency_id": 5, "name": "Canadian Dollar", "iso3_code": "CAD", "active": True},
    {"currency_id": 6, "name": "Australian Dollar", "iso3_code": "AUD", "active": True},
    {"currency_id": 7, "name": "Swiss Franc", "iso3_code": "CHF", "active": True},
    {"currency_id": 8, "name": "Chinese Yuan", "iso3_code": "CNY", "active": True},
    {"currency_id": 9, "name": "Indian Rupee", "iso3_code": "INR", "active": True},
    {"currency_id": 10, "name": "South Korean Won", "iso3_code": "KRW", "active": True}
]

currencies_df = pd.DataFrame(currencies)
currencies_df.to_csv('DimCurrency.csv', index=False)

# Generate DimInvestmentType with more specific investment types
investment_types = [
    {"investment_type_id": 1, "investment_type_name": "Stocks"},
    {"investment_type_id": 2, "investment_type_name": "Bonds"},
    {"investment_type_id": 3, "investment_type_name": "Mutual Funds"},
    {"investment_type_id": 4, "investment_type_name": "Cryptocurrency"},
    {"investment_type_id": 5, "investment_type_name": "Real Estate"},
    {"investment_type_id": 6, "investment_type_name": "Exchange-Traded Funds (ETFs)"},
    {"investment_type_id": 7, "investment_type_name": "Options"},
    {"investment_type_id": 8, "investment_type_name": "Commodities"},
    {"investment_type_id": 9, "investment_type_name": "Forex (Foreign Exchange)"},
    {"investment_type_id": 10, "investment_type_name": "Hedge Funds"},
    {"investment_type_id": 11, "investment_type_name": "Private Equity"},
    {"investment_type_id": 12, "investment_type_name": "Peer-to-Peer Lending"},
    {"investment_type_id": 13, "investment_type_name": "Collectibles (Art, Antiques, etc.)"},
    {"investment_type_id": 14, "investment_type_name": "Savings Accounts"},
    {"investment_type_id": 15, "investment_type_name": "Certificates of Deposit (CDs)"}
]

# for _ in range(num_records):
#     investment_types.append({
#         "investment_type_id": _ + 1,
#         "investment_type_name": random.choice(["Stocks", "Bonds", "Mutual Funds", "Real Estate", "Cryptocurrency"])
#     })

investment_types_df = pd.DataFrame(investment_types)
investment_types_df.to_csv('DimInvestmentType.csv', index=False)

# Generate FactTransactions with realistic loan and investment integration
transactions = []
for _ in range(num_records):
    txn_type_id = random.randint(1, len(transaction_types))
    transactions.append({
        "transaction_id": _ + 1,
        "customer_id": random.randint(1, num_records),
        "txn_date_id": random.randint(1, 365),
        "channel_id": random.randint(1, len(channels)),
        "account_id": random.randint(1, num_records),
        "txn_type_id": txn_type_id,
        "location_id": random.randint(1, num_records),
        "currency_id": random.randint(1, len(currencies)),
        "loan_id": random.randint(1, num_records) if random.choice([True, False]) else None,
        "investment_type_id": random.randint(1, len(investment_types)) if random.choice([True, False]) else None,
        "txn_amount": round(random.uniform(100, 500) if txn_type_id == 1 else random.uniform(10, 200), 2),
        "txn_status": random.choice(["Completed", "Pending", "Failed"])
    })
transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv('FactTransactions.csv', index=False)

# Generate FactDailyBalances with realistic balance changes
daily_balances = []
for _ in range(num_records):
    opening_balance = round(abs(random.gauss(2000, 1500)), 2)
    closing_balance = round(abs(random.gauss(2000, 1500)), 2)
    daily_balances.append({
        "balance_id": _ + 1,
        "date_id": random.randint(1, 365),
        "account_id": random.randint(1, num_records),
        "opening_balance": opening_balance,
        "closing_balance": closing_balance,
        "average_balance": round((opening_balance + closing_balance) / 2, 2)
    })
daily_balances_df = pd.DataFrame(daily_balances)
daily_balances_df.to_csv('FactDailyBalances.csv', index=False)

# Generate FactCustomerInteractions with realistic interaction types and ratings
customer_interactions = []
for _ in range(num_records):
    customer_interactions.append({
        "interaction_id": _ + 1,
        "date_id": random.randint(1, 365),
        "account_id": random.randint(1, num_records),
        "channel_id": random.randint(1, len(channels)),
        "interaction_type": random.choice(["Support Call", "ATM Transaction", "Online Query", "Branch Visit"]),
        "interaction_rating": random.randint(1, 5)
    })
customer_interactions_df = pd.DataFrame(customer_interactions)
customer_interactions_df.to_csv('FactCustomerInteractions.csv', index=False)

# Generate FactLoanPayments with realistic loan payment data
loan_payments = []
for _ in range(num_records):
    loan_payments.append({
        "payment_id": _ + 1,
        "date_id": random.randint(1, 365),
        "loan_id": random.randint(1, num_records),
        "customer_id": random.randint(1, num_records),
        "payment_amount": round(random.uniform(100, 1000), 2),
        "payment_status": random.choice(["Paid", "Pending"])
    })
loan_payments_df = pd.DataFrame(loan_payments)
loan_payments_df.to_csv('FactLoanPayments.csv', index=False)

# Generate FactInvestments with more realistic investment returns
investments = []
for _ in range(num_records):
    investment_type_id = random.randint(1, len(investment_types))
    investments.append({
        "investment_id": _ + 1,
        "date_id": random.randint(1, 365),
        "investment_type_id": investment_type_id,
        "account_id": random.randint(1, num_records),
        "amount_invested": round(random.uniform(100, 10000), 2),
        "investment_return": round(random.uniform(1, 1000), 2) if random.choice([True, False]) else None
    })
investments_df = pd.DataFrame(investments)
investments_df.to_csv('FactInvestments.csv', index=False)

print("Data generation complete! CSV files have been created.")
