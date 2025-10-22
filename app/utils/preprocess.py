from app.system.prompt import SYSTEM_PROMPT, CHAT_HISTORY_PROMPT, USER_PROMPT

def build_prompt(user_input: str, chat_history: str) -> str:
    """
    Constructs the full prompt for the model, including system prompt,
    memory (if any), and cleaned user input.
    """
    user_input = clean_input(user_input)

    sections = [SYSTEM_PROMPT]
    sections.append(CHAT_HISTORY_PROMPT.format(chat_history=chat_history))
    sections.append(USER_PROMPT.format(user_input=user_input))

    return "\n".join(sections)

def clean_input(text: str) -> str:
    """
    Cleans user input: trims whitespace, normalizes line breaks, removes artifacts.
    """
    return text.strip().replace("\r\n", "\n").replace("\r", "\n")
