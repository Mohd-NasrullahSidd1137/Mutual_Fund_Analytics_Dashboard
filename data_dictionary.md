# Mutual Fund Analytics - Data Dictionary

## Table: 01_fund_master

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | VARCHAR | Unique AMFI Scheme Code |
| fund_house | VARCHAR | Mutual Fund Company Name |
| scheme_name | VARCHAR | Mutual Fund Scheme Name |
| category | VARCHAR | Fund Category |
| sub_category | VARCHAR | Fund Sub Category |
| plan | VARCHAR | Regular / Direct Plan |
| launch_date | DATE | Scheme Launch Date |
| benchmark | VARCHAR | Benchmark Index |
| expense_ratio_pct | DECIMAL | Expense Ratio (%) |
| exit_load_pct | DECIMAL | Exit Load (%) |
| min_sip_amount | DECIMAL | Minimum SIP Amount |
| min_lumpsum_amount | DECIMAL | Minimum Lump Sum Amount |
| fund_manager | VARCHAR | Fund Manager Name |
| risk_category | VARCHAR | Risk Level |
| sebi_category_code | VARCHAR | SEBI Category Code |

---

# Table: 02_nav_history

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | VARCHAR | AMFI Scheme Code |
| date | DATE | NAV Date |
| nav | DECIMAL | Net Asset Value |

---

# Table: 03_aum_by_fund_house

| Column | Data Type | Description |
|---------|----------|-------------|
| date | DATE | Reporting Date |
| fund_house | VARCHAR | Fund House Name |
| aum_lakh_crore | DECIMAL | AUM in Lakh Crore |
| aum_crore | DECIMAL | AUM in Crore |
| num_schemes | INTEGER | Number of Schemes |

---

# Table: 04_monthly_sip_inflows

| Column | Data Type | Description |
|---------|----------|-------------|
| month | DATE | Month |
| sip_inflow_crore | DECIMAL | Monthly SIP Collection |
| active_sip_accounts_crore | DECIMAL | Active SIP Accounts |
| new_sip_accounts_lakh | DECIMAL | New SIP Accounts |
| sip_aum_lakh_crore | DECIMAL | SIP Assets Under Management |
| yoy_growth_pct | DECIMAL | Year-over-Year Growth |

---

# Table: 05_category_inflows

| Column | Data Type | Description |
|---------|----------|-------------|
| month | DATE | Month |
| category | VARCHAR | Fund Category |
| net_inflow_crore | DECIMAL | Net Monthly Inflow |

---

# Table: 06_industry_folio_count

| Column | Data Type | Description |
|---------|----------|-------------|
| month | DATE | Month |
| total_folios_crore | DECIMAL | Total Folios |
| equity_folios_crore | DECIMAL | Equity Folios |
| debt_folios_crore | DECIMAL | Debt Folios |
| hybrid_folios_crore | DECIMAL | Hybrid Folios |
| others_folios_crore | DECIMAL | Other Category Folios |

---

# Table: 07_scheme_performance

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | VARCHAR | AMFI Scheme Code |
| scheme_name | VARCHAR | Scheme Name |
| fund_house | VARCHAR | Fund House |
| category | VARCHAR | Fund Category |
| plan | VARCHAR | Plan Type |
| return_1yr_pct | DECIMAL | 1 Year Return |
| return_3yr_pct | DECIMAL | 3 Year Return |
| return_5yr_pct | DECIMAL | 5 Year Return |
| benchmark_3yr_pct | DECIMAL | Benchmark Return |
| alpha | DECIMAL | Alpha |
| beta | DECIMAL | Beta |
| sharpe_ratio | DECIMAL | Sharpe Ratio |
| sortino_ratio | DECIMAL | Sortino Ratio |
| std_dev_ann_pct | DECIMAL | Annual Standard Deviation |
| max_drawdown_pct | DECIMAL | Maximum Drawdown |
| aum_crore | DECIMAL | Assets Under Management |
| expense_ratio_pct | DECIMAL | Expense Ratio |
| morningstar_rating | INTEGER | Morningstar Rating |
| risk_grade | VARCHAR | Risk Grade |

---

# Table: 08_investor_transactions

| Column | Data Type | Description |
|---------|----------|-------------|
| investor_id | VARCHAR | Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | VARCHAR | AMFI Scheme Code |
| transaction_type | VARCHAR | SIP / Lumpsum / Redemption |
| amount_inr | DECIMAL | Transaction Amount |
| state | VARCHAR | Investor State |
| city | VARCHAR | Investor City |
| city_tier | VARCHAR | T30 / B30 Classification |
| age_group | VARCHAR | Investor Age Group |
| gender | VARCHAR | Investor Gender |
| annual_income_lakh | DECIMAL | Annual Income |
| payment_mode | VARCHAR | Payment Method |
| kyc_status | VARCHAR | KYC Verification Status |

---

# Table: 09_portfolio_holdings

| Column | Data Type | Description |
|---------|----------|-------------|
| amfi_code | VARCHAR | AMFI Scheme Code |
| stock_symbol | VARCHAR | Stock Symbol |
| stock_name | VARCHAR | Company Name |
| sector | VARCHAR | Industry Sector |
| weight_pct | DECIMAL | Portfolio Weight (%) |
| market_value_cr | DECIMAL | Market Value |
| current_price_inr | DECIMAL | Current Stock Price |
| portfolio_date | DATE | Portfolio Reporting Date |

---

# Table: 10_benchmark_indices

| Column | Data Type | Description |
|---------|----------|-------------|
| date | DATE | Index Date |
| index_name | VARCHAR | Benchmark Name |
| close_value | DECIMAL | Closing Index Value |