# Interview Notes — Canadian Energy Majors Valuation Project

These notes are designed to help explain the project in an interview or networking conversation. They are talking points, not a script that needs to be memorized word-for-word.

## 1. Title / framing

> I built this project to teach myself the workflow of a junior finance / equity-research analyst — pulling real data, building a valuation model from raw inputs, testing an investment question, and defending the conclusion. I chose Canadian energy majors because the sector is highly relevant to Calgary and gives me a good mix of company fundamentals and commodity exposure.

## 2. Methodology

> I split the workflow into two parts. Python handles the data collection: I used yfinance and pandas to pull financial statement data, daily prices for four Canadian energy companies, and WTI crude data. I then exported the data into Excel, where I built the valuation and trend analysis from the underlying inputs rather than relying on pre-calculated multiples.

## 3. Finding 1 — Comps valuation

> I calculated each company's EV/EBITDA multiple for 2022 through 2025 and used the average multiple across those years to reduce dependence on any single year. The peer average for CVE, SU, and IMO was 4.72x. Applying that benchmark to CNQ's average EBITDA produced a peer-multiple implied share value of about $35.70 versus a 2025 year-end price of $45.18.

> I would not describe $35.70 as definitive intrinsic fair value. I use it as a historical peer-multiple benchmark showing that CNQ traded at a meaningful premium to the peer group.

## 4. Finding 2 — Price vs. fundamentals divergence

> I indexed both EBITDA and stock price to 2022 = 100 and tracked the two series through 2025. All four companies showed stock prices outperforming their own EBITDA trend to some degree, but the gap was very different by company. CVE had the tightest 2025 gap at about 24 points, while IMO had the widest at about 77 points.

## 5. Finding 3 — 2026 WTI trend break

> I fitted a simple linear trend to annual average WTI prices from 2022 through 2025. That trend projected about $55 per barrel for 2026. In the dataset, the 2026 average through September 22 was about $83, roughly 50% above the historical trend projection.

> The important point is that this shows a measurable break from the prior trend. The model does not by itself prove the exact cause of that change, so I treat it as a macro regime shift rather than claiming the regression identified a specific causal mechanism.

## 6. Oil sensitivity

> I estimated each company's historical sensitivity to WTI using daily data and reported both an oil beta and R². IMO had the largest estimated dollar stock move per $1 of WTI at about $0.38, but its R² was only 0.27. That suggests oil matters, but a large share of daily stock movements is driven by other factors as well.

## 7. Conclusion

> Putting the pieces together, the analysis suggests CNQ was trading at a meaningful premium to its peers on a historical multiple basis, while the 2026 oil-price regime shift helps explain why sector share prices were stronger than a trailing-fundamentals view alone would suggest. The project was as much about learning to make and defend an analytical judgment as it was about calculating the numbers.

---

# Anticipated interview questions

## Why EV/EBITDA instead of P/E?

EV/EBITDA is useful for comparing companies with different capital structures because enterprise value incorporates both equity and net debt, while EBITDA focuses on operating earnings before interest. For this peer group, I wanted a multiple that was less dependent on differences in financing structure.

## Why average the multiple over four years?

Energy companies are cyclical and commodity prices can make a single year's multiple unusually high or low. I used a four-year average to reduce the influence of one specific year. I treat the result as a historical benchmark rather than a forward market multiple.

## Why use a linear forecast with only four data points?

That is one of the main limitations of the project. The model is intentionally simple and is best interpreted as a trend benchmark. With more time, I would use a longer historical series and a more robust forecasting framework.

## Are you claiming CNQ was actually 26.5% overvalued?

No. The 26.5% figure is the gap between CNQ's observed price and the peer-multiple implied value under my historical-average assumptions. A premium can be justified by forward growth, asset quality, acquisitions, balance-sheet differences, or other expectations that a simple historical comps model does not capture.

## Is the 2026 oil move proof of a supply shock?

No. It demonstrates that 2026 WTI prices were materially above the prior 2022–2025 trend. The regression itself does not establish causality, so I would describe it as a significant break from the previous trend and then use broader macro evidence to discuss possible explanations.

## What would you build next?

A DCF would be the most useful next step because it would provide an independent intrinsic-value framework to cross-check the comps conclusion. I would also build a more robust oil-sensitivity regression that controls for broad market or sector returns.
