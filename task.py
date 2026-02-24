from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool


analyze_financial_document = Task(
    description="""
You are a senior financial analyst.

Analyze the provided financial document carefully.

1. Extract key financial metrics.
2. Identify revenue, expenses, profit.
3. Highlight financial risks.
4. Provide structured professional summary.

Use the FinancialDocumentTool when needed.
""",
    expected_output="Structured financial analysis report.",
    agent=financial_analyst,
    tools=[FinancialDocumentTool()]
)