import os
import subprocess
import git
import multiprocessing

def _build_java_project(dir_path):
    print("Attempting compilation...")
    os.environ['JAVA_HOME']
    is_compiled = False
    pom_path = os.path.join(dir_path, 'pom.xml')
    if os.path.exists(pom_path):
        print("Found pom.xml")
        os.chdir(dir_path)
        proc = subprocess.Popen(
            [r'mvn', 'clean', 'install', '-DskipTests'])
        proc.wait()
        is_compiled = True

    gradle_path = os.path.join(dir_path, "build.gradle")
    if os.path.exists(gradle_path):
        print("Found build.gradle")
        os.chdir(dir_path)
        try:
            proc = subprocess.Popen([r'gradle', 'compileJava'])
            proc.wait()
        except Exception as ex:
            print(ex)
            exit(1)
        is_compiled = True
    if not is_compiled:
        print("Did not compile")

def _run_designite_java(folder_path, out_path):
    print("Analyzing ...")
    proc = subprocess.Popen(
        ["java", "-jar", DESIGNITEJAVA_CONSOLE_PATH, "-i", folder_path, "-o", out_path, "-ac", '""'])
    proc.wait()
    print("done analyzing.")

def analyze_java_repo(folder_path, folder_name):
    print("Analyzing " + folder_name + " ...")
    out_path = os.path.join(JAVA_RESULTS_PATH, folder_name)

    _build_java_project(folder_path)
    _run_designite_java(folder_path, out_path)

JAVA_HOME = "/Library/Java/Home/bin/java"

def listdir_nohidden(path):
  dirlist = []
  for f in os.listdir(path):
    if not f.startswith('.'):
      dirlist.append(f)
  return dirlist

BASE_PATH = '/data/indira/csl/download_repo' 
DESIGNITEJAVA_CONSOLE_PATH= os.path.join(BASE_PATH, 'DesigniteJava.jar')
JAVA_RESULTS_PATH = os.path.join(BASE_PATH, 'analyzed')
DOWNLOAD_PATH = os.path.join(BASE_PATH, 'downloaded')

list_of_dirs = listdir_nohidden(DOWNLOAD_PATH)

chunked_list_of_dirs = list()
chunk_size = 125 

for i in range(0, len(list_of_dirs), chunk_size):
   chunked_list_of_dirs.append(list_of_dirs[i:i+chunk_size])


def run_designite_1():
  for i in chunked_list_of_dirs[0]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_2():
  for i in chunked_list_of_dirs[1]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_3():
  for i in chunked_list_of_dirs[2]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_4():
  for i in chunked_list_of_dirs[3]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_5():
  for i in chunked_list_of_dirs[4]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_6():
  for i in chunked_list_of_dirs[5]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_7():
  for i in chunked_list_of_dirs[6]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

def run_designite_8():
  for i in chunked_list_of_dirs[7]:
    folder_path = os.path.join(DOWNLOAD_PATH, i)
    analyze_java_repo(folder_path, i) 
    os.chdir(BASE_PATH)

if __name__ == "__main__":
  p1 = multiprocessing.Process(target=run_designite_1)
  p2 = multiprocessing.Process(target=run_designite_2)
  p3 = multiprocessing.Process(target=run_designite_3)
  p4 = multiprocessing.Process(target=run_designite_4)
  p5 = multiprocessing.Process(target=run_designite_5)
  p6 = multiprocessing.Process(target=run_designite_6)
  p7 = multiprocessing.Process(target=run_designite_7)
  p8 = multiprocessing.Process(target=run_designite_8)

  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p5.start()
  p6.start()
  p7.start()
  p8.start()

  p1.join()
  p2.join()
  p3.join()
  p4.join()
  p5.join()
  p6.join()
  p7.join()
  p8.join()

  print("Done")
