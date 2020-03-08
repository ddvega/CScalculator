from setuptools import setup, find_packages

setup(name='tiny_calculator',
      version='1.0',
      description='A calculator for computer science students',
      url='',
      author='David Vega',
      packages=find_packages(),
      zip_safe=False,
      author_email='daviddvega@gmail.com',
      license='MIT',
      install_requires=['texteditor', 'numpy', 'PyQt5','PySide2', 'sip',
                        'pyperclip'])