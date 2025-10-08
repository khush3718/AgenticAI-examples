# Technical Documentation for AgenticAI-examples

This document provides a more detailed technical overview of the projects within the `AgenticAI-examples` repository.

## Repository Structure

The repository is organized into four main project directories, each containing a distinct agentic AI application.

```
AgenticAI-examples/
├── agentic rag/
│   ├── client.py   
│   └── server.py
├── Document Compare/
│   └── VersionCompare.ipynb
├── documentation_writer/
│   └── DocumentAgent.ipynb
├── Travel Agent/
│   └── TravelAgent.ipynb
├── .gitignore
└── requirements.txt
```

## Project Details

### 1. Agentic RAG

-   **Technical Overview**: This project is a client-server application that implements a Retrieval-Augmented Generation (RAG) system. The `server.py` file likely sets up a FastAPI server to expose an API for the RAG agent. The `client.py` provides a command-line or programmatic interface to interact with the server. The `DOCS.md` and `README.md` files provide further details on the implementation and usage.

### 2. Document Compare

-   **Technical Overview**: This project uses a Jupyter Notebook (`VersionCompare.ipynb`) to perform a sophisticated comparison of two document versions. It leverages AI for semantic analysis and `difflib` for a technical diff. The notebook is well-structured, with cells for dependency installation, file uploading, content reading, AI-powered comparison, and report generation. The `DOCS.md` and `README.md` files offer comprehensive documentation.

### 3. Documentation Writer

-   **Technical Overview**: The `DocumentAgent.ipynb` notebook in this project is designed to function as an automated documentation generation agent. While the specifics of its implementation are contained within the notebook, it is expected to take a codebase as input and produce documentation as output, likely using a large language model.

### 4. Travel Agent

-   **Technical Overview**: The `TravelAgent.ipynb` notebook simulates a travel agent. This notebook likely contains code that interacts with external APIs (e.g., for flights, hotels) and uses a language model to provide a conversational interface for travel planning.

## Dependencies

The `requirements.txt` file at the root of the repository lists a large number of Python packages. This suggests that the projects share a common environment. Key dependencies include:

-   `fastapi`: For building the web server in the Agentic RAG project.
-   `langchain`, `openai`, `google-generativeai`: Core libraries for interacting with large language models.
-   `ipywidgets`, `jupyter`: For the interactive notebooks.
-   `python-docx`: For handling `.docx` files in the Document Compare project.

It is advisable to create a virtual environment and install these dependencies before running any of the projects.
