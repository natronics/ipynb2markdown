from distutils.core import setup

setup(
    name='ipynb2markdown',
    version='0.1',
    description='A simple IPython Notebook to markdown converter. Works well for embedding IPython Notebooks into jekyll sites like github pages',
    author='Nathan Bergey',
    author_email='nathan.bergey@gmail.com',
    url='https://github.com/natronics/ipynb2markdown',
    scripts = [
        'scripts/ipynb2markdown'
    ]
)
