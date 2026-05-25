from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

import shutil
import os

from app.services.cv_parser import extract_text_from_pdf
from app.services.ai_service import improve_cv
from app.services.pdf_service import generate_pdf

router = APIRouter()


@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    # guardar PDF original
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # extraer texto
    text = extract_text_from_pdf(file_path)

    # mejorar CV con IA
    improved_cv = improve_cv(text)

    # generar nuevo PDF
    output_pdf = f"outputs/improved_{file.filename}"

    generate_pdf(improved_cv, output_pdf)

    # devolver PDF
    return FileResponse(
        output_pdf,
        media_type="application/pdf",
        filename=f"improved_{file.filename}"
    )