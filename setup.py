import setuptools

version = '0.1.1'

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rephunt',
    version=version,
    author='stefanitsky',
    author_email='stefanitsky.mozdor@google.com',
    description='Reputation enhancer for Stack Exchange',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Stefanitsky/rephunt',
    packages=['rephunt'],
    keywords='stackexchange stackoverflow reputation enhance raise up',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Utilities'
    ],
    project_urls={
        'Documentation': 'https://github.com/Stefanitsky/rephunt/wiki',
        'Say Thanks!': 'https://saythanks.io/to/Stefanitsky',
        'Source': 'https://github.com/Stefanitsky/rephunt',
        'Tracker': 'https://github.com/Stefanitsky/rephunt/issues',
    },
)