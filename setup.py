from setuptools import setup, find_packages

setup(
    name="medical_chatbot",  # Replace with your project name
    version="0.0.1",  # Version number
    author="Bablu kumar pandey",
    author_email="bablupandey446@gmail.com",
    description="A medical chatbot using Python",
    long_description=open("README.md").read(),  # Reads the project description from README.md
    long_description_content_type="text/markdown",
    url="https://github.com/Creator-Turbo/medical-chatbot",  # Replace with your repo URL
    packages=find_packages(),  # Automatically finds Python packages
    include_package_data=True,
   install_requires=[
        "sentence-transformers==2.2.2",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone-client",
        "langchain-pinecone",
        "langchain_community",
        # "langchain_experimental"
        "mistralai"  # Add Mistral AI package
    ],

#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",  # Minimum Python version required
)
