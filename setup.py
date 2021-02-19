import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='kgbase',
    packages=['kgbase'],
    include_package_data=True,
    version='0.31',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kgbase',                   # Type in your name
    author_email='customersuccess@thinknum.com',      # Type in your E-Mail
    url='https://kgbase.com',
    download_url='https://github.com/thinknum/kgbase-client',
    keywords=['Kgbase', 'Thinknum', 'Alternative data', 'Data'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
