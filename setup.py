from setuptools import setup, find_packages

setup(
    name='wordle',
    version='1.0',
    author='chriskr',
    description='Utility to solve wordles',
    packages=find_packages(),
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'wordle = src.wordle:main_func'
        ],
    },
    package_data={
        "": ["*.txt"],
    },
    python_requires='>=3.5'
)
