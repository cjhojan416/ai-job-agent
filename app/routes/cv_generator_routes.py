from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import StreamingResponse
import tempfile
import os
from app.services.cv_parser import extract_text_from_pdf
from app.services.cv_generator_service import (
    generate_optimized_cv,
    create_pdf
)

router = APIRouter()
def delete_file(path: str):

    if os.path.exists(path):

        os.remove(path)

@router.post("/generate-cv")
async def generate_cv(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        content = await file.read()

        temp_file.write(content)

        temp_path = temp_file.name

    try:

        cv_text = extract_text_from_pdf(temp_path)

        optimized_cv = generate_optimized_cv(
            cv_text,
            job_description
        )

        pdf_buffer = create_pdf(optimized_cv)

        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=optimized_cv.pdf"
            }
        )

    finally:

        delete_file(temp_path)