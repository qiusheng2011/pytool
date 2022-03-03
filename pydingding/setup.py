import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydingding",
    version="0.0.2",
    author="gxz",
    author_email="137812291@qq.com",
    description="钉钉开放功能对接使用库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.dingding.com",
    project_urls={},
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
     
)