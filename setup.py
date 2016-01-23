from setuptools import setup


setup(
    name="sigma.standard",
    version="0.2.0a0",
    packages=["sigma", "sigma.standard"],
    namespace_packages=["sigma"],
    install_requires=["sigma.core"],
    extras_require={},
    zip_safe=True,
    package_data={
        "": ["*.txt", "*.rst", "*.md"]
    },
    author="Suzuki Shunsuke",
    author_email="suzuki.shunsuke.1989@gmail.com",
    description="Validation framework.",
    license="MIT",
    keywords="validation",
    url="https://github.com/pysigma/standard",
)
