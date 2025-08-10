import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from drugforge import run_end_to_end_workflow


def test_workflow_runs():
    assert run_end_to_end_workflow("design an inhibitor") is True
