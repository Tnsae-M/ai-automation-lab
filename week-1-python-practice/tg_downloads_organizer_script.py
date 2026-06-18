import os
import shutil
tg_path=os.path.join("C:\\","Users","ThinkPad","Downloads","Telegram Desktop")
def organize_files():
    files=os.listdir(tg_path)
    for f in files:
        updated_path=os.path.join(tg_path,f)
        if os.path.isdir(updated_path):
            continue
        # optionally use f.lowercase.endswith(".pdf",..)
        if f.endswith((".pdf",".PDF")):
            os.makedirs(os.path.join(tg_path,"pdfs"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"pdfs",f))
        elif f.endswith((".md",".MD")):
            os.makedirs(os.path.join(tg_path,"mds"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"mds",f))
        elif f.endswith((".txt",".TXT")):
            os.makedirs(os.path.join(tg_path,"txts"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"txts",f))
        elif f.endswith((".jpg",".JPG")):
            os.makedirs(os.path.join(tg_path,"jpgs"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"jpgs",f))
        elif f.endswith((".png",".PNG")):
            os.makedirs(os.path.join(tg_path,"pngs"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"pngs",f))
        elif f.endswith((".wav",".WAV")):
            os.makedirs(os.path.join(tg_path,"audios"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"audios",f))
        elif f.endswith((".doc",".DOC",".docx",".DOCX")):
            os.makedirs(os.path.join(tg_path,"docs"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"docs",f))
        elif f.endswith((".xls",".XLS",".xlsx",".XLSX")):
            os.makedirs(os.path.join(tg_path,"spreadsheets"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"spreadsheets",f))
        elif f.endswith((".ppt",".PPT",".pptx",".PPTX")):
            os.makedirs(os.path.join(tg_path,"presentations"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"presentations",f))
        elif f.endswith((".zip",".ZIP",".rar",".RAR")):
            os.makedirs(os.path.join(tg_path,"archives"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"archives",f))
        elif f.endswith((".csv",".CSV")):
            os.makedirs(os.path.join(tg_path,"csvs"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"csvs",f))
        elif f.endswith((".mp3",".MP3")):
            os.makedirs(os.path.join(tg_path,"audios"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"audios",f))
        elif f.endswith((".mp4",".MP4")):
            os.makedirs(os.path.join(tg_path,"videos"),exist_ok=True)
            shutil.move(updated_path,os.path.join(tg_path,"videos",f))
organize_files()