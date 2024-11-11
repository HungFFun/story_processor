from setuptools import setup, find_packages

setup(
    name="story_processor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'google-api-python-client==2.108.0',
        'google-auth-oauthlib==1.1.0',
        'openai==1.3.0',
        'python-dotenv==1.0.0',
        'moviepy==1.0.3',
        'pydub==0.25.1',
        'loguru==0.7.2',
        'pytest==7.4.3',
        'python-slugify==8.0.1',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for processing stories into videos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
) 