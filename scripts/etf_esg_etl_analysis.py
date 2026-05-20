import pandas as pd
from sqlalchemy import create_engine
import os


#==========================================================================
# 1.LOADING DATASETS - European Funds dataset from Morningstar
#==========================================================================

df_overview = pd.read_csv("European ETFs - Fund Overview.csv")
df_financials = pd.read_csv("European ETFs - Financials.csv")
df_esg = pd.read_csv("European ETFs - ESG.csv")

#==========================================================================
# 2. DATASET INVESTIGATION
#==========================================================================


# Upon inspection we can establish that ticker can be used as Primary Keys (fund_name and isin have duplicate values as a fund might be listed in multiple markets witht the same name and isin))
# Data is well fragmented with many Null values (e.g. modified_duration shows only 285 entries)
#print(df_overview.info())
#print(df_financials.info())
#print(df_esg.info())


#==========================================================================
# 3. POSTGRESQL CONNECTION
#==========================================================================

engine = create_engine("postgresql://postgres:PASSWORD@localhost:5432/Financial%20Institution%20Analysis")

files = {
    'etf_overview': r'C:\Users\kevin\PycharmProjects\ProjectAlpha\Financial Institution Analysis\European ETFs - Fund Overview.csv',
    'etf_financials': r'C:\Users\kevin\PycharmProjects\ProjectAlpha\Financial Institution Analysis\European ETFs - Financials.csv',
    'etf_esg': r'C:\Users\kevin\PycharmProjects\ProjectAlpha\Financial Institution Analysis\European ETFs - ESG.csv'
}

print("Starting the engine...\n ")

for table_name, file_path in files.items():
    if os.path.exists(file_path):
        print(f"Reading {file_path}...\n")

        # Load data
        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = [c.lower().replace(' ', '_').replace('-', '_') for c in df.columns]

        # Clean Data before upload
        if 'nav_per_share' in df.columns:
            df = df.drop(columns=['nav_per_share'])
        if 'price_book_ratio' in df.columns:
            df = df.drop(columns=['price_book_ratio'])

        #Create new column that sums the Assets Classes (shares, bonds and cash), then verify if equal to 100 (or close by)
        count_invalid = 0

        if 'asset_stock' in df.columns:
            df["total_assets"] = df["asset_stock"] + df["asset_bond"] + df["asset_cash"]
            #Establish a count of values that do not fall between 99& and 101%
            outliers = df[~df["total_assets"].between(99,101)]
            count_invalid = len(outliers)

        if count_invalid > 0:
            print(f"There are a toal of {count_invalid} rows that do not sum to 100% in {table_name} \n")

        # Upload to SQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"Success! Table '{table_name}' is live with {len(df)} rows.")
    else:
        print(f"File not found: {file_path}")

print("\nAll done. Check pgAdmin. \n \n")

#==========================================================================
# 4. MASTER TABLE
#==========================================================================

#Merging on ticker (PK). First merge overview with financials, then add esg
df_master = pd.merge(df_overview, df_financials, on='ticker', how='inner')
df_master = pd.merge(df_master, df_esg, on='ticker', how='inner')

#==========================================================================
#5. CORRELATION AND PERFORMANCE ANALYSIS
#==========================================================================

#Remove duplicates to avoid data pollution. The same investment fund might be traded amongst different stock exchanges.
df_master_unique = df_master.drop_duplicates(subset=['fund_name']).copy()

# 5a) Question: Do higher fees reflect stronger ESG score?
print("CORRELATION - ESG scores and management fees:")

#Filter out rows with Nan values to avoi polluting the correlation matrix
mask = (df_master_unique["environmental_score"] > 0) & \
       (df_master_unique["social_score"] > 0) & \
       (df_master_unique["governance_score"] > 0) & \
       (df_master_unique["management_fees"] > 0)

df_clean_analysis = df_master_unique[mask]

cols_for_corr = ["management_fees", "environmental_score", "social_score", "governance_score"]
corr_matrix = df_clean_analysis[cols_for_corr].corr()
print(corr_matrix["management_fees"])

#5b) Question: Does involvement in unethical sectors translates to stronger fund performance?

print("\nRETURN - Performance of funds invested in unethical involvement:")

involvement_cols = ["involvement_abortive_contraceptive", "involvement_alcohol", "involvement_animal_testing",
    "involvement_controversial_weapons", "involvement_gambling", "involvement_gmo",
    "involvement_military_contracting", "involvement_nuclear", "involvement_palm_oil",
    "involvement_pesticides", "involvement_small_arms", "involvement_thermal_coal", "involvement_tobacco"]

return_cols = ["fund_return_2019_q4","fund_return_2020_q1", "fund_return_2020_q2", "fund_return_2020_q3"]

#Magnitude of funds exposed to controversial sectors
df_master_unique["total_unethical_exposure"] = df_master_unique[involvement_cols].sum(axis=1)

#Function to classifying mutual funds based on their exposure
def assign_merit(exposure):
    if exposure == 0: return "1.Pure (0%)"
    if exposure <10: return "2.Low (<10%)"
    if exposure <= 20: return "3.Moderate (10-20%)"
    if exposure <= 35: return "4.High (20-35%)"
    return "5.Very High (>25%)"

df_master_unique['merit_class'] = df_master_unique['total_unethical_exposure'].apply(assign_merit)

performance_merit = df_master_unique.groupby("merit_class")[return_cols].agg(["count", "mean", "std"])

print(performance_merit.to_string())

#==========================================================================
#6. LEADERBOARD AT THE FUND-LEVEL
#==========================================================================


# The top 5 funds by return in Q3 2020
top_performers = df_master_unique.nlargest(5, 'fund_return_2020_q3')[['fund_name', 'fund_return_2020_q3', 'total_unethical_exposure']]
print("\nTOP 5 PERFORMING FUNDS (Q4 2020):")
print(top_performers.to_string())

# The top 5 funds with the most unethical involvement
top_unethical = df_master_unique.nlargest(5, 'total_unethical_exposure')[['fund_name', 'total_unethical_exposure', 'fund_return_2020_q3']]
print("\nTOP 5 HIGHEST UNETHICAL EXPOSURE:")
print(top_unethical.to_string())

#==========================================================================
#7. EXPORT CSV FOR POWER BI DATA-VIZ
#==========================================================================

df_master_unique.to_csv("PBI - Master_Financial_ESG Analysis.csv", index=False)
