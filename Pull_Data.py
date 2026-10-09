import yfinance as yf
import pandas as pd

# Tickers
tickers = {
    "CNQ": "CNQ.TO",
    "CVE": "CVE.TO",
    "SU": "SU.TO",
    "IMO": "IMO.TO",
}

# 1. Income Statement Metrics
income_metrics = [
    "Total Revenue", "EBITDA", "EBIT", "Net Income", 
    "Diluted EPS", "Pretax Income", "Tax Provision"
]

results = []

for name, symbol in tickers.items():
    ticker_obj = yf.Ticker(symbol)
    financials = ticker_obj.financials

    for metric in income_metrics:
        for year in financials.columns:
            value = financials.loc[metric, year]
            results.append({
                "Company": name,
                "Year": year.year,
                "Metric": metric,
                "Value": value,
            })

df = pd.DataFrame(results)
df = df[df["Year"] != 2021]

# 2. Cash Flow Statement Metrics
cashflow_metrics = [
    "Free Cash Flow", "Operating Cash Flow", "Capital Expenditure", 
    "Cash Dividends Paid", "Repurchase Of Capital Stock"
]

results2 = []

for name, symbol in tickers.items():
    ticker_obj = yf.Ticker(symbol)
    cashflow = ticker_obj.cashflow

    for metric in cashflow_metrics:
        for year in cashflow.columns:
            value = cashflow.loc[metric, year]
            results2.append({
                "Company": name,
                "Year": year.year,
                "Metric": metric,
                "Value": value,
            })

df2 = pd.DataFrame(results2)
df2 = df2[df2["Year"] != 2021]

# 3. Balance Sheet Metrics
balance_sheet_metrics = [
    "Total Debt", "Cash And Cash Equivalents", "Ordinary Shares Number"
]

results4 = []

for name, symbol in tickers.items():
    ticker_obj = yf.Ticker(symbol)
    balance_sheet = ticker_obj.balance_sheet

    for metric in balance_sheet_metrics:
        for year in balance_sheet.columns:
            value = balance_sheet.loc[metric, year]
            results4.append({
                "Company": name,
                "Year": year.year,
                "Metric": metric,
                "Value": value,
            })

df3 = pd.DataFrame(results4)
df3 = df3[df3["Year"] != 2021]

# Combine Statement Data
combined_df = pd.concat([df, df2, df3])

# 4. Stock Price History
results3 = []

for name, symbol in tickers.items():
    ticker_obj = yf.Ticker(symbol)
    price_history = ticker_obj.history(start="2022-01-01")

    for date, row in price_history.iterrows():
        results3.append({
            "Company": name,
            "Date": date,
            "Close": row["Close"],
        })

price_df = pd.DataFrame(results3)
price_df["Date"] = price_df["Date"].dt.tz_localize(None)

price_df_baseline = price_df[price_df["Date"].dt.year <= 2025]
price_df_2026 = price_df[price_df["Date"].dt.year == 2026]

# Year-End Prices
year_end_prices = price_df.copy()
year_end_prices["Year"] = year_end_prices["Date"].dt.year
year_end_prices = year_end_prices.sort_values("Date")
year_end_prices = year_end_prices.groupby(["Company", "Year"]).tail(1)
year_end_prices = year_end_prices[["Company", "Year", "Close"]]

# 5. Oil Price History (WTI Crude)
oil_ticker = yf.Ticker("CL=F")
oil_history = oil_ticker.history(start="2022-01-01")

oil_results = []

for date, row in oil_history.iterrows():
    oil_results.append({
        "Date": date,
        "Close": row["Close"],
    })

oil_price_df = pd.DataFrame(oil_results)
oil_price_df["Date"] = oil_price_df["Date"].dt.tz_localize(None)

# 6. Export to Excel (Saves in Current Project Directory)
output_file = "energy_sector_valuation_data12.xlsx"

with pd.ExcelWriter(output_file) as writer:
    combined_df.to_excel(writer, sheet_name="Fundamentals", index=False)
    price_df.to_excel(writer, sheet_name="Prices_All", index=False)
    price_df_baseline.to_excel(writer, sheet_name="Prices_2022-2025", index=False)
    price_df_2026.to_excel(writer, sheet_name="Prices_2026", index=False)
    year_end_prices.to_excel(writer, sheet_name="Year_End_Prices", index=False)
    oil_price_df.to_excel(writer, sheet_name="Oil_Price", index=False)

print(f"Done — exported to {output_file}")



