from setuptools import setup

setup(name='ripper',
      version='0.0.1',
      description='Image Ripper for the Pythonic Soul',
      url='http://github.com/kevinaloys/ripper',
      author='Kevin Aloysius',
      author_email='kevinaloysius25@gmail.com',
      license='MIT',
      packages=['ripper'],
      install_requires=['requests','BeautifulSoup4'],
      zip_safe=False
     )