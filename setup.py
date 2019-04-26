from setuptools import setup, find_packages


setup(
    name='mkdocs-git-committers-plugin',
    version='0.1.7',
    description='An MkDocs plugin to create a list of contributors on the page',
    long_description='The git-committers plugin will seed the template context with a list of github committers',
    keywords='mkdocs pdf github',
    url='https://github.com/byrnereese/mkdocs-git-committers-plugin/',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'PyGithub>=1.43',
        'mkdocs>=0.17'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'git-committers = mkdocs_git_committers_plugin.plugin:GitCommittersPlugin'
        ]
    }
)
