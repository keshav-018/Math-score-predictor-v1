from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(filepath: str) -> List[str]:
    with open(filepath) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject1',
    version='0.0.1',
    author='Keshav Gupta',
    author_email='keshav10017@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)