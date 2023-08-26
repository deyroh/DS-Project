from setuptools import find_packages,setup
from typing import List

Hypen_edot="-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_edot in requirements:
            requirements.remove(Hypen_edot)
    
    return requirements

setup(
    name='Rohan',
    version=0.01,
    author_email='deyroh777@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)