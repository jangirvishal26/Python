import sys
import tarfile

def extract_tar_file(tar_filename, destination):
    with tarfile.open(tar_filename) as tar:
        extract_entries(tar, destination)

def extract_entries(tar, destination):
    # BAD: This could write any file on the filesystem.
    for entry in tar:
        tar.extract(entry, destination)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <tar_filename>")
        sys.exit(1)

    tar_filename = sys.argv[1]
    extract_tar_file(tar_filename, "/tmp/unpack/")
