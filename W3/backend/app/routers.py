from app.schemas import OCR_Response
from app.controllers import extract_ocr
from fastapi import APIRouter, File, UploadFile, status

router = APIRouter()

@router.post("/ocr")
async def ocr_api(file_upload: UploadFile = File(...)):
    ocr_result = extract_ocr(file_upload.file)
    return OCR_Response(
        data=ocr_result,
        status_code=status.HTTP_200_OK
    )



