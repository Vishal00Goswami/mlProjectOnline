from setuptools import setup, find_packages
from typing import List 

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements 

setup(
    name = "ML_Project_DS",
    version = "0.0.1",
    packages = find_packages(),
    author = "Your name",
    author_email = "Your mail",
    isntall_requies= get_requirements('requirements.txt')
)