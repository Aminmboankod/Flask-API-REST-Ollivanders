from setuptools import find_packages, setup


package_data = {"": ["README.md"]}

setup(
    name="Flask-API-REST-Ollivanders",
    version="1.0",
    description="RESTful basic of Ollivanders shops",
    author="Aminmboankod",
    author_email="amustafaboankod@cifpfbmoll.eu",
    url="https://github.com/Aminmboankod/Flask-API-REST-Ollivanders",
    packages=find_packages(),
    package_data=package_data,
    install_requires = [
            'attrs==22.2.0',
            'certifi==2022.12.7',
            'charset-normalizer==3.1.0',
            'click==8.1.3',
            'coverage==7.2.1',
            'exceptiongroup==1.1.1',
            'Flask==2.2.3',
            'idna==3.4',
            'iniconfig==2.0.0',
            'itsdangerous==2.1.2',
            'Jinja2==3.1.2',
            'MarkupSafe==2.1.2',
            'packaging==23.0',
            'pluggy==1.0.0',
            'pytest==7.2.2',
            'requests==2.28.2',
            'tomli==2.0.1',
            'urllib3==1.26.15',
            'Werkzeug==2.2.3',
    ],
    entry_points={"console_scripts": ["my-App = app:run"]},
    
)



