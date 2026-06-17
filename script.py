import os
import shutil

def organize_files():
    files=os.listdir("downloads")
    for f in files:
        # source_path=os.path.join("download",f)
        if os.path.isdir("downloads"+"/"+f):
            continue
        if f.endswith(".pdf"):
            os.makedirs("downloads/pdfs",exist_ok=True)
            shutil.move("downloads"+"/"+f,"downloads/pdfs")
        if f.endswith(".md"):
            os.makedirs("downloads/mds",exist_ok=True)
            shutil.move("downloads"+"/"+f,"downloads/mds")
        if f.endswith(".txt"):
            os.makedirs("downloads/txts",exist_ok=True)
            shutil.move("downloads"+"/"+f,"downloads/txts")
organize_files()