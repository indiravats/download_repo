from pydriller import Repository
import os
import pandas as pd
import errno

BASE_DIR = "/data/indira/csl/download_repo/" 
DATASET_DIR = os.path.join(BASE_DIR, "results.csv")
DOWNLOADED_DIR = os.path.join(BASE_DIR, "downloaded")
ANALYZED_DIR = os.path.join(BASE_DIR, "analyzed_repo")

results = pd.read_csv(DATASET_DIR)
remove = results['name'].str.split('/', expand=True)[results['name'].str.split('/', expand=True).duplicated([1], keep='last')]
results.drop(remove.index, axis=0, inplace=True)
results['github_link'] = 'https://github.com/' + results['name'].astype(str)
results[['repo_author', 'repo_name']] = results.name.str.split('/', expand=True)
results_final = results[['repo_name', 'repo_author', 'github_link']]

repo_links = []
for i in os.listdir(DOWNLOADED_DIR):
  if i in results_final['repo_name'].tolist():
    x = results_final.loc[results_final['repo_name'] == i, 'repo_author'].item()
    link = 'https://github.com/' + x + '/' + i
    repo_links.append(link)

op_folder_names = []

folder_name = []
for i in repo_links:
  folder_name.append(i.split('/')[-1])

for i in folder_name:
    op_folder_names.append(i.split('/')[-1])

os.chdir(ANALYZED_DIR)

try:
  for i in op_folder_names:
    new_dir = os.path.join(ANALYZED_DIR, i)
    os.mkdir(new_dir)
except OSError as exc:
  if exc.errno != errno.EEXIST:
    raise
  pass

for i in repo_links:
  if i.split('/')[-1] in results_final.repo_name.tolist():
    link = results_final.loc[results_final['repo_name']== i.split('/')[-1], 'github_link'].item()
    path = os.path.join(ANALYZED_DIR, i.split('/')[-1])
    os.chdir(path)

  for commit in Repository(link).traverse_commits():
      current_hash = commit.hash[0:9]
      directory = current_hash
      parent_dir = path
      current_path = os.path.join(parent_dir, directory)

      if not os.path.exists(current_path):
        os.makedirs(current_path)
        print("Directory '%s' created for '%s' folder in '%s' path" %(directory, i.split('/')[-1], current_path))
      else:
        print("Directory '%s' already exists" % directory)
