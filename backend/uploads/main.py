from flask import Flask, request, jsonify
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
CHUNK_SIZE = 5000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the uploaded file
    file.save(file_path)

    # Check if the file is a zip file
    if zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(app.config['UPLOAD_FOLDER'])
        os.remove(file_path)  # Remove the zip file after extraction

    # Process files in chunks
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    total_files = len(files)
    progress = 0
    chunks = [files[i:i + CHUNK_SIZE] for i in range(0, total_files, CHUNK_SIZE)]

    for chunk in chunks:
        # Simulate processing of files
        progress += len(chunk)
        percentage = (progress / total_files) * 100
        print(f"Progress: {percentage:.2f}%")

    return jsonify({'message': 'Uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)