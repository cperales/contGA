from setuptools import setup

setup(
    name='contGA',
    description='Continuous Genetic Algorithm',
    version='0.1',
    author='Javier Perez-Rodriguez, Carlos Perales-Gonzalez',
    author_email='cperales@uloyola.es',
    packages=['contGA',
              ],
    zip_safe=False,
    install_requires=['numpy',
                      'matplotlib'],
    include_package_data=True,
    setup_requires=[],
    tests_require=[]
)
