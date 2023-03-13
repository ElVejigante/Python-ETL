# Import the required library
import requests

# Get the zip file (create path)
path = "https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip"
response = requests.get(path)

# Print the status code
print(response.status_code)

# Save the file locally (open())
local_path = f"tmp/data/source/downloaded_at=2021-02-01/PPR-ALL.zip"
with open(local_path, "wb") as f:
    f.write(response.content)

# Exploring a ZIP file

# Import the required method
from zipfile import ZipFile

with ZipFile(path, mode="r") as f:
    #Get the list of files and print it
    file_names = f.namelist()
    print(file_names)