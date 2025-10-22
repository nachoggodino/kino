class ChatHistory:
    def __init__(self, max_turns=5):
        self.turns = []
        self.max_turns = max_turns

    def add(self, user_msg: str, kino_reply: str):
        self.turns.append((user_msg, kino_reply))
        if len(self.turns) > self.max_turns:
            self.turns = self.turns[-self.max_turns:]

    def format(self) -> str:
        lines = []
        for user, kino in self.turns:
            lines.append(f"User: {user}")
            lines.append(f"Kino: {kino}")
        return "\n".join(lines)
