from setuptools import setup

setup(
    name="realpython-reader",
    version="0.1",
    description="Read the latest Real Python tutorials",
    # long_description=README,
    # long_description_content_type="text/markdown",
    # url="https://github.com/realpython/reader",
    # author="Real Python",
    # author_email="info@realpython.com",
    # license="MIT",
    classifiers=[
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["translator"],
    include_package_data=True,
    entry_points={"console_scripts": ["translator=translator.__main__:main"]},
)