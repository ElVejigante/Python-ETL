# Import the required library
import requests

# Get the zip file (create path)
path = "https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip"
response = requests.get(path)

