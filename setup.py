
from setuptools import setup, find_packages
setup(
    name='NTCCW',
    version='0.0.b',
    packages=find_packages(),
    url='https://github.com/timseed/NTCCW.git',
    license='GNU',
    author='tim seed',
    author_email='tim@sy-edm.com',
    description='Philippine NTC Cw Mock exam generator',
    install_requires=['numpy','scipy','daiquiri', 'm2r','python-Levenshtein'],
    #
    # Dev Requirements installed using this option
    # mkdir ./dev
    # pip install -e .["dev"]
    extras_require = {
        'dev': [
            'black',
            'pylint',
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'sphinx',
            'm2r',
            'recommonmark'
        ]
    }
)
