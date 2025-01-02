from setuptools import find_packages,setup
from typing import List
#修改完代码要保存一下，然后再运行...傻了
HYPEN_E_DOT='-e .' 
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

    name='Project-ML',
    version='0.0.1',
    author='H-jianfei',
    author_email='xnm2580@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)