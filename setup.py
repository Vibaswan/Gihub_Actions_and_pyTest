import setuptools

setuptools.setup(
    name='Gihub_Actions_and_pyTest',
    version='1.0.2',
    packages=setuptools.find_packages(),
    url='https://github.com/Vibaswan/Gihub_Actions_and_pyTest',
    license='MIT',
    author='vhowdhur',
    author_email='vroychowdhury@gmail.com',
    description='just a fun project to learn github actions and pytest',
    tests_require=['pytest'],
    setup_requires=['pytest-runner']
)
