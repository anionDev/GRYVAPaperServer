import sys
import os
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.GeneralUtilities import GeneralUtilities


def run_dockerfile_example_in_common_project_structure(current_file: str):
    folder = os.path.dirname(current_file)
    example_name = os.path.dirname(folder)
    sc = ScriptCollectionCore()
    oci_image_artifacts_folder = GeneralUtilities.resolve_relative_path("../../../Artifacts/BuildResult_OCIImage", folder)
    image_filename = os.path.basename(sc.find_file_by_extension(oci_image_artifacts_folder, "tar"))
    codeunit_name = os.path.basename(GeneralUtilities.resolve_relative_path("../../../..", folder))
    sc.run_program("docker", f"load -i {image_filename}", oci_image_artifacts_folder)
    sc.run_program("docker-compose", f"--project-name {codeunit_name}_{example_name} up", folder)


def run_example():
    run_dockerfile_example_in_common_project_structure(str(Path(__file__).absolute()))


if __name__ == "__main__":
    run_example()
