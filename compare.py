import os
import pandas as pd

def listdir_nohidden(path):
  dirlist = []
  for f in os.listdir(path):
    if not f.startswith('.'):
      dirlist.append(f)
  return dirlist

BASE_PATH = '/data/indira/csl/download_repo/'
ANALYZED_PATH = os.path.join(BASE_PATH, 'analyzed_repositories')
DOWNLOAD_PATH = os.path.join(BASE_PATH, 'downloaded')

repo_list = []
results = pd.read_csv('results.csv')
for i in range(len(results)):
  repo_list.append(results.name[i].split('/')[1])

print("Total repositories:", len(repo_list))
downloaded_dirs = listdir_nohidden(DOWNLOAD_PATH)
print("Downloaded repositories:", len(downloaded_dirs))
analyzed_dirs = listdir_nohidden(ANALYZED_PATH)
print("Analyzed repositores:", len(analyzed_dirs))

not_downloaded = [x for x in repo_list if x not in downloaded_dirs]
not_analyzed = [x for x in downloaded_dirs if x not in analyzed_dirs]

number_not_downloaded = len(not_downloaded)
number_not_analyzed = len(not_analyzed)

print("Number of repositories not downloaded:", number_not_downloaded)
print("Names of repositories not downloaded:", not_downloaded)
print("Number of repositories not analyzed:", number_not_analyzed)
print("Names of repositories not analyzed:", not_analyzed)
