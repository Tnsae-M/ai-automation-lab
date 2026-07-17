from pathlib import Path
from analyze_resume import analyze_resume
from reader import read_resume
INPUT_DIR=Path(__file__).parent/"input"
resume_files=list(INPUT_DIR.glob("*.pdf"))+list(INPUT_DIR.glob("*.txt"))
for resume in resume_files:
    if resume.name=="tinsae.melkamu.backend.CV.pdf":
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
            projects=output_txt.projects
            job_readiness_verdict=output_txt.job_readiness_verdict
            print(f"name: {name}\n\ntarget job: {target_job}\n\nResume score: {score}\n\n languages:{languages}\n\nprojects: {projects}\n\nstrengths:{strengths}\n\nweaknesses: {weaknesses}\n\nimprovement points: {improvement}\n\njob readiness verdict: {job_readiness_verdict}")
        except Exception as e:
            print(f"Skipped resume {resume.name}.\nreason: {e}")
