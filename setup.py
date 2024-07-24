from setuptools import setup, find_packages

setup(
    name='conger',
    version='0.1',
    description='A simple terminal library for creating console-based applications.',
    author='Nub4ikgame',
    author_email='cindaevila@gmail.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'conger=conger:main',  # Assuming `main()` is a function in conger.py
        ],
    },
)
