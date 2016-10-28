from setuptools import setup

setup(
    name="lazy_paged_sequence",
    author="Misty De Meo",
    description=("Simple iterable interface to "
                 "paged data structures such as REST API clients"),
    author_email="mistydemeo@gmail.com",
    url='https://github.com/mistydemeo/lazy_paged_sequence',
    license="AGPL",
    version="0.3",
    py_modules=["lazy_paged_sequence"],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
