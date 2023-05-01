import os
import pandas as pd

ANALYSED_PATH = '/data/indira/csl/download_repo/test_analyzed/'
RESULTS_PATH = '/data/indira/csl/download_repo/test_result/'

def listdir_nohidden(path):
  dirlist = []
  for f in os.listdir(path):
    if not f.startswith('.'):
      if not f.endswith('.txt'):
        dirlist.append(f)
  return dirlist

analyzed_list = listdir_nohidden(ANALYSED_PATH)

rep_name = []
loc_count = []
commit_name = []
classes_list = []
methods_list = []
arch_smells_list = []
design_smells_list = []
impl_smells_list = []
testability_smells_list = []
test_smells_list = []

for i in analyzed_list:
    print("For repository:", i)
    dir_path = os.path.join(ANALYSED_PATH, i)
    commit_list = listdir_nohidden(dir_path)
    for j in commit_list:
      commit_path = os.path.join(dir_path, j)
      type_metrics_path = os.path.join(commit_path, "TypeMetrics.csv")
      method_metrics_path = os.path.join(commit_path, "MethodMetrics.csv")
      arch_smells_path = os.path.join(commit_path, "ArchitectureSmells.csv")
      design_smells_path = os.path.join(commit_path, "DesignSmells.csv")
      impl_smells_path = os.path.join(commit_path, "ImplementationSmells.csv")
      testability_smells_path = os.path.join(commit_path, "TestabilitySmells.csv")
      test_smells_path = os.path.join(commit_path, "TestSmells.csv")
      df_type = pd.read_csv(type_metrics_path)
      df_method = pd.read_csv(method_metrics_path)
      df_arch = pd.read_csv(arch_smells_path)
      #df_design = pd.read_csv(design_smells_path, on_bad_lines='skip')
      df_design = pd.read_csv(design_smells_path, usecols=["Project Name", "Package Name", "Type Name", "Design Smell", "Cause of the Smell"])
      df_impl = pd.read_csv(impl_smells_path)
      df_testability = pd.read_csv(testability_smells_path)
      df_test = pd.read_csv(test_smells_path)
      LOC_sum = df_type.LOC.sum()
      classes = df_type.shape[0]
      methods = df_method.shape[0]
      archsmells = df_arch.shape[0]
      designsmells = df_design.shape[0]
      implsmells = df_impl.shape[0]
      testsmells = df_test.shape[0]
      testabilitysmells = df_testability.shape[0]
      arch_smells_list.append(archsmells) 
      design_smells_list.append(designsmells)
      impl_smells_list.append(implsmells)
      testability_smells_list.append(testabilitysmells)
      test_smells_list.append(testsmells)
      loc_count.append(LOC_sum)
      rep_name.append(i)
      commit_name.append(j)
      classes_list.append(classes)
      methods_list.append(methods)

list_of_tuples = list(zip(rep_name, commit_name, loc_count, classes_list, methods_list, arch_smells_list, design_smells_list, impl_smells_list, testability_smells_list, test_smells_list))
df_results = pd.DataFrame(list_of_tuples, columns=['Repository Name', 'Commit', 'LOC', 'Classes', 'Methods', 'Architecture Smells', 'Design Smells', 'Implementation Smells', 'Testability Smells', 'Test Smells'])
output_path = RESULTS_PATH + "output.csv"
df_results.to_csv(output_path)
