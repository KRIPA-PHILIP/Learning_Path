from agent import agent

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": """
                Generate a complete learning path for becoming a FastAPI Developer.
                """
            }
        ]
    }
)

print(result["messages"][-1].content)