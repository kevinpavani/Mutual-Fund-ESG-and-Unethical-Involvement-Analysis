# Mutual-Fund-ESG-and-Unethical-Involvement-Analysis
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
* **The Volatility Paradox:** Absolute exclusion strategies (Pure 0% with no unethical exposure) provide excellent capital protection during a market crash (Q1 2020 Return: `-2.3%`) but introduce extreme unpredictability (Std Dev: `17.5`) due to sector concentration.
* **The Investment "Sweet Spot":** A **Low-Tolerance Framework (<10%)** represents the optimal choice, slashing portfolio volatility by nearly two-thirds while fully capturing market upside during recoveries.

---

## 🛠️ Tech Stack & Architecture

* **Extract & Clean (Python/Pandas):** Automated data cleaning, schema formatting, and structural checks (ensuring asset allocations equaled 100%).
* **Storage & Relational Mapping (PostgreSQL):** Built an automated ETL pipeline to push and replace cleaned data tables to a local PostgreSQL server using SQLAlchemy.
* **Advanced Analytics (Python):** Merged fragmented datasets, executed Pearson correlation matrix analyses, and dynamically segmented portfolios into 5 Ethical Merit Classes.
* **Data Visualization (Power BI):** Created dynamic scatter plots with statistical trendlines, and customized line/column charts to explore ESG fees and track risk-adjusted performance across the 2020 crash, rebound, and stabilization phases.
