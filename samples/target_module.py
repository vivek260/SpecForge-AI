import os
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class SpecForgeEngine:
    """
    A Universal Code-to-Spec Conversion Engine.
    This engine treats any source code as input and generates a 
    Technical Specification regardless of the domain (Finance, Health, Web, etc.).
    """

    def __init__(self, model_name: str = "llama3.1"):
        print(f"--- SpecForge-AI: Initializing Universal Architect Engine ---")
        
        # Initialize Local LLM
        self.llm = ChatOllama(model=model_name, temperature=0)
        
        # Domain-Agnostic Architectural Prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "You are an expert Software Architect. Your goal is to reverse-engineer "
                "the provided source code and generate a formal Technical Specification.\n\n"
                "Structure your output as follows:\n"
                "## 1. Module Overview: High-level purpose of the code.\n"
                "## 2. Technical Interfaces: Analysis of classes, functions, and parameters.\n"
                "## 3. Logic Flow: Step-by-step breakdown of the internal algorithms.\n"
                "## 4. Dependencies & Requirements: External libraries or system needs."
            )),
            ("user", "Analyze the following source code and generate the specification:\n\n{code}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()

    def generate_spec(self, input_file_path: str):
        path = Path(input_file_path)
        if not path.exists():
            print(f"Error: {input_file_path} not found.")
            return

        code_content = path.read_text()
        print(f"📝 Forging specification for: {path.name}...")
        
        # AI Processing
        specification = self.chain.invoke({"code": code_content})

        # Save Output
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        (output_dir / f"{path.stem}_spec.md").write_text(specification)
        
        print(f"✅ Specification created: output/{path.stem}_spec.md")

if __name__ == "__main__":
    engine = SpecForgeEngine()
    # You can point this to ANY .py file you want to document
    engine.generate_spec("samples/target_module.py")