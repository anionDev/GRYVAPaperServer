import os
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def run_example():
    TasksForCommonProjectStructure().run_dockerfile_example(str(Path(__file__).absolute()), 3, True)


if __name__ == "__main__":
    run_example()
