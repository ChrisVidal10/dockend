from distutils.core import setup
import setuptools

setuptools.setup(
    name='dockend',
    version='0.1.2',
    author='Christian Vidal',
    author_email='chris.vidal10@gmail.com',
    url='http://pypi.python.org/pypi/dockend/',
    packages=setuptools.find_packages(),
    description='Change backend for BYR-Microservices and DLA-backend-services',
    install_requires=[
        "docker>=3.4.0",
        "termcolor>=1.1.0"
    ],
    entry_points={
        'console_scripts': [
            'dockend = dockend.dockend:main',
        ],
    }
)
