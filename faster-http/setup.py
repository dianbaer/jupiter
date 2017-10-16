import pathlib
import re

from setuptools import setup

here = pathlib.Path(__file__).parent

def read(name):
    fname = here / name
    with fname.open() as f:
        return f.read()


setup(name='faster-http',
      version='1.0',
      description=("faster-http"),
      long_description="faster-http",
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: AsyncIO',
      ],
      author='dianbaer',
      author_email='232365732@qq.com',
      url='https://github.com/dianbaer/faster',
      license='MIT',
      packages=['faster_http'],
	  install_requires=["aiohttp", "jinja2"],  
      include_package_data=False)
