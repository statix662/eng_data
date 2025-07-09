from importlib import resources

# Get package data

PACKAGE_DATA = resources.files("eng_data.data")

# Get user data


# Combine data souces
DATA_DIRS = [PACKAGE_DATA]

def get_dirs():
    subdirs = [d for d in PACKAGE_DATA.iterdir() if d.is_dir() and d.name != "__pycache__"]
    for d in subdirs:
        print(d)
