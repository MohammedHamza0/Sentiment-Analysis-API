import os
from pathlib import Path



list_of_files = 

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