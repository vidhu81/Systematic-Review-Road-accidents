# Screening Abstract

library(tidyverse)
library(metagear)
library(here)

my_results <- read_csv("data/pubmed_search_20241220.csv")

my_results <- my_results |> 
  rename(AUTHORS = authors,
         ABSTRACT = abstract,
         TITLE = title, 
         DOI = doi)

effort_distribute(my_results,
                  initialize = TRUE,
                  reviewers = c("alekhya"),
                  save_split = TRUE, 
                  directory = 'effort')

abstract_screener("effort/effort_alekhya.csv",
                  aReviewer = "alekhya",
                  highlightKeywords = c("caesarean", "and", "methods"))











