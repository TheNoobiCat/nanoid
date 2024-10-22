from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='python-nanoid',
    version='2.0.0',
    author='TheNoobiCat',
    author_email='127432361+TheNoobiCat@users.noreply.github.com',
    description='A tiny, secure, URL-friendly, unique string ID generator for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/thenoobicat/python-nanoid',
    license='MIT',
    packages=['nanoid'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    # removed zipsafe
)
