import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ArvanClient",
    version="0.0.2",
    author="Sajad Rahimi",
    author_email="rahimisajad@outlook.com",
    description="A Python SDK for ArvanCloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sajadrahimi/arvan-client",
    project_urls={
        "Bug Tracker": "https://github.com/sajadrahimi/arvan-client/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)