import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.ProgramRunnerEpew import ProgramRunnerEpew


def run_dockerfile_example_in_common_project_structure(current_file: str, verbosity: int = 3, remove_old_container: bool = False):
    folder = os.path.dirname(current_file)
    example_name = os.path.basename(folder)
    GeneralUtilities.write_message_to_stdout(f"Run {example_name}-example ")
    sc = ScriptCollectionCore()
    oci_image_artifacts_folder = GeneralUtilities.resolve_relative_path("../../Artifacts/BuildResult_OCIImage", folder)
    image_filename = os.path.basename(sc.find_file_by_extension(oci_image_artifacts_folder, "tar"))
    codeunit_name = os.path.basename(GeneralUtilities.resolve_relative_path("../../..", folder))
    codeunit_name_lower = codeunit_name.lower()
    if remove_old_container:
        GeneralUtilities.write_message_to_stdout(f"Ensure container {codeunit_name_lower} does not exist...")
        sc.run_program("docker", f"container rm -f {codeunit_name_lower}", oci_image_artifacts_folder)
    GeneralUtilities.write_message_to_stdout("Load docker-image...")
    sc.run_program("docker", f"load -i {image_filename}", oci_image_artifacts_folder)
    project_name = f"{codeunit_name}_{example_name}".lower()
    sc.program_runner = ProgramRunnerEpew()
    GeneralUtilities.write_message_to_stdout("Start docker-container...")
    sc.run_program("docker-compose", f"--project-name {project_name} up", folder, verbosity)


def run_example():
    run_dockerfile_example_in_common_project_structure(str(Path(__file__).absolute()), 3, True)


if __name__ == "__main__":
    run_example()
