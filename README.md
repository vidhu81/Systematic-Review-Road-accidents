"""# Systematic Review: Road Traffic Accidents in India (2006–2024)

## Objective
To evaluate the epidemiological patterns, public health impact, and trends in road traffic accidents in India from 2006 to 2024.

## Inclusion Criteria
- Study location: India
- Time frame: 2006–2024
- Focus: Public health and epidemiological aspects of road traffic accidents
- Language: English
- Excludes: Clinical/surgical post-accident outcomes, Non-Indian studies, if the article is not available for free access, no full text article 
  

## Databases Searched
- PubMed
- Scopus
- Embase
- MEDLINE
- SafetyLit

**## Search Strategy**
```plaintext
("accidents, traffic"[MeSH Terms] OR (("Road"[Title/Abstract] OR "driv*"[Title/Abstract]) 
AND ("accident*"[Title/Abstract] OR "crash*"[Title/Abstract] OR "colli*"[Title/Abstract] 
OR "mishap*"[Title/Abstract] OR "pileup*"[Title/Abstract] OR "disast*"[Title/Abstract]))) 
AND ("India"[MeSH Terms] OR "India"[Title/Abstract] OR "India"[Affiliation] 
OR "India"[Place of Publication]) 
AND ("cost of illness"[MeSH Terms] OR "quality adjusted life years"[MeSH Terms] 
OR "wounds and injuries"[MeSH Terms] OR "mortality"[MeSH Terms] OR "death"[MeSH Terms] 
OR "morbidity"[MeSH Terms] OR "fatal outcome"[MeSH Terms] OR "injur*"[Title/Abstract] 
OR "death*"[Title/Abstract] OR "fatal*"[Title/Abstract] OR "morbid*"[Title/Abstract] 
OR "mortalit*"[Title/Abstract] OR "trauma*"[Text Word] 
OR "health impact"[Title/Abstract] OR "disab*"[Text Word]) 
AND 2006/01/01:2024/12/31[Date - Publication])```


**## Coding**
-Python code for scraping in safetylit could not scrape easily so ris file for first two hundred entries
-Python is used for data extraction using API from pubmed and scopus
- Tried in Embase using API key but it does not allow for access. 
- results were stored as excel file 


results_scopus_cleaned.xlsx has the article details with scopusid, title, author, doi, abstract, date of publication, journal, open access flag got from scopus.

similarly other pubmed and safetylit data is saved and merged data sheet is also there 

before abstract screening 
(<systematic review data from scopus Pubmed and safetylit before abstract screening.xlsx>) this has all the data 

200 entries from safetylit, 200 entries from pubmed and 25 from sopus are there. 
425 entries 
After deduplication also there are 425 entries 

-next we are going to apply title screenin and abstract screening 