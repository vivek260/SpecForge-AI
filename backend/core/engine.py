from pathlib import Path

def generate_spec(self, input_file_or_dir: str) -> str:
        """
        Engine layer: Focuses purely on data extraction and AI execution.
        Throws clean exceptions if prerequisites fail.
        """
        path = Path(input_file_or_dir)
        
        # 1. Input Validation - Throw standard Python exceptions
        if not path.exists():
            raise FileNotFoundError(f"Asset path '{input_file_or_dir}' does not exist.")

        if path.is_dir():
            py_files = list(path.glob("**/*.py"))
            if not py_files:
                raise ValueError("No processing targets (.py files) found in directory.")
            code_content = "\n\n".join([f"# File: {f.name}\n{f.read_text(encoding='utf-8')}" for f in py_files[:3]])
        else:
            code_content = path.read_text(encoding='utf-8')

        # 2. Pipeline Execution
        try:
            specification = self.chain.invoke({"code": code_content})
            
            # Validation: Ensure the LLM actually returned data
            if not specification or not specification.strip():
                raise RuntimeError("AI Engine returned an empty specification string.")
                
            self._save_output(path, specification)
            return specification
            
        except Exception as e:
            # Re-raise the exception so the FastAPI layer knows it failed
            raise RuntimeError(f"LLM Processing Failed: {str(e)}")