from setuptools import setup

setup(name='pycon-tutorial-steve98654',
      version = '0.1',
      description='test proj',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
        'pytest-runner',
      ],
      test_require=[
        'pytest',
      ]
      )
        
