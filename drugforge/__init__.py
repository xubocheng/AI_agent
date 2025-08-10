"""
DrugForge: AI-Assisted Drug Design via Multi-Agent Collaboration.

This package provides a minimal skeleton for a multi-agent pipeline that
analyses drug discovery tasks, designs computational strategies, generates
models or code, and evaluates the results.
"""

__version__ = "0.1.0"

from .end_to_end_workflow import EndToEndWorkflow

__all__ = ["run_end_to_end_workflow"]

def run_end_to_end_workflow(task_description: str, dataset_info: dict | None = None) -> bool:
    """Run the complete end-to-end workflow.

    Parameters
    ----------
    task_description:
        Text describing the drug design goal.
    dataset_info:
        Optional dataset metadata.

    Returns
    -------
    bool
        True if the workflow completed successfully.
    """
    workflow = EndToEndWorkflow()
    return workflow.run_complete_workflow(task_description, dataset_info)
