import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lisptick",
    version="0.1.0",
    author="Cedric Joulain",
    author_email="cedric.joulain@kereon-intelligence.com",
    description="LispTick Python client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kereon-intelligence/lisptick-client",
    project_urls={
        "Bug Tracker": "https://github.com/kereon-intelligence/lisptick-client/issues",
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
    ],
    packages=["lisptick"],
    python_requires='>=2.6'
)
