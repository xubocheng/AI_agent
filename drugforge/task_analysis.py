"""Task analysis module."""

def analyze_task(description: str) -> dict:
    """Convert a natural-language drug design request into a plan.

    This stub simply wraps the description in a dictionary, but a real
    implementation would use language models to extract targets, desired
    properties, and constraints.
    """
    return {"objective": description}
