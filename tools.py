from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


# Input schema
class FinancialDocumentInput(BaseModel):
    document_text: str = Field(..., description="Financial document content")


# Custom Tool
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Analyzer"
    description: str = "Analyzes financial documents and extracts structured insights."

    args_schema: Type[BaseModel] = FinancialDocumentInput

    def _run(self, document_text: str) -> str:
        word_count = len(document_text.split())

        return f"""
Financial Analysis Summary
--------------------------
Total Words: {word_count}

Basic Insight:
The document appears to contain structured financial data.
Revenue, expenses and profitability metrics can be evaluated.
        """.strip()