from pathlib import Path
from analyze_resume import analyze_resume
from reader import read_resume
INPUT_DIR=Path(__file__).parent/"input"
resume_files=list(INPUT_DIR.glob("*.pdf"))+list(INPUT_DIR.glob("*.txt"))
for resume in resume_files:
    print("===============================")
    input_txt=read_resume(resume)
    output_txt=analyze_resume(input_txt)
    print(output_txt)