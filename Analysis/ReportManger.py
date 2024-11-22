import pandas as pd
from sqlalchemy import create_engine

#  connection string using SQLAlchemy
DRIVER_NAME = 'SQL Server'
SERVER_NAME = r'YaraMohamed\SQLEXPRESS09'
DATABASE_NAME = 'Bankfinal'

connection_string = f'mssql+pyodbc://{SERVER_NAME}/{DATABASE_NAME}?trusted_connection=yes&driver={DRIVER_NAME}'

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Read SQL queries using SQLAlchemy engine
df_customers = pd.read_sql_query('''SELECT customer_id, first_name+' '+last_name as 'Full name',occupation, city, state, postal_code, phone_number 
FROM DimCustomers;''', engine)
df_accounts = pd.read_sql_query('''SELECT cust.first_name+' '+cust.last_name as 'Full Name', account_number, acc.customer_id, acc.account_balance, acc.credit_score
FROM DimAccount acc
JOIN DimCustomers cust ON acc.customer_id = cust.customer_id

''', engine)
df_loans = pd.read_sql_query('''SELECT c.first_name+' '+c.last_name as 'Full name', loan.loan_id, loan.loan_type, loan.loan_amout
FROM DimLoan loan
 JOIN FactTransactions f  ON loan.loan_id= f.loan_id
 join DimCustomers c on c.customer_id=f.customer_id ;''', engine)
df_transactions = pd.read_sql_query('''SELECT cust.first_name+' '+cust.last_name as 'Full Name',trans.transaction_id, trans.txn_ammount, date.date, trans.txn_status
FROM FactTransactions trans
JOIN DimDate date ON trans.txn_date_id = date.Id 
join DimCustomers cust on cust.customer_id=trans.customer_id
order by date desc;
''', engine)

# Create an Excel file to save the results
with pd.ExcelWriter('bank_report.xlsx') as writer:
    df_customers.to_excel(writer, sheet_name='Customers')
    df_accounts.to_excel(writer, sheet_name='Accounts')
    df_loans.to_excel(writer, sheet_name='Loans')
    df_transactions.to_excel(writer, sheet_name='Transactions')
