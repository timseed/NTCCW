from setuptools import setup

setup(
    name='NTCCW',
    version='0.0.a',
    packages=['ham', 'ham.cw', 'ham.cw.ntcexam', 'tests'],
    url='https://github.com/timseed/NTCCW.git',
    license='GNU',
    author='tim seed',
    author_email='tim@sy-edm.com',
    description='Philippine NTC Cw Mock exam generator',
    install_requires=['numpy','scipy','daiquiri'],
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
            'recommonmark'
        ]
    }
)
