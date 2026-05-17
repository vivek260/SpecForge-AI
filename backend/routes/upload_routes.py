from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse

from typing import List

from services.upload_service import process_uploads

router = APIRouter()


@router.post("/upload")
async def upload_files(
    uploadType: str = Form(...),
    files: List[UploadFile] = File(...)
):

    try:

        result = await process_uploads(
            files=files,
            upload_type=uploadType
        )

        return JSONResponse(
            status_code=200,
            content=result
        )

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(e)
            }
        )