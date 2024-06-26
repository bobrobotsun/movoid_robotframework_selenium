from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='movoid_robotframework_selenium',
    version='1.2.9.001',
    packages=find_packages(),
    url='',
    license='',
    author='movoid',
    author_email='bobrobotsun@163.com',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['selenium==4.6.0',
                      'movoid_function',
                      'movoid_robotframework',
                      'robotframework_selenium2library',
                      'movoid_package',
                      'opencv-python',
                      ],
)
