import illumiprocessor
from distutils.core import setup

setup(
        name='illumiprocessor',
        version='2.0.1',
        description='Automated Illumina read trimning using trimmomatic',
        url='https://github.com/faircloth-lab/illumiprocessor',
        author='Brant C. Faircloth',
        author_email='borg@faircloth-lab.org',
        license='BSD',
        platforms='any',
        packages=[
            'illumiprocessor'
        ],
        scripts=[
            'bin/illumiprocessor'
        ]
    )