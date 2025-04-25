import os
from pathlib import Path



list_of_files = [
     "artifacts",
     "DataSets",
     "images",
     "NoteBooks/notebook.ipynb",
     "src/__init__.py",
     "src/schemas/__init__.py",
     "src/schemas/input_output_schema.py",
     "src/utils/__init__.py",
     "src/utils/inferance.py",
     "src/utils/text_processor.py",
     "src/config.py",
     ".env",
     ".env.example",
     "requirements.txt",
     "backend.py",
     "frontend.py",
]


for filepath in list_of_files:
     filepath = Path(filepath)
     filedir, filename = os.path.split(filepath)
     if filedir != "":
          os.makedirs(name=filedir, exist_ok=True)
          
     if (not os.path.exists(filepath)):
          if filename in  ["artifacts", "DataSets, images"]:
               os.makedirs(name=filename, exist_ok=True)
          else:
               with open(file=filepath, mode="w") as f:
                    pass
     else:
          print(f"{filepath} is already exists")