import setuptools

setuptools.setup(
    name='pottery',
    version='0.0',
    author='Sravani',
    description='A small personalized website',
    packages =setuptools.find_packages(),
    # packages =['pottery'],
    include_package_data=True,
    install_requires=['flask','pymodm',],
)