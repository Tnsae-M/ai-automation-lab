from pathlib import Path
from pypdf import PdfReader

INPUT_DIR=Path(__file__).parent/"input"
resume_files=list(INPUT_DIR.glob("*.pdf"))+list(INPUT_DIR.glob("*.txt"))
def read_resume(filepath: str) -> str:
    path = Path(filepath)
    if path.suffix == ".txt":
        return path.read_text(encoding="utf-8")
    elif path.suffix == ".pdf":
       reader=PdfReader(path)
       return "\n".join(page.extract_text() or "" for page in reader.pages)
    else:
       raise ValueError(f"Unsupported file type: {path.suffix}")
for resume in resume_files:
    if resume.name=="Tinsae_Melkamu_intern_CV.pdf":
        text=read_resume(resume)
print(text[:300])