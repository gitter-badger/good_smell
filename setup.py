import sys
from pathlib import Path

from setuptools import setup

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner==4.2'] if needs_pytest else []
long_description = Path("README.md").read_text()

setup(
    name='good_smell',
    version='0.1',
    author="Tomer Keren",
    author_email="tomer.keren.dev@gmail.com",
    description="A linter/refactoring tool to make you code smell better!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
    ],
    py_modules=['good_smell'],
    install_requires=[
        'fire==0.1.3',
        'astor==0.7.1',
    ],
    setup_requires=[] + pytest_runner,
    tests_require=['pytest==4.0.1',
                   'mccabe==0.6.1', 'pytest-mccabe==0.1',
                   'autopep8==1.4.3'],
    entry_points={
        'console_scripts': [
            'good_smell=good_smell:main'
        ]
    }
)
