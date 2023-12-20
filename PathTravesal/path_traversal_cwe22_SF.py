import tarfile

def untar_image(path, filename):
    tar_file = tarfile.open(filename, 'r|gz')
    tar_file.extract_all(path)
    image_file = tar_file.get_names()[0]
    tar_file.close()
    return os.path.join(path, image_file)
