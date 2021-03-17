from setuptools import setup

setup(
    name="ptmcmcsampler",
    version="2.0.0",
    author="Justin A. Ellis",
    author_email="justin.ellis18@gmail.com",
    packages=["PTMCMCSampler"],
    package_dir={"PTMCMCSampler": "PTMCMCSampler"},
    url="https://github.com/jellis18/PTMCMCSampler",
    license="MIT",
    zip_safe=False,
    description="Parallel tempering MCMC sampler written in Python",
    long_description=open("README.md").read() + "\n\n" + "---------\n\n" + open("HISTORY.md").read(),
    long_description_content_type="text/markdown",
    package_data={"": ["README.md", "HISTORY.md"]},
    install_requires=["numpy>=1.16.3", "scipy>=1.2.0"],
    python_requires=">=3.6",
    extras_require={"mpi": ["mpi4py>=3.0.3"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
