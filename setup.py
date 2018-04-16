from setuptools import setup


setup(
    name='iinsta',
    version='1.0',
    install_requires=[
        'bcrypt',
        'flask_assets',
        'jsmin',
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
