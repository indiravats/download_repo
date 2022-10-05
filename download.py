import os
import pandas as pd
from git import Repo

results = pd.read_csv('results.csv')
results_compact = results.head(10)

repo_list = []

for i in range(len(results_compact)):
  repo_list.append(results_compact.name[i])

for i in range(len(results_compact)):
  folder_name = repo_list[i].split('/')
  x = 'https://github.com/' + repo_list[i]
  location = '/Users/indiravats/PycharmProjects/download-repo/downloaded/repository_'+ folder_name[1]
  Repo.clone_from(x, location)

