# Canadian Energy Majors: Relative Valuation & Macro Divergence Analysis

**Independent equity research project | Python + Excel | 2026**

An independent analysis of **Canadian Natural Resources (CNQ)** against three Canadian energy peers — **Cenovus (CVE), Suncor (SU), and Imperial Oil (IMO)** — using historical trading comps, price-vs-fundamentals analysis, and WTI crude sensitivity.

The project was built to practice the workflow of a junior finance / equity-research analyst: **pull data -> build a model from raw inputs -> test an investment question -> defend the conclusion and its limitations.**

## Investment question

**Is CNQ's valuation premium versus comparable Canadian energy companies supported by its historical fundamentals and the 2026 commodity-price environment?**

## Key findings

1. **Relative valuation:** CNQ's 2022–2025 average EV/EBITDA multiple was **5.21x**, versus **4.72x** for the peer average (CVE, SU, IMO). Applying the peer benchmark to CNQ's average EBITDA produced a **peer-multiple implied share value of $35.70**, versus a 2025 year-end price of **$45.18** — a premium of approximately **26.5%**.
2. **Price vs. fundamentals:** Indexing EBITDA and stock price to **2022 = 100** shows stock prices outpaced EBITDA across all four companies to different degrees. The 2025 gap ranked **CVE (24.4 points), CNQ (42.4), SU (52.9), IMO (77.4)**.
3. **WTI trend break:** A linear trend fitted to 2022–2025 annual average WTI prices projected approximately **$55/bbl** for 2026. The dataset's 2026 WTI average through **September 22, 2026** was approximately **$83/bbl**, roughly **50% above the historical trend projection**.
4. **Oil sensitivity:** Regression using daily stock and WTI data estimates different company-level sensitivities. IMO had the largest estimated dollar stock move per $1 change in WTI (**$0.38**) but the lowest R² (**0.27**), suggesting a meaningful amount of its daily price variation is explained by factors beyond WTI alone.

## Methodology

### Python data pipeline

`Pull_Data.py` uses `yfinance` and `pandas` to collect:

- Income statement metrics
- Cash flow metrics
- Balance sheet metrics
- Daily stock prices for CNQ, CVE, SU, and IMO
- Daily WTI crude oil prices (`CL=F`)

The pipeline reshapes statement data into a long-format structure and exports a raw-data workbook for analysis.

### Excel valuation and analysis

The committed Excel model contains dedicated analysis sheets for:

- **Comps_Analysis** — market capitalization, enterprise value, EV/EBITDA, peer averages, and CNQ implied value
- **Price_vs_Fundamentals** — revenue/EBITDA growth and indexed price-vs-EBITDA analysis
- **Oil_Macro_Analysis** — WTI trend forecast, actual-vs-projected 2026 comparison, and stock sensitivity to oil
- **Fundamentals / Prices / Oil_Price** — underlying datasets exported from the Python pipeline

EV is built from raw inputs rather than importing a pre-calculated multiple. The project uses the historical peer average as a **benchmark**, not as a claim of intrinsic value.

## Tools

- **Python:** `yfinance`, `pandas`
- **Excel:** financial modeling, `AVERAGEIFS`, `FORECAST.LINEAR`, regression / sensitivity analysis
- **Finance:** EV/EBITDA trading comps, financial statement analysis, commodity sensitivity
- **Statistics:** beta and R² analysis

## Limitations

This is an independent student research project and the conclusions are deliberately presented with caveats:

- The WTI forecast is based on only **four annual observations (2022–2025)**, so it is a simple trend benchmark rather than a robust forecasting model.
- The 2026 WTI figure is a **partial-year average through September 22, 2026**, not a full-year realized average.
- The comps valuation uses historical averages to test relative positioning. A valuation premium can reflect mispricing, different forward expectations, asset quality, or other company-specific factors.
- The daily oil-sensitivity analysis identifies historical relationships, not causality.

## What I would build next

A natural next step would be a **DCF as an independent cross-check** on the comps conclusion, followed by a more robust regression that controls for broader market or sector returns when estimating oil sensitivity.

## Repository structure

```text
├── README.md
├── Pull_Data.py
├── energy_sector_valuation_MASTER.xlsx
├── CNQ_Energy_Valuation_Deck.pdf
├── Interview_Notes.md
├── requirements.txt
└── .gitignore
```

## How to run the Python pipeline

1. Install Python 3.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run:

```bash
python Pull_Data.py
```

The script creates a raw-data Excel export named `energy_sector_valuation_data12.xlsx`. The committed `energy_sector_valuation_MASTER.xlsx` contains the analysis/model sheets built from the exported data.

## Author

**Gavin Bansi**  
Final-year Economics student, University of Calgary
