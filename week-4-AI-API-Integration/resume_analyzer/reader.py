from pathlib import Path
from pypdf import PdfReader

def read_resume(filepath: str) -> str:
    path = Path(filepath)
    
    if path.suffix == ".txt":
        # your code here
        ...
    elif path.suffix == ".pdf":
        # your code here — use the pattern from last message
        ...
    else:
        # what should happen here?
        ...