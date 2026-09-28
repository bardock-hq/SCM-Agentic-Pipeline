import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from scraper import fetch_latest_scm_news

# Load GEMINI_API_KEY from .env
load_dotenv()

# Initialize Gemini model for CrewAI
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Fetch news data using scraper
news = fetch_latest_scm_news()

# Agent 1: SCM Researcher
researcher = Agent(
    role='Global Logistics Intelligence Analyst',
    goal='Analyze supply chain disruptions, port delays, and freight rates.',
    backstory='An expert operational analyst specializing in global maritime trade trends.',
    verbose=True,
    llm=gemini_llm
)

# Agent 2: Executive Strategist
strategist = Agent(
    role='Executive Supply Chain Strategist',
    goal='Translate logistics disruption news into actionable business insights.',
    backstory='A former VP of Supply Chain turning operational updates into C-suite briefings.',
    verbose=True,
    llm=gemini_llm
)

# Tasks
task1 = Task(
    description=f"Analyze this logistics news item:\nTitle: {news['title']}\nSummary: {news['summary']}",
    agent=researcher,
    expected_output="An operational disruption breakdown."
)

task2 = Task(
    description="Draft a 2-sentence executive summary with 2 relevant logistics hashtags for LinkedIn.",
    agent=strategist,
    expected_output="Formatted social post content."
)

# Multi-Agent Crew Execution
scm_crew = Crew(
    agents=[researcher, strategist],
    tasks=[task1, task2],
    process=Process.sequential
)

if __name__ == "__main__":
    result = scm_crew.kickoff()
    print("\n================== AGENT OUTPUT ==================")
    print(result)
    