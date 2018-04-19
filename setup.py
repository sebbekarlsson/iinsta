from setuptools import setup


setup(
    name='iinsta',
    version='1.0',
    install_requires=[
        'pymongo',
        'mongoengine',
        'bcrypt',
        'flask_assets',
        'jsmin',
        'wtforms',
        'flask'
    ],
    packages=[
        'iinsta'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
