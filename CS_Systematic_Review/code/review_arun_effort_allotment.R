# Abstract Screen the discrepancies/discordant articles

# Screening Abstract

library(tidyverse)
library(metagear)
library(here)

my_results <- read_csv(here("data", "df_to_review_20250426.csv"))

my_results <- my_results |> 
  rename(AUTHORS = authors,
         ABSTRACT = abstract,
         TITLE = title,
         DOI = doi)

effort_distribute(my_results,
                  initialize = TRUE,
                  reviewers = c("arun"),
                  save_split = TRUE, 
                  directory = 'effort/arun')

abstract_screener("effort/arun/effort_arun.csv",
                  aReviewer = "arun",
                  highlightKeywords = c("caesarean", "and", "methods"))
