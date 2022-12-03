import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def run_testcases():
    TasksForCommonProjectStructure().standardized_tasks_run_testcases_for_docker_project_in_common_project_structure(str(Path(__file__).absolute()), 1,  "QualityCheck", sys.argv)


if __name__ == "__main__":
    run_testcases()
