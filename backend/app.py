from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload_routes import router as upload_router

app = FastAPI(
    title="Code Upload API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(upload_router)


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "FastAPI backend running"
    }