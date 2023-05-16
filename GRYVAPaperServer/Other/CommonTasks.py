import sys
import os
import urllib.request
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def download_paperserver():
    folder_of_this_file = os.path.dirname(os.path.realpath(__file__))
    resource_folder = GeneralUtilities.resolve_relative_path("./Resources/PaperServer", folder_of_this_file)
    GeneralUtilities.ensure_directory_does_not_exist(resource_folder)
    GeneralUtilities.ensure_directory_exists(resource_folder)
    target_file = os.path.join(resource_folder, "PaperServer.jar")
    urllib.request.urlretrieve("https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/538/downloads/paper-1.19.4-538.jar", target_file)


def common_tasks():
    file = str(Path(__file__).absolute())
    folder_of_current_file = os.path.dirname(file)
    sc = ScriptCollectionCore()
    cmd_args = sys.argv
    t = TasksForCommonProjectStructure()
    codeunitname = os.path.basename(GeneralUtilities.resolve_relative_path("..", os.path.dirname(file)))
    verbosity = t.get_verbosity_from_commandline_arguments(cmd_args, 1)
    targetenvironmenttype = t.get_targetenvironmenttype_from_commandline_arguments(cmd_args, "QualityCheck")
    additional_arguments_file = t.get_additionalargumentsfile_from_commandline_arguments(cmd_args, None)
    codeunit_version = sc.get_semver_version_from_gitversion(GeneralUtilities.resolve_relative_path(
        "../..", os.path.dirname(file)))  # Should always be the same as the project-version
    download_paperserver()
    sc.replace_version_in_dockerfile_file(GeneralUtilities.resolve_relative_path(f"../{codeunitname}/Dockerfile", folder_of_current_file), codeunit_version)
    t.standardized_tasks_do_common_tasks(file, codeunit_version, verbosity, targetenvironmenttype, True, additional_arguments_file, True, cmd_args)
    t.standardized_tasks_update_version_in_docker_examples(file, codeunit_version)


if __name__ == "__main__":
    common_tasks()
