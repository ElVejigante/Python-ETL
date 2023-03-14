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
    # Get the list of files and print it
    file_names = f.namelist()
    print(file_names)
    # Extract the CSV file
    csv_file_path = f.extract(file_names[0])
    print(csv_file_path)

# Reading from a CSV file
import csv
from pprint import pprint

# Open the CSV file in read mode
with open(path, mode="r", encoding="windows-1252") as csv_file:
    # Open csv_file so that each row is a dictionary
    reader = csv.DictReader(csv_file)

    # Print the first row
    row = next(reader)
    print(type(row))
    pprint(row)

fieldnames = {
    "Date of Sale (dd/mm/yyyy)": "date_of_sale",
    "Address": "address",
    "Postal Code": "postal_code",
    "County": "county",
    "Price (€)": "price",
    "Description of Property": "description",
}

    