from setuptools import setup, find_packages

setup(
    name='pyqt-transparent-centralwidget-window',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt window which can set the QMainWindow '
                'as main widget and make central widget of QMainWindow transparent. '
                'Simply put, frame with no image',
    url='https://github.com/yjg30737/pyqt-transparent-centralwidget-window.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main',
        'pyqt-top-titlebar-widget @ git+https://git@github.com/yjg30737/pyqt-top-titlebar-widget.git@main'
    ]
)