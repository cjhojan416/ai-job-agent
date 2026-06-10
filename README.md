# AI Job Agent - Backend

Backend desarrollado con FastAPI para el procesamiento de currículums y análisis ATS mediante Inteligencia Artificial.

Clonar el repositorio:

```bash
git clone https://github.com/cjhojan416/ai-job-agent
```

## Tecnologías

* Python
* FastAPI
* Uvicorn
* pdfplumber
* Ollama 
* ReportLab

## Instalación

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Variables de entorno

Crear archivo `.env`


## Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponible en:

```text
http://localhost:8000
```

## Estructura del proyecto

```text
app/
│
├── routes/
│   └── cv_routes.py
│
├── services/
│   ├── cv_parser.py
│   ├── ats_service.py
│   └── cv_generator_service.py
│
└── main.py
```

## Endpoints

### POST /analyze

Analiza la compatibilidad entre un CV y una oferta laboral.

#### Entrada

* CV en PDF
* Descripción de la oferta

#### Salida

* Fortalezas detectadas
* Recomendaciones

---

### POST /generate-cv

Genera una nueva versión optimizada del CV.

#### Entrada

* CV original
* Oferta laboral

#### Salida

* Nuevo CV optimizado
* PDF descargable

## Flujo interno

1. Recepción del PDF.
2. Extracción de texto mediante pdfplumber.
3. Comparación con oferta laboral.
4. Procesamiento mediante IA.
5. Generación de CV optimizado.
6. Construcción de PDF.
7. Retorno al frontend.

## Próximas mejoras

* Caché de resultados.
* Historial de análisis.
* Soporte para DOCX.
* API de autenticación.
* Sistema avanzado de puntuación ATS.

## Autor

Jhojan Cardona
