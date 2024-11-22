---***************Transaction ***************-----
   --&-- Transaction Volume &Total Transaction Amount by month
		SELECT DATEPART(month,txn_date_id)as 'Month', COUNT(transaction_id) as 'count_txn',
		SUM(txn_ammount)as'txn_Amount', AVG(txn_ammount)as'avg_txn_amount'
		FROM FactTransactions 
		GROUP BY DATEPART(month, txn_date_id)
		ORDER BY DATEPART(month, txn_date_id)  asc
   --&-- num of tranction  for each type 
		SELECT t.description, COUNT(f.transaction_id)
		FROM FactTransactions f
		JOIN DimTransactionType t ON f.txn_type_id= t.transaction_type_id
		GROUP BY t.description;
   --&-- Top Customers by Transaction
		SELECT top(10) c.customer_id, SUM(f.txn_ammount) AS total_amount
		FROM FactTransactions f
		JOIN DimCustomers c ON f.customer_id = c.customer_id
		GROUP BY c.customer_id
		ORDER BY total_amount DESC
 
		
---***************Loan***************-----
  --&--Loan Analysis by Loan Type
		SELECT l.loan_type, COUNT(f.loan_id) AS number_of_loans, SUM(f.payment_ammount) AS total_loan_amount
		FROM DimLoan l
		JOIN FactLoanPayments f ON l.loan_id = f.loan_id
		GROUP BY l.loan_type;

 --&--pending Loans Analysis
		SELECT loan_id, customer_id, payment_ammount, payment_status
		FROM FactLoanPayments
        WHERE payment_status = 'Pending';

---***************Investment ***************-----
  --&--Investment by Type and amount
		SELECT it.investment_type_name, COUNT(f.investment_id) AS number_of_investments, 
		SUM(f.amount_invested) AS total_invested
		FROM DimInvestmentType it
		JOIN FactInvestments f ON it.investment_type_id = f.investment_type_id
		GROUP BY it.investment_type_name;
  --&--Investment Performance Over Time
		SELECT d.FiscalYear, d.FiscalMonth, 
       SUM(f.investment_return) AS total_investment_return
		FROM FactInvestments f
		JOIN DimDate d ON f.date_id = d.Id
		GROUP BY d.FiscalYear, d.FiscalMonth
		ORDER BY d.FiscalYear, d.FiscalMonth asc;

   --&--Investment Risk Analysis
		SELECT top(50) investment_type_id, account_id, 
		(amount_invested - investment_return) / amount_invested AS risk_factor
		FROM FactInvestments f
		WHERE investment_return < amount_invested;

---***************Currancy ***************-----           ->>> miss in data
  --&--Currancy and avg balance
		SELECT currency_id, is3_code, AVG(closing_balance) AS avg_closing_balance
		FROM Dimcurrency
		JOIN FactDailyBalances ON Dimcurrency.currency_id = FactDailyBalances.Balance_id
		GROUP BY currency_id, is3_code;

---***************Channel***************-----
  --&--Number of transaction roe Each Channel
        SELECT ch.channel_name, COUNT(f.transaction_id) as 'Num Of Transaction'
		FROM FactTransactions f
		JOIN DimChannel ch ON f.channel_id = ch.channel_id
		GROUP BY ch.channel_name;
----(Customer Satisfaction by Channel)
		SELECT c.channel_name, AVG(f.interaction_rating) AS average_rating
		FROM DimChannel c
		JOIN FactCustomerInteractions f ON c.channel_id = f.channel_id
		GROUP BY c.channel_name;
----- (Channel Performance Over Year)
		SELECT d.FiscalYear, c.channel_name, COUNT(f.interaction_type) AS number_of_interactions
		FROM DimChannel c
		JOIN FactCustomerInteractions f ON c.channel_id = f.channel_id
		JOIN DimDate d ON f.date_id = d.Id
		GROUP BY d.FiscalYear, c.channel_name
		ORDER BY d.FiscalYear  asc

---***************Account Balance ***************-----
--&--Average daily Balance
        SELECT account_id, AVG(average_balance) AS avg_daily_balance
		FROM FactDailyBalances
		GROUP BY account_id
		order by AVG(average_balance)
--&--Balance Analysis by Account Type
	    SELECT acc.account_type, SUM(fdb.closing_balance) AS total_closing_balance
		FROM DimAccount acc
		JOIN FactDailyBalances fdb ON acc.account_id = fdb.account_id
		GROUP BY acc.account_type;
		

   

		


