import sys
import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def build():
    TasksForCommonProjectStructure().standardized_tasks_build_for_docker_library_project_in_common_project_structure(str(Path(__file__).absolute()), "QualityCheck", 1, sys.argv)


if __name__ == "__main__":
    build()
