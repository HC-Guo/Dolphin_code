#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

# Read requirements from file
def read_requirements():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Read long description from README
def read_long_description():
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    return ""

setup(
    name="dolphin-ultrasound",
    version="0.1.0",
    description="Dolphin Ultrasound: A Large Language Model for Medical Ultrasound Analysis with Two-Stage Training",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="DolphinAI Team",
    author_email="contact@dolphinai.com",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=read_requirements(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    keywords="ultrasound, medical AI, large language model, multimodal, fine-tuning, reinforcement learning",
)