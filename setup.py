from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='gan_art',
      version="1.0",
      description="Project Description",
      # packages=find_packages(),
      packages=requirements,
      # test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      # scripts=['scripts/STOCK_PREDICT-run'],
      zip_safe=False)
