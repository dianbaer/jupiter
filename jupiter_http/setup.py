from setuptools import setup

setup(name='jupiter_http',
      version='1.0',
      description=("jupiter_http"),
      long_description="jupiter_http",
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
      url='https://github.com/dianbaer/jupiter',
      license='MIT',
      packages=['jupiter_http'],
	  install_requires=["aiohttp", "jinja2"],  
      include_package_data=False)
