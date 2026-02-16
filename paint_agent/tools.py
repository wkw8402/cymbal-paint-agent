from dotenv import load_dotenv, find_dotenv
import os
from google.adk.tools import ToolContext

load_dotenv(find_dotenv())


def set_session_value(tool_context: ToolContext, key: str, value: str):
    tool_context.state[key] = value
    return {"status": f"stored '{value}' in '{key}'"}

