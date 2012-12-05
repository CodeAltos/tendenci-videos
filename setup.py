from setuptools import setup, find_packages

longdesc = \
'''
An addon for Tendenci for displaying videos.
'''

setup(
    name='videos',
    author='John-Michael Oswalt',
    author_email='jmoswalt@schipul.com',
    version='1.0.1',
    license='',
    description='An addon for Tendenci for displaying embedded videos.',
    long_description=longdesc,
    url='https://github.com/tendenci/tendenci-videos',
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=['tendenci>=5.1'],
)
