# Mutual Fund ESG and Unethical Involvement Analysis

An end-to-end data analytics project investigating the relationship between management fees, ESG ratings, and market resilience across European ETFs during the 2020 market crisis. Developed for **Banca Generali** evaluation.

---

## 📌 Executive Summary
This project aims to answer two critical strategic questions for the financial network:
1. **The ESG Pricing Paradox:** Do higher ESG scores entail higher management fees?
2. **The Ethical Shield:** Does exposure to unethical sectors translate to better fund performance?

---

## 📉 Key Findings

* **Debunking the "ESG Premium":** There is a remarkably weak mathematical correlation between fund fees and sustainability scores across all three pillars (Environmental, Social, and Governance). Asset managers do not price ESG as a luxury good.

**Statistical Correlation Output (Python):**
```text
management_fees        1.000000
environmental_score    0.115465
social_score           0.044917
governance_score       0.021009


* **The Volatility Paradox:** Absolute exclusion strategies (Pure 0% with no unethical exposure) provide excellent capital protection during a market crash (Q1 2020 Return: `-2.3%`) but introduce extreme unpredictability (Std Dev: `17.5`) due to sector concentration.
* **The Investment "Sweet Spot":** A **Low-Tolerance Framework (<10%)** represents the optimal choice, slashing portfolio volatility by nearly two-thirds while fully capturing market upside during recoveries.

merit_class          | Q4 2019 Mean (Std) | Q1 2020 Mean (Std)  | Q2 2020 Mean (Std) | Q3 2020 Mean (Std)
----------------------+--------------------+---------------------+--------------------+--------------------
 1. Pure (0%)         |  -2.75%  (8.79)    |  -2.15%  (41.34)    |  +6.30%  (18.18)   |  +0.88%  (17.54)
 2. Low (<10%)        |  -0.40%  (5.15)    | -13.54%  (14.63)    | +13.96%   (9.00)   |  +0.97%   (5.86)
 3. Moderate (10-20%) |  +0.49%  (4.79)    | -14.30%  (11.53)    | +14.91%   (7.59)   |  +2.30%   (6.05)
 4. High (20-35%)     |  +0.13%  (3.15)    | -14.22%   (9.71)    | +15.04%   (6.09)   |  +2.16%   (4.97)
 5. Very High (>25%)  |  +0.77%  (3.54)    | -15.44%  (10.70)    | +15.76%   (6.15)   |  +1.77%   (4.57)


TOP 5 PERFORMING FUNDS (Q4 2020):
                                               fund_name  fund_return_2020_q3  total_unethical_exposure
8964        GraniteShares 3x Short Rolls-Royce Daily ETC               403.82                       0.0
8948                 GraniteShares 3x Short BP Daily ETC                97.25                       0.0
8962  GraniteShares 3x Short Royal Dutch Shell Daily ETC                94.92                       0.0
2900                WisdomTree Silver 3x Daily Leveraged                54.33                       0.0
319                 WisdomTree Silver 2x Daily Leveraged                44.07                       0.0


TOP 5 HIGHEST UNETHICAL EXPOSURE:
                                                               fund_name  total_unethical_exposure  fund_return_2020_q3
3764                             SPDR® MSCI Europe Health Care UCITS ETF                    183.09                -2.57
12                   iShares STOXX Europe 600 Health Care UCITS ETF (DE)                    174.27                -2.43
232             Xtrackers Stoxx Europe 600 Health Care Swap UCITS ETF 1C                    174.26                -2.24
7903  Lyxor Index Fund - Lyxor Stoxx Europe 600 Healthcare UCITS ETF Acc                    174.26                -2.33
790             Invesco STOXX Europe 600 Optimised Health Care UCITS ETF                    168.27                -1.98
---

## 🛠️ Tech Stack & Architecture

* **Extract & Clean (Python/Pandas):** Automated data cleaning, schema formatting, and structural checks (ensuring asset allocations equaled 100%).
* **Storage & Relational Mapping (PostgreSQL):** Built an automated ETL pipeline to push and replace cleaned data tables to a local PostgreSQL server using SQLAlchemy.
* **Advanced Analytics (Python):** Merged fragmented datasets, executed Pearson correlation matrix analyses, and dynamically segmented portfolios into 5 Ethical Merit Classes.
* **Data Visualization (Power BI):** Created dynamic scatter plots with statistical trendlines, and customized line/column charts to explore ESG fees and track risk-adjusted performance across the 2020 crash, rebound, and stabilization phases.
