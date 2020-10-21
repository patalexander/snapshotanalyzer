from setuptools import setup

setup(
    name='snapshotanalyzer',
    version='0.1',
    author="Pat Alexander",
    author_email="patalexander71@gmail.com",
    description="Snapshotanalyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotan'],
    url="https://github.com/patalexander/snapshotanalyzer",
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        shotan=shotan.shotan:cli
    ''',
)
