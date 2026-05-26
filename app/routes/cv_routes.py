from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse

import os
import tempfile

from app.services.cv_parser import extract_text_from_pdf
from app.services.ai_service import improve_cv
from app.services.pdf_service import generate_pdf

router = APIRouter()


def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)


@router.post("/upload-cv")
async def upload_cv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):

    # =========================
    # Crear archivo temporal input
    # =========================

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input:

        content = await file.read()
        temp_input.write(content)

        input_path = temp_input.name

    try:

        # =========================
        # Extraer texto
        # =========================

        text = extract_text_from_pdf(input_path)

        # =========================
        # Mejorar CV con IA
        # =========================

        improved_cv = improve_cv(text)

        # =========================
        # Crear PDF temporal output
        # =========================

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_output:

            output_path = temp_output.name

        # Generar PDF
        generate_pdf(improved_cv, output_path)

        # =========================
        # Eliminar archivos luego
        # =========================

        background_tasks.add_task(delete_file, input_path)
        background_tasks.add_task(delete_file, output_path)

        # =========================
        # Retornar PDF
        # =========================

        return FileResponse(
            output_path,
            media_type="application/pdf",
            filename=f"improved_{file.filename}"
        )

    except Exception as e:

        # limpiar input si ocurre error
        delete_file(input_path)

        return {"error": str(e)}