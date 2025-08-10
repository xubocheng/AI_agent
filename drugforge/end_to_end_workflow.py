"""End-to-end orchestration for DrugForge."""

from .task_analysis import analyze_task
from .method_design import design_method
from .model_generation import generate_model
from .evaluation import evaluate_model


class EndToEndWorkflow:
    """Coordinate the full drug design pipeline."""

    def run_complete_workflow(self, task_description: str, dataset_info: dict | None = None) -> bool:
        plan = analyze_task(task_description)
        blueprint = design_method(plan)
        model = generate_model(blueprint)
        return evaluate_model(model, dataset_info)
