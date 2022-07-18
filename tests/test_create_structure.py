import os

def test_create_packages():


    base_path = "./output/"
    packages = ["my_project", "tests"]

    create_packages(base_path, packages)

    assert os.path.exists("./output/tests")
    assert os.path.exists("./output/tests/__init__.py")

def test_create_files():
    base_path = "./output/"
    files = [".gitignore", "README.md", "requirements.txt", ]
    for file in files:
        path_to_file = os.path.join(base_path, file)
        create_file(path_to_file)
    assert os.path.exists("./output/.gitignore")
    assert os.path.exists("./output/README.md")

def create_packages(base_path, packages):
    try:
        for package in packages:
            directory = os.path.join(base_path, package)
            os.mkdir(directory)
            init_py_file = os.path.join(directory, "__init__.py")
            create_file(init_py_file)
    except OSError:
        print("Creation of the directory %s failed" % package)
    else:
        print("%s created " % package)


def create_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'w+').close()
