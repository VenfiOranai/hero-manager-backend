from setuptools import setup


setup(
    name='hero_manager',
    version='1.0.0',
    description='Hero manager backend',
    author='America',
    install_requires=[
        'sqlalchemy==1.4.54',
        'flask',
        'Flask-RESTful',
        'Flask-API',
    ]
)
