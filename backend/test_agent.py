from agent import agent

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
                I want to become a FastAPI developer.

                Give me:
                1. Learning Roadmap
                2. Learning Resources
                3. Practice Projects
                4. Daily Study Plan
                """
            }
        ]
    }
)

print(result["messages"][-1].content)
print("ROADMAP TOOL CALLED")
print("RESOURCES TOOL CALLED")
print("PROJECTS TOOL CALLED")
print("PLANNER TOOL CALLED")