import ast
import logging
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CodeValidatorInput(BaseModel):
    """Input schema for Code Validator."""
    code: str = Field(..., description="Python code to validate")

class CodeValidatorTool(BaseTool):
    name: str = "Code Validator"
    description: str = "Validates Python code syntax without executing it. Returns validation results and any syntax errors."
    args_schema: Type[BaseModel] = CodeValidatorInput

    def _run(self, code: str) -> str:
        """Validate Python code syntax."""
        logger.info("🔧 CODE VALIDATOR TOOL CALLED - Validating code syntax")
        try:
            # Parse the code using AST
            ast.parse(code)
            result = "✅ Code is syntactically valid"
            logger.info(f"🔧 CODE VALIDATOR RESULT: {result}")
            return result
        except SyntaxError as e:
            result = f"❌ Syntax Error: {e.msg} at line {e.lineno}, column {e.offset}"
            logger.info(f"🔧 CODE VALIDATOR RESULT: {result}")
            return result
        except Exception as e:
            result = f"❌ Validation Error: {str(e)}"
            logger.info(f"🔧 CODE VALIDATOR RESULT: {result}")
            return result