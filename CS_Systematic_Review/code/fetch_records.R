library(easyPubMed)
library(tidyverse)
library(metagear)
library(here)

my_query <- '("accidents, traffic"[MeSH Terms] OR (("Road"[Title/Abstract] OR "driv*"[Title/Abstract]) 
              AND ("accident*"[Title/Abstract] OR "crash*"[Title/Abstract] OR "colli*"[Title/Abstract] 
              OR "mishap*"[Title/Abstract] OR "pileup*"[Title/Abstract] OR "disast*"[Title/Abstract]))) 
              AND ("India"[MeSH Terms] OR "India"[Title/Abstract] OR "India"[Affiliation] 
              OR "India"[Place of Publication]) AND ("cost of illness"[MeSH Terms] 
              OR "quality adjusted life years"[MeSH Terms] OR "wounds and injuries"[MeSH Terms] 
              OR "mortality"[MeSH Terms] OR "death"[MeSH Terms] OR "morbidity"[MeSH Terms] 
              OR "fatal outcome"[MeSH Terms] OR "injur*"[Title/Abstract] OR "death*"[Title/Abstract] 
              OR "fatal*"[Title/Abstract] OR "morbid*"[Title/Abstract] OR "mortalit*"[Title/Abstract] 
              OR "trauma*"[Text Word] OR "health impact"[Title/Abstract] OR "disab*"[Text Word]) 
              AND 2006/01/01:2024/12/31[Date - Publication])'


# ✅ Step 1: Get PubMed IDs
my_entrez <- get_pubmed_ids(my_query)

# ✅ Step 2: Fetch Data
my_abstracts_txt <- fetch_pubmed_data(my_entrez, format = "xml")

# ✅ Step 3: Parse and Extract
my_df <- articles_to_list(my_abstracts_txt) |>
  lapply(article_to_df) |>
  bind_rows()

# ✅ Save results
fs::dir_create("data")
readr::write_csv(my_df, "data/pubmed_search_20241231.csv")










# fulltext::ft_get(my_results$doi[1], type = "pdf")


my_query <- '("accidents, traffic"[MeSH Terms] OR (("Road"[Title/Abstract] OR "driv*"[Title/Abstract]) 
              AND ("accident*"[Title/Abstract] OR "crash*"[Title/Abstract] OR "colli*"[Title/Abstract] 
              OR "mishap*"[Title/Abstract] OR "pileup*"[Title/Abstract] OR "disast*"[Title/Abstract]))) 
              AND ("India"[MeSH Terms] OR "India"[Title/Abstract] OR "India"[Affiliation] 
              OR "India"[Place of Publication]) AND ("cost of illness"[MeSH Terms] 
              OR "quality adjusted life years"[MeSH Terms] OR "wounds and injuries"[MeSH Terms] 
              OR "mortality"[MeSH Terms] OR "death"[MeSH Terms] OR "morbidity"[MeSH Terms] 
              OR "fatal outcome"[MeSH Terms] OR "injur*"[Title/Abstract] OR "death*"[Title/Abstract] 
              OR "fatal*"[Title/Abstract] OR "morbid*"[Title/Abstract] OR "mortalit*"[Title/Abstract] 
              OR "trauma*"[Text Word] OR "health impact"[Title/Abstract] OR "disab*"[Text Word]) 
              AND 2006/01/01:2024/12/31[Date - Publication])'
fulltext::ft_search(my_query, from = "scopus")

