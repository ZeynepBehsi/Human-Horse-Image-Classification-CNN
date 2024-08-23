import requests

# URLs
urls = [
    "https://storage.googleapis.com/tensorflow-1-public/course2/week3/horse-or-human.zip",
    "https://storage.googleapis.com/tensorflow-1-public/course2/week3/validation-horse-or-human.zip"
]

# Download process
for url in urls:
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"{filename} downloaded.")


import zipfile

# Unzip training set
local_zip = './horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('./horse-or-human')
zip_ref.close()

# Unzip validation set
local_zip = './validation-horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('./validation-horse-or-human')
zip_ref.close()
