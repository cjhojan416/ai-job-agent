from fastapi import APIRouter, UploadFile, File, Form
import tempfile
import os

from app.services.cv_parser import extract_text_from_pdf
from app.services.ats_service import analyze_cv_match

router = APIRouter()


def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)


@router.post("/analyze-match")
async def analyze_match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        content = await file.read()
        temp_file.write(content)

        temp_path = temp_file.name

    try:

        cv_text = extract_text_from_pdf(temp_path)

        analysis = analyze_cv_match(
            cv_text,
            job_description
        )

        return {
            "analysis": analysis
        }

    finally:

        delete_file(temp_path)