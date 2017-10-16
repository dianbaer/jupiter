from setuptools import setup

setup(name='fast_orm',
      version='1.0',
      description=("fast_orm"),
      long_description="fast_orm",
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
      url='https://github.com/dianbaer/fast',
      license='MIT',
      packages=['fast_orm'],
	  install_requires=["aiomysql"],  
      include_package_data=False)
