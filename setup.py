from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        return requirements


setup(
    name= "Earthquake predictin with Historic data",
    version = "0.0.1",
    author = "Rushikesh Wakhare",
    author_email = "rrushi6548@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
