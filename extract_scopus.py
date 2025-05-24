from habanero import Crossref
import pandas as pd

import re
import html
dois = [
    "10.47203/IJCH.2024.v36i06.024",
    "10.2174/9789815238181124010016",
    "10.3969/j.issn.0253-4967.2024.06.004",
    "10.1016/j.chemgeo.2024.122472",
    "10.1016/j.lithos.2024.107845",
    "10.1063/5.0240241",
    "10.1108/K-04-2023-0620",
    "10.4271/2024-28-0212",
    "10.48165/jiafm.2024.46.2(Suppl).4",
    "10.11867/j.issn.1001-8166.2024.096",
    "10.3390/rs16244765",
    "10.1371/journal.pone.0312595",
    "10.1371/journal.pone.0312729",
    "10.3390/ai5040124",
    "10.3390/min14121234",
    "10.3390/min14121292",
    "10.3390/rs16244771",
    "10.17491/jgsi/2024/174041",
    "10.1029/2024TC008687",
    "10.1029/2024JB029447",
    "10.1029/2024TC008609",
    "10.1093/nsr/nwae356",
    "10.1785/0120230319",
    "10.1007/s44192-024-00118-w",
    "10.1007/s13146-024-00997-8"
]

cr = Crossref()
results = []

def clean_abstract(raw_text):
    # Convert HTML entities like &lt; to <, &gt; to >
    unescaped = html.unescape(raw_text)
    # Remove all tags like <jats:p>, <b>, etc.
    clean_text = re.sub(r"<[^>]+>", "", unescaped)
    return clean_text.strip()

for doi in dois:
    try:
        work = cr.works(ids=doi)
        raw_abstract = work['message'].get('abstract', 'Not available')
        title = work['message'].get('title', [''])[0]
        abstract = clean_abstract(raw_abstract) if raw_abstract != 'Not available' else 'Not available'
        results.append({'DOI': doi, 'Title': title, 'Abstract': abstract})
    except Exception as e:
        results.append({'DOI': doi, 'Title': 'Error', 'Abstract': str(e)})

# Save to Excel
df = pd.DataFrame(results)
df.to_excel("doi_abstracts_cleaned.xlsx", index=False)
print("Saved as doi_abstracts_cleaned.xlsx")

