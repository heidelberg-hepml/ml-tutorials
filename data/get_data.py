""" Get lhc datasets """

import os, sys
import wget
from zipfile import ZipFile
from tqdm import tqdm

n_dataset = int(sys.argv[1])
DESTINATION = sys.argv[2]

baseURL = "https://www.thphys.uni-heidelberg.de/~plehn/data/"
if n_dataset == 1:
    URL = "tutorial-2-data.zip"
    DESCRIPTION = "amplitude regression"
    TUTS = [2,3,4]
elif n_dataset == 2:
    URL = "toptagging-short.zip"
    DESCRIPTION = "top tagging"
    TUTS = [5,6,7,8,9]
elif n_dataset == 3:
    URL = "tutorial-10-data.zip"
    DESCRIPTION = "anomaly detection"
    TUTS = [10]
elif n_dataset == 4:
    URL = "tutorial-11-data.zip"
    DESCRIPTION = "event generation"
    TUTS = [11,12,13,14,15]
else:
    raise ValueError(f"Loading dataset {n_dataset} not implemented")

os.chdir(DESTINATION)
fullURL = baseURL + URL

# download zip file
print(f"Trying to download dataset {n_dataset} ('{DESCRIPTION}', used in tutorials {TUTS}) from {fullURL} to {URL}")
wget.download(fullURL, URL)

# Re-open the newly-created file with ZipFile()
with ZipFile(URL ,"r") as zip_ref:
     for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist())):
          zip_ref.extract(member=file)

print(f"Successfully extracted files from {URL}")
