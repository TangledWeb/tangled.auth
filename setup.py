from setuptools import setup, find_packages


setup(
    name='tangled.auth',
    version='0.1a1',
    description='Tangled auth integration',
    url='http://tangledframework.org/',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    packages=find_packages(),
    install_requires=(
        'tangled.web>=0.1.dev0',
    ),
    extras_require={
        'dev': (
            'tangled[dev]',
        ),
    },
    entry_points="""
    [tangled.scripts]
    auth = tangled.auth.command:Command

    """,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ),
)
