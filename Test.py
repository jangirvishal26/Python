import zipfile
import os

with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    for file_info in zip_ref.infolist():
        file_name = file_info.filename
        # WARNING: This could write any file on the filesystem.
        with zip_ref.open(file_name) as source, open(file_name, 'wb') as sink:
            sink.write(source.read())
