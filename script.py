import os
import shutil

def organize_files():
    files=os.listdir("downloads")
    for f in files:
        source_path=os.path.join("downloads",f)
        if os.path.isdir(source_path):
            continue
        if f.endswith(".pdf"):
            os.makedirs("downloads/pdfs",exist_ok=True)
            shutil.move(source_path,"downloads/pdfs")
        elif f.endswith(".md"):
            os.makedirs("downloads/mds",exist_ok=True)
            shutil.move(source_path,"downloads/mds")
        elif f.endswith(".txt"):
            os.makedirs("downloads/txts",exist_ok=True)
            shutil.move(source_path,"downloads/txts")
organize_files()