from setuptools import setup, find_packages

setup(
    name="library-pengolah-data",  
    version="0.1.0",  
    description="Library pengolah data python",  
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/Dwi-Wahyu/library-pengolah-data.git",  
    author="Kelompok 1",  
    author_email="",
    license="MIT",  
    packages=find_packages(),  
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)
