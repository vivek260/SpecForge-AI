// CodeToSpec.tsx

import { useState } from "react";
import "./CodeToSpec.css";

type UploadType = "folder" | "file" | "zip";

export default function CodeToSpec() {
  const [selectedType, setSelectedType] = useState<UploadType | "">("");
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadMessage, setUploadMessage] = useState("");
  const MAX_FILES = 5000;
  const [generateSpecButton, setGenerateSpecButton] = useState(false);
  const [storedPath, setStoredPath] = useState("");

  const handleFiles = (files: FileList | null) => {
    if (!files) return;

    const fileArray = Array.from(files);

    // Prevent huge uploads
    if (fileArray.length > MAX_FILES) {
      setUploadMessage(
        `Too many files selected (${fileArray.length}).
Please upload ZIP instead.`,
      );

      setSelectedFiles([]);

      return;
    }

    setUploadMessage("");

    setSelectedFiles(fileArray);

    console.log("Selected Files:", fileArray);
  };

  const handleGenerateSpec = async (storedPath) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/generate_spec", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ uploadPath: storedPath.uploadPath }),
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Spec Generation Success:", result);
      } else {
        console.error("Spec Generation Failed");
      }
    } catch (error) {
      console.error("Error during spec generation:", error);
    }
  };

  const handleUpload = async () => {
    if (!selectedFiles.length) return;

    try {
      setUploadMessage("Uploading...");
      setUploadProgress(0);
      const formData = new FormData();
      selectedFiles.forEach((file) => {
        formData.append("files", file);
      });
      formData.append("uploadType", selectedType);
      const uploadUrl = "http://127.0.0.1:8000/upload";
      const xhr = new XMLHttpRequest();
      xhr.open("POST", uploadUrl, true);
      xhr.upload.onprogress = (event) => {
        if (event.lengthComputable) {
          const percent = Math.round((event.loaded / event.total) * 100);
          setUploadProgress(percent);
        }
      };

      xhr.onload = () => {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          console.log("Upload Success:", response);
          setUploadMessage("Upload completed successfully");
          setGenerateSpecButton(true);
          setStoredPath(response);
        } else {
          setUploadMessage("Upload failed");
        }
      };

      xhr.onerror = () => {
        setUploadMessage("Network error occurred");
      };

      xhr.send(formData);
    } catch (error) {
      console.error(error);
      setUploadMessage("Something went wrong");
    }
  };

  const resetState = () => {
    setUploadProgress(0);
    setUploadMessage("");
    setGenerateSpecButton(false);
    setStoredPath("");
  };

  return (
    <div className="upload-page">
      <div className="overlay"></div>

      <div className="upload-card">
        <h1>Code to Spec</h1>

        <p className="subtitle">Upload folder, files, or ZIP archive</p>

        {/* Upload Type */}
        <div className="upload-type-container">
          <button
            className={`type-btn ${selectedType === "folder" ? "active" : ""}`}
            onClick={() => {
              setSelectedType("folder");
              setSelectedFiles([]);
              resetState();
            }}
          >
            <img src="/icons/folder.png" alt="folder" className="type-icon" />

            <span>Folder</span>
          </button>

          <button
            className={`type-btn ${selectedType === "file" ? "active" : ""}`}
            onClick={() => {
              setSelectedType("file");
              setSelectedFiles([]);
              resetState();
            }}
          >
            <img src="/icons/file.png" alt="file" className="type-icon" />

            <span>File</span>
          </button>

          <button
            className={`type-btn ${selectedType === "zip" ? "active" : ""}`}
            onClick={() => {
              setSelectedType("zip");
              setSelectedFiles([]);
              resetState();
            }}
          >
            <img src="/icons/zip.png" alt="zip" className="type-icon" />

            <span>ZIP</span>
          </button>
        </div>

        {/* Upload Area */}
        <label className="upload-box">
          <div className="upload-icon">⬆</div>

          <p className="upload-text">Click to upload or drag & drop</p>

          <p className="upload-subtext">
            {!selectedType
              ? "Select upload type first"
              : `Selected type: ${selectedType}`}
          </p>

          {selectedFiles.length > 0 && (
            <p className="selected-files">
              {selectedFiles.length} file(s) selected
            </p>
          )}

          <input
            type="file"
            className="hidden-input"
            disabled={!selectedType}
            onChange={(e) => handleFiles(e.target.files)}
            {...(selectedType === "folder"
              ? {
                  webkitdirectory: "true",
                  directory: "",
                }
              : selectedType === "zip"
                ? {
                    accept: ".zip",
                  }
                : {
                    multiple: true,
                  })}
          />
        </label>

        {/* Progress */}
        {uploadProgress > 0 && (
          <div className="progress-container">
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${uploadProgress}%`,
                }}
              />
            </div>

            <p className="progress-text">{uploadProgress}%</p>
          </div>
        )}

        {/* Upload or Generate Spec Button */}
        {generateSpecButton ? (
          <button
            className="upload-btn"
            disabled={!storedPath}
            onClick={() => handleGenerateSpec(storedPath)}
          >
            Generate Spec
          </button>
        ) : (
          <button
            className={`upload-btn ${
              !selectedType || selectedFiles.length === 0 ? "disabled-btn" : ""
            }`}
            disabled={!selectedType || selectedFiles.length === 0}
            onClick={handleUpload}
          >
            Upload
          </button>
        )}

        {/* Upload Message */}
        {uploadMessage && <p className="upload-message">{uploadMessage}</p>}
      </div>
    </div>
  );
}
