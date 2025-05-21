from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="job-application-tracker",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Automated tracking of job applications from email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/job-application-tracker",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-api-python-client>=2.0.0",
        "google-auth-oauthlib>=1.0.0",
        "google-auth-httplib2>=0.1.0",
        "pandas>=1.0.0",
        "openpyxl>=3.0.0",  # For Excel export
        "tqdm>=4.0.0",      # Progress bars
        "python-dateutil>=2.8.0"  # Date parsing
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-mock>=3.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0",  # Code formatting
            "mypy>=0.900"   # Type checking
        ],
    },
    entry_points={
        "console_scripts": [
            "py-job-tracker=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Job Seekers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)