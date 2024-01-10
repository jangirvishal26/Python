import os

def source_input():
    user_input = input("Enter the path: ")
    return user_input

def download(path):
    os.system("wget " + path)

# Example usage
download(source_input())
