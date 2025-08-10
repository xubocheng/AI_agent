"""Method design module."""

def design_method(task_plan: dict) -> dict:
    """Select algorithms and strategies to pursue the objective.

    Parameters
    ----------
    task_plan: dict
        Output from :func:`analyze_task` describing the objective.

    Returns
    -------
    dict
        Blueprint of algorithms or approaches to apply.
    """
    return {
        "plan": task_plan.get("objective", ""),
        "algorithms": ["QSAR", "Docking"],
    }
