import pandas as pd

# Load your Excel file
df = pd.read_excel('/Users/srividhyaanand/Documents/systematic review f rta/systematic review data from scopus Pubmed and safetylit before abstract screening.xlsx', sheet_name='merged data')

# Define inclusion logic function
def should_include(title, abstract):
    text = f"{title} {abstract}".lower()

    # Inclusion conditions
    mentions_india = 'india' in text
    mentions_rta = any(term in text for term in [
        'road traffic accident', 'rta', 'traffic injury', 'road accident', 'road crash', 'traffic crash'
    ])
    mentions_epi = any(term in text for term in [
        'epidemiolog', 'incidence', 'prevalence', 'cross-sectional', 'retrospective', 'prospective', 'descriptive study'
    ])

    if mentions_india and mentions_rta and mentions_epi:
        return 'Include'
    else:
        return 'Exclude'

# Apply function to dataframe
df['Include/Exclude'] = df.apply(
    lambda row: should_include(str(row.get('Title', '')), str(row.get('Abstract', ''))),
    axis=1
)

# Save results to a new Excel file
df.to_excel('screened_studies.xlsx', index=False)

print("Screening complete. File saved as 'screened_studies.xlsx'.")
