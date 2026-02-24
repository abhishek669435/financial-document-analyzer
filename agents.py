from crewai import Agent

# Financial Analyst Agent
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and extract meaningful insights.",
    backstory="An expert financial analyst skilled in balance sheets, income statements, and financial risk evaluation.",
    llm="gpt-4o-mini",
    verbose=True
)

# Verifier Agent
verifier = Agent(
    role="Financial Report Verifier",
    goal="Review and validate financial analysis reports for correctness and clarity.",
    backstory="A senior financial auditor ensuring high accuracy and structured reporting.",
    llm="gpt-4o-mini",
    verbose=True
)