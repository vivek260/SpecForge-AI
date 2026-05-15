SpecForge-AI: Secure Code-to-Spec Agent 🚀

SpecForge-AI is a privacy-first, local AI agent designed to bridge the gap between source code and technical documentation. Built for enterprise environments where data security is paramount, it utilizes local Large Language Models (LLMs) to reverse-engineer code into professional-grade technical specifications.

🏗️ Architecture & Design Patterns

This project is built following strict software engineering principles to ensure scalability and maintainability:

SOLID Principles: - Single Responsibility: Isolated layers for ingestion, AI processing, and storage.

Open/Closed: The engine supports any local model (Llama, Mistral, Codestral) without core code changes.

Pipeline Pattern: Uses LangChain Expression Language (LCEL) to chain prompts and models.

Layered Architecture: Clear separation between core logic, sample data, and generated artifacts.

🛡️ Security Features

100% Local Execution: Powered by Ollama, ensuring no source code ever leaves your machine or company network.

Zero-Data-Leakage: No external API calls to OpenAI or Anthropic.

🚀 Tech Stack

Orchestration: LangChain

Intelligence: Meta Llama 3.1 (via Ollama)

Language: Python 3.x

Format: Markdown (Documentation)

🛠️ Setup Instructions

### Backend Setup

1. Prerequisite: Local LLM

Install Ollama and pull the model:

```bash
ollama pull llama3.1
```

2. Installation

```bash
git clone https://github.com/your-username/SpecForge-AI.git
cd SpecForge-AI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Usage

From the frontend, you will need to upload your code as a zip file. The steps are as follows:

1. Navigate to the frontend application at `http://localhost:3000`.
2. Use the upload feature to select and upload your zip file containing the code.
3. The zip file will be sent to the backend for processing.
4. The backend will process the uploaded code and generate the documentation.
5. The generated documentation will be available in the `output/` folder.

### Frontend Setup

1. Navigate to the `frontend/` directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`.

📈 Future Roadmap

- [ ] Support for multi-file repository scanning.
- [ ] Integration with Mistral Codestral for complex logic.
- [ ] Automated Reviewer Agent for documentation validation.
