import pandas as pd

# Load the Excel file
file_path = 'systematic review data from scopus Pubmed and safetylit before abstract screening.xlsx'

# Specify the sheet name (or index, e.g., sheet_name=0)
df = pd.read_excel(file_path, sheet_name='merged data')

# Drop duplicate rows (based on all columns)
df_deduped = df.drop_duplicates()

# OR: drop duplicates based on specific columns
# df_deduped = df.drop_duplicates(subset=['DOI', 'Title'])

# Save the cleaned data to a new Excel file
df_deduped.to_excel('deduplicated_output.xlsx', index=False)

print("Deduplicated data saved as 'deduplicated_output.xlsx'")
