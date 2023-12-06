import requests
import hashlib
import os
import pandas as pd
url_breast_cancer_zip = 'https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip' 
response = requests.get(url_breast_cancer_zip) 
if response.status_code == 200: 
    with open('breast+cancer+wisconsin+diagnostic.zip', mode='wb') as f: 
        f.write(response.content) 
    filename = 'breast+cancer+wisconsin+diagnostic.zip' 
    with open(filename, mode='rb') as f: 
        data = f.read() 
        sha256hash = hashlib.sha256(data).hexdigest() 
    cancer_sha_256 = 'bc154869ef13f753f9e2b5a17e248cfe1ba4b6721db7c4da9f4880e40b05d3af' 
    if cancer_sha_256 != sha256hash: 
        print("Computed hash does not match expected hash") 
    else: 
        print("Computed hash matches expected hash") 
else: 
    print(f"Could not download adult.zip. Status code: {response.status_code}") 

import hashlib

filename = r'C:\Users\Angel\Desktop\IS477-finalproject\data\breast_cancer_wisconsin\breast_cancer_wisconsin.csv'

with open(filename, 'rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

breast_sha_256 = '19cce5f6dba53d0e42fb63aed47f9603c6e88267e86534896cebe48e63f63062'
if breast_sha_256 != sha256hash:
    print("Computed hash does not match expected hash")
else:
    print("Computed hash matches expected hash")
