# Week 1 Python Practice

This directory contains a simple file organizer script written in Python. The script is designed to organize files in a specified download directory by file type, moving them into categorized subfolders.

## Script Purpose

- `tg_downloads_organizer_script.py` automatically sorts downloaded files into folders such as `pdfs`, `mds`, `txts`, `jpgs`, `pngs`, `audios`, `videos`, `docs`, `spreadsheets`, `presentations`, `archives`, and `csvs`.
- It is useful for maintaining a cleaner Downloads directory and reducing manual file management.

## Libraries Used

- `os`: for filesystem operations, path construction, and directory listing.
- `shutil`: for moving files between directories.

## Lessons Learned

- Correct path assignment is essential when working with absolute and relative directories.
- Basic Python syntax and control flow with `if`/`elif`/`else` statements were reinforced.
- Handling file extensions in a case-insensitive way improves reliability.
- Using `os.makedirs(..., exist_ok=True)` provides safe folder creation without errors when the folder already exists.

## Notes

The script is a practical refresher on file handling, directory manipulation, and using standard Python libraries for automation tasks.