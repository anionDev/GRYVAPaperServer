import sys
import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure
import re


def standardized_tasks_update_version_in_docker_examples(file, codeunit_version):
    folder_of_current_file = os.path.dirname(file)
    codeunit_folder = GeneralUtilities.resolve_relative_path("..", folder_of_current_file)
    codeunit_name = os.path.basename(codeunit_folder)
    codeunit_name_lower = codeunit_name.lower()
    examples_folder = GeneralUtilities.resolve_relative_path("Other/Examples", codeunit_folder)
    for example_folder in GeneralUtilities.get_direct_folders_of_folder(examples_folder):
        docker_compose_file = os.path.join(example_folder, "docker-compose.yml")
        if os.path.isfile(docker_compose_file):
            filecontent = GeneralUtilities.read_text_from_file(docker_compose_file)
            replaced = re.sub(f'image:\\s+[\'"]{codeunit_name_lower}:\\d+\\.\\d+\\.\\d+[\'"]', f'image: "{codeunit_name_lower}: {codeunit_version}"', filecontent)
            GeneralUtilities.write_text_to_file(docker_compose_file, replaced)


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
    sc.replace_version_in_dockerfile_file(GeneralUtilities.resolve_relative_path(f"../{codeunitname}/Dockerfile", folder_of_current_file), codeunit_version)
    t.standardized_tasks_do_common_tasks(file, codeunit_version, verbosity, targetenvironmenttype, True, additional_arguments_file, cmd_args)
    standardized_tasks_update_version_in_docker_examples(file, codeunit_version)


if __name__ == "__main__":
    common_tasks()
