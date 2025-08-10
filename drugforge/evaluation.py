"""Evaluation module."""

def evaluate_model(model_desc: str, dataset_info: dict | None = None) -> bool:
    """Evaluate the generated model.

    Currently returns ``True`` unconditionally. Future versions will
    compute metrics such as binding affinity or ADMET predictions.
    """
    return True
