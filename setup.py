from setuptools import setup, find_packages

setup(
  name='kgbase-client',
  version='0.1.0',
  description='A kgbase client.',
  url='https://github.com/thinknum/kgbase-client.git',
  packages=['kgbase_client'],
  package_dir={
    'kgbase_client': 'kgbase_client',
  },
)