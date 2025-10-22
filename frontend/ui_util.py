import streamlit.components.v1 as components
import json

def avatar(role):
    return "🤖" if role == "kino" else "🧔🏻"

def get_author(role):
    return "**" + role.capitalize() + "**: "

def log_to_console(message: str) -> None:
    js_code = f"""
<script>
    console.log({json.dumps(message)});
</script>
"""
    components.html(js_code)