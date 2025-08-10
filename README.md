# DrugForge

DrugForge is a conceptual rewrite of the [CellForge](https://github.com/gersteinlab/CellForge) framework, repurposed for AI-assisted drug design. It provides a multi-agent pipeline that decomposes natural-language drug discovery goals into actionable plans, generates computational workflows, and evaluates their outcomes.

## Overview

DrugForge aims to:

- Analyse textual drug design objectives and break them into structured tasks.
- Design appropriate computational methods (e.g. QSAR modelling, docking, generative chemistry).
- Generate executable models or code fragments using large language models.
- Evaluate candidate molecules or models against provided datasets.

This repository currently contains a lightweight skeleton illustrating how the pipeline could be organised. It serves as a starting point for further development.

## Structure

```
 drugforge/
 ├── __init__.py            # Package entry point with run_end_to_end_workflow
 ├── end_to_end_workflow.py # Orchestrates the multi-step pipeline
 ├── task_analysis.py       # Stub for analysing textual tasks
 ├── method_design.py       # Stub for selecting algorithms/strategies
 ├── model_generation.py    # Stub for producing code or models
 ├── evaluation.py          # Stub for assessing results
 └── llm.py                 # Minimal LLM interface abstraction
 tests/
 └── test_workflow.py       # Ensures the workflow executes
```

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:

   ```bash
   pytest
   ```

## Roadmap

Future iterations will focus on:

- Integrating real molecular datasets and cheminformatics libraries.
- Adding retrieval-augmented generation for domain knowledge.
- Implementing advanced evaluation metrics such as docking scores or ADMET predictions.
- Enabling collaborative multi-agent optimisation loops.

Contributions are welcome!

