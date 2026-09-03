import json
from typing import Any,Callable

# ---------------------------------------------------------------------------
# 1. Tool Implementations (Deterministic mocks for testing)
# ---------------------------------------------------------------------------
def mock_search_places(query: str) -> dict[str, str]:
    """Simulates querying an external places or maps API."""
    print(f"  [Executing Tool: mock_search_places] query='{query}'")
    if "tomoca" in query.lower():
        return {
            "name": "Tomoca Coffee",
            "phone": "+251 11 111 2233",
            "website": "https://tomocacoffee.com",
            "city": "Addis Ababa"
        }
    return {"error": "No business found matching query"}

def mock_check_url_status(url: str) -> dict[str, Any]:
    """Simulates sending an HTTP HEAD request to check availability."""
    print(f"  [Executing Tool: mock_check_url_status] url='{url}'")
    if "tomocacoffee.com" in url:
        return {"url": url, "status_code": 200, "reachable": True}
    return {"url": url, "status_code": 404, "reachable": False}
# tool dispatcher
TOOL_DISPATCH:dict[str,Callable[...,Any]]={
    "mock_places":mock_search_places,
    "mock_url_search":mock_check_url_status
}
# LLM decision engine
def mock_llm_step(msgs:list[dict[str,Any]])->dict[str,Any]:
    has_search_result=any(
        msg.get("role")=="tool" and msg.get("name")=="mock_places" for msg in msgs
    )
    has_status_result=any(
        msg.get("role")=="tool" and msg.get("name")=="mock_url_search" for msg in msgs
    )
    # Turn 1: tool call-> No result yet
    if not has_search_result:
        return {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "name": "mock_places",
                    "arguments": {"query": "Tomoca Coffee Addis Ababa"}
                }
            ]
        }
    # 2nd turn ot iteration where the search result is attached as history.
    if not has_status_result:
        # The LLM reads the website directly from context
        return {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "name": "mock_url_search",
                    "arguments": {"url": "https://tomocacoffee.com"}
                }
            ]
        }
    # final iteration where all context is gathered and final response is prepared by the agent
    return{
        "role": "assistant",
        "content": (
            "Found Tomoca Coffee in Addis Ababa. Phone: +251 11 111 2233. "
            "Verified website: https://tomocacoffee.com (Status: 200 OK)."
        ),
        "tool_calls": []
    }
def run_agent(task_prompt:str,max_iter:int=5)->None:
    print(f"\n--- Starting Agent Run ---\nTask: '{task_prompt}'\n")
    messages:list[dict[str,Any]]=[{
        "role":"user","content":task_prompt
    }]
    for iteration in range(1,max_iter+1):
        print(f"[iteration {iteration} Calling LLM...]")
        decision=mock_llm_step(messages)
        messages.append(decision)
        tool_calls=decision.get("tool_calls",[])
        # Base case
        if not tool_calls:
            print("\n[Complete] Final Response:")
            print(decision["content"])
            return
        # Loop case
        for call in tool_calls:
            name=call['name']
            args=call['arguments']
            handler=TOOL_DISPATCH.get(name)
            if not handler:
                observation=f"Error: Tool {name} doesn't exist."
            else:
                observation=handler(**args)
            messages.append({
                "role":"tool",
                "name":name,
                "content":json.dumps(observation)
            })
    print("[Terminated] Exceeded Maximum iteration thershold")
if __name__=="__main__":
    run_agent("Find the phone number for Tomoca Coffee in Addis Ababa and verify if their website is reachable.")