from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sample_package_abdullah',
    version='0.1.5',
    author='Abdullah Al Baki',
    author_email='abdullahalbaki009@gmail.com',
    description='A sample Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abdullahal-baki/sample_package',  #home page
    license='MIT', 
    packages=find_packages(include=['sample_package', 'sample_package.*']),
    install_requires=[
        'requests>=2.25.1',
    ],
    project_urls={
        "Source": "https://github.com/abdullahal-baki/sample_package",
        "Documentation": "https://github.com/abdullahal-baki/sample_package#readme",
        "Bug Tracker": "https://github.com/abdullahal-baki/sample_package/issues",
    },
)

