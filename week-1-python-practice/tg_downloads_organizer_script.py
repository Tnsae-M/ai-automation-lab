import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

tg_path = os.path.join("C:\\", "Users", "ThinkPad", "Downloads")

# Extension to folder mapping
extension_mapping = {
    ".pdf": "pdfs",
    ".md": "mds",
    ".txt": "txts",
    ".jpg": "jpgs",
    ".jpeg": "jpgs",
    ".png": "pngs",
    ".wav": "audios",
    ".mp3": "audios",
    ".mp4": "videos",
    ".doc": "docs",
    ".docx": "docs",
    ".xls": "spreadsheets",
    ".xlsx": "spreadsheets",
    ".ppt": "presentations",
    ".pptx": "presentations",
    ".zip": "archives",
    ".rar": "archives",
    ".csv": "csvs"
}

def handle_duplicate(dest_path):
    """Handle duplicate files by renaming them with a counter."""
    if not os.path.exists(dest_path):
        return dest_path
    
    name, ext = os.path.splitext(dest_path)
    counter = 1
    new_path = f"{name}_{counter}{ext}"
    
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{name}_{counter}{ext}"
    
    logger.warning(f"Duplicate detected. Renaming to: {os.path.basename(new_path)}")
    return new_path

def organize_files():
    """Organize files in the target directory by file type."""
    try:
        if not os.path.exists(tg_path):
            logger.error(f"Directory not found: {tg_path}")
            return
        
        files = os.listdir(tg_path)
        logger.info(f"Found {len(files)} items to process")
        
        for f in files:
            updated_path = os.path.join(tg_path, f)
            
            # Skip directories
            if os.path.isdir(updated_path):
                continue
            
            try:
                # Get file extension using os.path.splitext and convert to lowercase
                _, ext = os.path.splitext(f)
                ext_lower = ext.lower()
                
                # Check if extension exists in mapping
                if ext_lower not in extension_mapping:
                    logger.debug(f"Skipping file with unmapped extension: {f}")
                    continue
                
                # Get destination folder from mapping
                dest_folder = extension_mapping[ext_lower]
                dest_dir = os.path.join(tg_path, dest_folder)
                
                # Create destination folder
                os.makedirs(dest_dir, exist_ok=True)
                
                # Prepare destination path
                dest_path = os.path.join(dest_dir, f)
                
                # Handle duplicates
                dest_path = handle_duplicate(dest_path)
                
                # Move file
                shutil.move(updated_path, dest_path)
                logger.info(f"Moved '{f}' to '{dest_folder}/'")
                
            except Exception as e:
                logger.error(f"Error processing file '{f}': {str(e)}")
                continue
    
    except Exception as e:
        logger.error(f"Error in organize_files: {str(e)}")

if __name__ == "__main__":
    organize_files()