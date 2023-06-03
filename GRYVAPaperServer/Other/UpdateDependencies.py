import requests
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure
from selenium import webdriver
import time
import re


def get_rendered_website(url: str, duration_in_seconds: int = 2) -> str:
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(duration_in_seconds)
    htmlSource = driver.page_source
    return htmlSource


def get_latest_paper_version() -> str:
    sc = ScriptCollectionCore()
    website_content = get_rendered_website("https://papermc.io/downloads/paper")
    regex = '\\"https\\:\\/\\/api\\.papermc\\.io\\/v2\\/projects\\/paper\\/versions\\/(\\d+\.\\d+\\.\\d+)\\/builds\\/(\\d+)\\/downloads\\/paper-\\d+\\.\\d+\\.\\d+-\\d+\\.jar\\"'
    result = re.compile(regex).search(website_content)
    version = result.groups(0)[0]
    build = result.groups(0)[1]
    return f"{version};{build}"


def update_dependencies():
    script_file = str(Path(__file__).absolute())
    TasksForCommonProjectStructure().update_dependency_in_resources_folder(script_file, "Paper", get_latest_paper_version())


if __name__ == "__main__":
    update_dependencies()
