import os
import uuid
import zipfile

from typing import List
from fastapi import UploadFile

UPLOAD_FOLDER = "uploads"
CHUNK_SIZE = 5000

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


async def process_uploads(
    files: List[UploadFile],
    upload_type: str
):
    session_id = str(uuid.uuid4())
    session_folder = os.path.join(
        UPLOAD_FOLDER,
        session_id
    )
    os.makedirs(session_folder, exist_ok=True)
    total_files = len(files)
    uploaded_files = []
    processed_count = 0
    progress_data = []
    chunks = [
        files[i:i + CHUNK_SIZE]
        for i in range(0, total_files, CHUNK_SIZE)
    ]
    for chunk in chunks:
        for file in chunk:
            filename = file.filename
            if not filename:
                continue
            save_path = os.path.join(
                session_folder,
                filename
            )
            try:
                os.makedirs(
                    os.path.dirname(save_path),
                    exist_ok=True
                )
                with open(save_path, "wb") as buffer:
                    content = await file.read()
                    buffer.write(content)
                uploaded_files.append(filename)
                if zipfile.is_zipfile(save_path):

                    extract_folder = os.path.join(
                        session_folder,
                        filename.replace(".zip", "")
                    )
                    os.makedirs(
                        extract_folder,
                        exist_ok=True
                    )
                    with zipfile.ZipFile(save_path, "r") as zip_ref:
                        zip_ref.extractall(extract_folder)
                    os.remove(save_path)
                processed_count += 1
                percentage = round(
                    (processed_count / total_files) * 100,
                    2
                )
                progress_data.append({
                    "processed": processed_count,
                    "total": total_files,
                    "percentage": percentage
                })
            except FileExistsError as e:
                error_message = f"[Errno 17] File exists: '{save_path}'"
                print({"message": error_message, "success": False})
    return {
        "success": True,
        "message": "Upload completed successfully",
        "uploadType": upload_type,
        "sessionId": session_id,
        "totalFiles": total_files,
        "uploadedFiles": uploaded_files,
        "progress": progress_data,
        "uploadPath": session_folder
    }