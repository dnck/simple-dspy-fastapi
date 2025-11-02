from fastapi import FastAPI
from pydantic import BaseModel

from generate_llms_txt import run_dspy_pipeline #, summarize_for_pr

class Request(BaseModel):
    repo: str
    ref: str | None = None

class Response(BaseModel):
    file_path: str
    content: str
    summary: str

app = FastAPI()

@app.post("/generate_llms_txt", response_model=Response)
def generate(req: Request):
    # 1) clone/checkout repo@ref to tmp (or mount workspace passed by Newman)
    # 2) run your DsPy pipeline to produce llms.txt content
    content = run_dspy_pipeline(repo=req.repo)
    # summ = summarize_for_pr(content)
    summ = "Summary generation not implemented."
    return Response(file_path="llms.txt", content=content, summary=summ)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)