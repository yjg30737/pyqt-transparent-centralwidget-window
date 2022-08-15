from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-transparent-centralwidget-window',
    version='0.0.12',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt window which can set the QMainWindow '
                'as main widget and make central widget of QMainWindow transparent. '
                'Simply put, frame with no image',
    url='https://github.com/yjg30737/pyqt-transparent-centralwidget-window.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-custom-titlebar-window>=0.0.1'
    ]
)