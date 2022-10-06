import os
import pandas as pd
from git import Repo

results = pd.read_csv('results.csv')

repo_list = []

for i in range(len(results)):
  repo_list.append(results.name[i])

for i in range(len(results)):
  folder_name = repo_list[i].split('/')
  x = 'https://github.com/' + repo_list[i]
  location = '/data/indira/csl/download_repo/downloaded/'+ folder_name[1]
  Repo.clone_from(x, location)
  print("Downloading repository:", i+1)


