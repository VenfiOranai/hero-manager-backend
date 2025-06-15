from setuptools import setup


setup(
    name='hero_manager',
    version='1.0.0',
    description='Hero manager backend',
    author='America',
    install_requires=[
        'sqlalchemy==1.4.54',
        'flask==2.2.2',
        'Flask-RESTful',
        'Flask-API',
        'pydantic',
        'werkzeug==2.2.2',
    ]
)
