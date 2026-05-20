# Mutual-Fund-ESG-and-Unethical-Involvement-Analysis

📌 **Executive Summary
This project aims to answer 2 strategic questions for the financial network:
    - Do higher ESG scores entail higher management fees?
    - Does exposure to unethical sectores translate to better fund performance? **
---

📉 Key Findings**
There is a remarkably weak mathematical correlation between fund fees and sustainability scores across all three pillars (Environmental, Social and Governance). Asset managers do not price ESG as a luxury good.
Absolute exclusion strategies (Pure 0% with no unethical exposure) provide excellent capital protection during a market crash (Q1 2020 Return: `-2.3%`) but introduce extreme unpredictability (Std Dev: `17.5`) due to sector concentration.
**---

🛠️ Tech Stack & Architecture
*** Extract & Clean (Python/Pandas): Automated data cleaning, schema formatting, and structural checks (ensuring asset allocations equaled 100%).
* Storage & Relational Mapping (PostgreSQL) Built an automated ETL pipeline to push cleaned data tables to a local PostgreSQL server.
* Advanced Analytics (Python): Merged fragmented datasets, executed Pearson correlation matrix analyses, and dynamically segmented portfolios into 5 Ethical Merit Classes.
* Data Visualization (Power BI): Created dynamic scatter plots with statistical trendlines, and customized line/column charts toexplore ESG fees and track performance across the 2020 crash.
**---
