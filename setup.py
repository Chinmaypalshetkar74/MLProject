from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """This function returns a list of requirements."""
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Chinmay",
    author_email="chinmaypalshetkar30@gmail.com",
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=get_requirements("requirements.txt"),
)
