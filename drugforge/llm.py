"""Minimal LLM interface placeholder."""

class LLMInterface:
    """Simple abstraction for a language model client."""

    def __init__(self, model_name: str = "gpt-4"):
        self.model_name = model_name

    def chat(self, prompt: str) -> str:
        """Return a dummy response for the given prompt."""
        return f"LLM({self.model_name}) response to: {prompt}"
