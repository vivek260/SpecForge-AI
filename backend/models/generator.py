class GeneratorRequest(BaseModel):
    storage_path: str
    model_name: str = "llama3.1"

class GeneratorResponse(BaseModel):
    success: bool
    message: str
    response_path: str | None = None