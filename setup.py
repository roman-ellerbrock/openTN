from setuptools import setup, find_packages

setup(
    name='openTN',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/roman-ellerbrock/openTN',
    license='MIT',
    author='Roman Ellerbrock',
    author_email='romanellerbrock@gmail.com',
    description='A Python package for implementing MERA',
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        # add any additional dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    
)

