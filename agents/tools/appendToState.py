from google.adk.tools.tool_context import ToolContext

def append_to_state(
    tool_context: ToolContext, field: str, response: str
) -> dict[str, str]:
    """Append new output to an existing state key.

    Args:
        :param tool_context: (ToolContext) Context object containing state
        :param field: (str) a field name to append to
        :param response: (str) a string to append to the field

    Returns:
        dict[str, str]: {"status": "success"}
    """
    existing_state = tool_context.state.get(field, [])
    tool_context.state[field] = existing_state + [response]
    return {"status": "success"}