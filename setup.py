from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return the list of requirements
    """
    requirements_lst: List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #read file line by line
            lines= file.readlines()
            for line in lines:
               requirement= line.strip()
               #ignore empty lines and '-e .' 
               if requirement and requirement!='-e .':
                 requirements_lst.append(requirement)

    except FileNotFoundError :
        print("requirement.txt file is not found") 
    
    return requirements_lst



setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shobhit Kumar",
    author_email="shobhit9532@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements(),
    
)
        
