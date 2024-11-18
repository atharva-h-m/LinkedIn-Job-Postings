from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of the packages defined in requirements.txt
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="LinkedIn_Job_Postings_ML",
    version="1.0.0",
    author="Atharva Malandkar",
    author_email="atharva.h.malandkar@gmail.com",
    url="https://github.com/atharva-h-m/LinkedIn_Job_Postings_ML",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
