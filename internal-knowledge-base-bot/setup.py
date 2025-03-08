from setuptools import setup, find_packages

setup(
    name='internal-knowledge-base-bot',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A multilingual chat bot for internal knowledge management using GPT and MongoDB.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'streamlit',
        'pymongo',
        'torch',  # Assuming PyTorch is used for CUDA support
        'transformers',  # Assuming Hugging Face Transformers for GPT
        'numpy',  # Commonly used for numerical operations
        'pandas'  # Useful for data manipulation
    ],
    python_requires='>=3.7',
)