from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from crewai import Crew
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(...)
):
    try:
        # Read uploaded file
        contents = await file.read()
        document_text = contents.decode("utf-8")

        # Create Crew
        crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_financial_document],
            verbose=True
        )

        # Run Crew
        result = crew.kickoff(
            inputs={"document_text": document_text}
        )

        # DO NOT use .get()
        return {
            "analysis": str(result)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing financial document: {str(e)}"
        )