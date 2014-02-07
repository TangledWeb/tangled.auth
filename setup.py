from setuptools import setup


setup(
    name='tangled.auth',
    version='0.1a3.dev0',
    description='Tangled auth integration',
    long_description=open('README.rst').read(),
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=[
        'tangled',
        'tangled.auth',
        'tangled.auth.tests',
    ],
    install_requires=[
        'tangled.web>=0.1.dev0',
    ],
    extras_require={
        'dev': [
            'tangled[dev]',
        ],
    },
    entry_points="""
    [tangled.scripts]
    auth = tangled.auth.command:Command

    """,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
