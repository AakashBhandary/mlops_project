import os
from pathlib import Path

package_name = "mongodb_connect"

file_list = [
    # for writing workflows and configurations for continuous integration and deployment
    ".github/workflows/.gitkeep", 

    # source code components
    "./src/__init__.py",
    f"./src/{package_name}/__init__.py",
    f"./src/{package_name}/mongo_crud.py",
    "./src/components/__init__.py",
    "./src/components/data_ingestion.py",
    "./src/components/data_transformation.py",
    "./src/components/model_trainer.py",
    "./src/components/model_evaluation.py",

    # source code for pipelining the components
    "./src/pipeline/__init__.py",
    "./src/pipeline/training_pipeline.py",
    "./src/pipeline/prediction_pipeline.py",
    
    # utility functions
    "./src/utils/__init__.py",
    "./src/utils/utils.py",

    # logging and exceptions
    "./src/logger/logging.py",
    "./src/exception/exception.py",

    # testing -> (unit and integration testing)
    "./tests/unit/__init__.py",
    "./tests/unit/unit.py",
    "./tests/integration/__init__.py",
    "./tests/integration/integration.py",

    # setup script
    "init_setup.sh",

    # production requirements
    "requirements.txt",

    # development requirements
    "requirements_dev.txt",

    # setup files
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",

    # files for experimenting
    "./experiments/experiments.ipynb"
]

for file_path in file_list:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        # logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass # creates an empty file
