import os
from setuptools import setup, find_packages

def readme() -> str:
    """Reads the README.md for long_description."""
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.1.0',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.description }}',
    long_description=readme(),
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    license='MIT',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
