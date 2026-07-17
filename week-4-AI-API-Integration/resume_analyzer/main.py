from pathlib import Path
from analyze_resume import analyze_resume
from reader import read_resume
INPUT_DIR=Path(__file__).parent/"input"
resume_files=list(INPUT_DIR.glob("*.pdf"))+list(INPUT_DIR.glob("*.txt"))
for resume in resume_files:
    try:
        print("===============================")
        print(resume.name)
        print("===============================")
        input_txt=read_resume(resume)
        output_txt=analyze_resume(input_txt)
        if output_txt is None:
            print(f"Skipped {resume.name}:analysis failed")
            continue
        name=output_txt.name
        score=output_txt.resume_score
        target_job=output_txt.target_job
        languages=output_txt.languages
        strengths=output_txt.strength
        weaknesses=output_txt.weakness
        improvement=output_txt.suggestion
        print(f"name: {name}\ntarget job: {target_job}\nResume score: {score}\n languages:{languages}\nstrengths:{strengths}\nweaknesses: {weaknesses}\nimprovement points: {improvement}")
    except Exception as e:
        print(f"Skipped resume {resume.name}.\nreason: {e}")
