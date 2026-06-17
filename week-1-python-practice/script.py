import os
import shutil

def organize_files():
    files=os.listdir("downloads")
    for f in files:
        source_path=os.path.join("downloads",f)
        if os.path.isdir(source_path):
            continue
        if f.endswith(".pdf"):
            #use os.path.join("downloads","pdfs") instead of plain "downloads/pdfs"
            os.makedirs(os.path.join("downloads","pdfs"),exist_ok=True)
            shutil.move(source_path,os.path.join("downloads","pdfs",f))
        elif f.endswith(".md"):
            os.makedirs(os.path.join("downloads","mds"),exist_ok=True)
            shutil.move(source_path,os.path.join("downloads","mds",f))
        elif f.endswith(".txt"):
            os.makedirs(os.path.join("downloads","txts"),exist_ok=True)
            shutil.move(source_path,os.path.join("downloads","txts",f))
organize_files()