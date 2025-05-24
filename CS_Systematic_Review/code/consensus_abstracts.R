# Consensus between Alekhya and Shreyas

library(tidyverse)
library(here)

df_alekhya <- here('data', 'effort_alekhya_completed.csv') |> 
  read_csv()

df_shreyas <- here('data', 'effort_shreyas_completed.csv') |> 
  read_csv()


df_alekhya <- df_alekhya |> janitor::clean_names()
df_shreyas <- df_shreyas |> janitor::clean_names()

df_alekhya |> 
  count(include)

df_shreyas |> 
  count(include)

# Rename include

df_alekhya <- df_alekhya |> 
  rename(include_alekhya = include)

df_shreyas <- df_shreyas |> 
  rename(include_shreyas = include)


# Join Both

df <- df_alekhya |> 
  select(study_id, include_alekhya) |> 
  left_join(df_shreyas)

# Consensus

### Select common YES

yes_study_id <- df |> 
  filter(include_alekhya == "YES") |> 
  filter(include_shreyas == "YES") |> 
  pull(study_id)

df_common_yes <- df |> 
  filter(include_alekhya == "YES") |> 
  filter(include_shreyas == "YES") 

df_common_yes |> 
  write_csv(here('data', 'df_common_yes_20250426.csv'))

no_study_id <- df |> 
  filter(include_alekhya == "NO") |> 
  filter(include_shreyas == "NO") |> 
  pull(study_id)

df |> 
  filter(!study_id %in% c(yes_study_id, no_study_id)) |> 
  mutate(test = include_alekhya == include_shreyas) |> 
  filter(test) |> 
  select(include_alekhya, include_shreyas)

df_to_review <- df |> 
  filter(!study_id %in% c(yes_study_id, no_study_id)) 

df_to_review |> 
  write_csv(here('data', 'df_to_review_20250426.csv'))
