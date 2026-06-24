from agent import agent

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "How do I become a Backend Developer?"
            }
        ]
    }
)

print(result["messages"][-1].content)