"""Model generation module."""

def generate_model(method_blueprint: dict) -> str:
    """Produce a model or code representation for the chosen algorithms.

    Parameters
    ----------
    method_blueprint: dict
        Output from :func:`design_method` specifying algorithms.

    Returns
    -------
    str
        Description of the generated model or code.
    """
    algs = ", ".join(method_blueprint.get("algorithms", []))
    return f"Generated model using {algs}"
