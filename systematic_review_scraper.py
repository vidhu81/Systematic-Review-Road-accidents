import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from Bio import Entrez
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import rispy
import pandas as pd
# ---------- CONFIG ----------
EMAIL = "srividhya.anand2021@gmail.com"
SCOPUS_API_KEY = "e051d30938a8167944ec5ce630394b94"
PUBMED_QUERY = '''("accidents, traffic"[MeSH Terms] OR (("Road"[Title/Abstract] OR "driv*"[Title/Abstract]) 
AND ("accident*"[Title/Abstract] OR "crash*"[Title/Abstract] OR "colli*"[Title/Abstract] 
OR "mishap*"[Title/Abstract] OR "pileup*"[Title/Abstract] OR "disast*"[Title/Abstract]))) 
AND ("India"[MeSH Terms] OR "India"[Title/Abstract] OR "India"[Affiliation] 
OR "India"[Place of Publication]) AND ("cost of illness"[MeSH Terms] 
OR "quality adjusted life years"[MeSH Terms] OR "wounds and injuries"[MeSH Terms] 
OR "mortality"[MeSH Terms] OR "death"[MeSH Terms] OR "morbidity"[MeSH Terms] 
OR "fatal outcome"[MeSH Terms] OR "injur*"[Title/Abstract] OR "death*"[Title/Abstract] 
OR "fatal*"[Title/Abstract] OR "morbid*"[Title/Abstract] OR "mortalit*"[Title/Abstract] 
OR "trauma*"[Text Word] OR "health impact"[Title/Abstract] OR "disab*"[Text Word]) 
AND 2006/01/01:2024/12/31[Date - Publication])'''
SCOPUS_QUERY = 'TITLE-ABS-KEY("traffic accident" OR "road accident" OR "crash" OR "collision") AND TITLE-ABS-KEY(India) AND PUBYEAR > 2005 AND PUBYEAR < 2025'

# ---------- PUBMED ----------
def fetch_pubmed(query, max_results=200):
    Entrez.email = EMAIL
    print("Searching PubMed...")
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]
    
    articles = []
    for i, pmid in enumerate(ids):
        fetch = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
        data = fetch.read()
        articles.append({'pmid': pmid, 'raw': data})
        time.sleep(0.3)
    return articles

# ---------- SCOPUS ----------
def fetch_scopus(query):
    print("Searching Scopus...")
    client = ElsClient(SCOPUS_API_KEY)
    search = ElsSearch(query, 'scopus')
    search.execute(client, get_all=False)
    results = search.results[:200] 
    return results

# ---------- SAFETYLIT ----------

# Path to your .ris file
input_ris_file = ['combined_ris_075507.ris','combined_ris_075536.ris']
output_excel_file = 'safetylit.xlsx'

# Read the RIS file
entries = []
for ris_file in input_ris_file:
    with open(ris_file, 'r', encoding='utf-8') as file:
        entries.extend(rispy.load(file))

# Convert to DataFrame
df = pd.DataFrame(entries)

# Save to Excel
df.to_excel(output_excel_file, index=False)

print(f"✅ RIS file converted and saved to '{output_excel_file}'")





# ---------- MAIN ----------
if __name__ == "__main__":
    pubmed_data = fetch_pubmed(PUBMED_QUERY, max_results=200)
    pd.DataFrame(pubmed_data).to_excel("results_pubmed.xlsx", index=False)
    
    scopus_data = fetch_scopus(SCOPUS_QUERY)
    pd.DataFrame(scopus_data).to_excel("results_scopus.xlsx", index=False)

    