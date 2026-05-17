from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from core.engine import SpecForgeEngine
from models.generator import GeneratorRequest, GeneratorResponse

router = APIRouter()
@router.post("/generate_spec")
async def generate_specification(payload: GeneratorRequest):
    try:
        engine = SpecForgeEngine(model_name=payload.model_name)
        markdown_spec = engine.generate_spec(payload.storage_path)
        
        return GeneratorResponse(
            success=True,
            message="Technical specification forged successfully.",
            response_path=payload.storage_path
        )
        # return JSONResponse(
        #     status_code=status.HTTP_200_OK,
        #     content={
        #         "success": True,
        #         "specification": markdown_spec,
        #         "message": "Technical specification forged successfully."
        #     }
        # )

    except FileNotFoundError as fnf_err:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"success": False, "message": str(fnf_err)}
        )
        
    except ValueError as val_err:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"success": False, "message": str(val_err)}
        )

    except Exception as general_err:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": f"Internal Architecture Error: {str(general_err)}"
            }
        )