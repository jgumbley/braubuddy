from setuptools import setup, find_packages

setup(
    name='braubuddy',
    version='0.4.2',
    author='James Stewart',
    author_email='jstewart101@gmail.com',
    description='An extensile temperature management framework.',
    long_description=open('README.rst').read(),
    license='LICENSE.txt',
    packages=find_packages(),
    url='http://braubuddy.org/',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'braubuddy = braubuddy.runserver:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
