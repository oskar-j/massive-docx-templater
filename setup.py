import setuptools
from massive_docx.version import Version


setuptools.setup(name='massive_docx',
                 version=Version('1.0.0').number,
                 description='Python Package Boilerplate',
                 long_description=open('README.md').read().strip(),
                 author='Oskar Jarczyk',
                 author_email='oskar.jarczyk@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['massive_docx'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='boilerplate package',
                 classifiers=['Packages', 'Boilerplate'])
