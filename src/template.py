import os
from pathlib import Path

list_of_files = [
    # Root level files
    "README.md",
    "run.py",
    "setup.py",
    "LICENSE",
    
    # Source directory structure
    "src/__init__.py",
    "src/requirements.txt",
    "src/.gitignore",
    
    # Core module
    "src/Core/__init__.py",
    "src/Core/config.py",
    "src/Core/constants.py",
    
    # View module
    "src/View/__init__.py",
    "src/View/templates/",
    "src/View/static/",
    
    # Controller module
    "src/Controller/__init__.py",
    "src/Controller/routes.py",
    
    # Model module
    "src/Model/__init__.py",
    "src/Model/sentiment_analyzer.py",
    
    # Utils module
    "src/Utils/__init__.py",
    "src/Utils/helpers.py",
    
    # Docker module
    "src/Docker/__init__.py",
    "src/Docker/Dockerfile",
    "src/Docker/docker-compose.yml",
    
    # Data and artifact directories
    "DataSets/",
    "Artifacts/",
    "images/",
    "NoteBooks/"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(name=filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)):
        if filename in ["Artifacts", "DataSets", "images", "NoteBooks"]:
            os.makedirs(name=filepath, exist_ok=True)
        else:
            with open(file=filepath, mode="w") as f:
                pass
    else:
        print(f"{filepath} is already exists")