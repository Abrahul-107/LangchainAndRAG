# LangchainAndRAG
An exploration of LangChain and RAG (Retrieval-Augmented Generation) for building intelligent applications
# LangchainAndRAG

An exploration of LangChain and RAG (Retrieval-Augmented Generation) for building intelligent applications. This repository includes a Streamlit app that generates restaurant names and menu items based on given recipes using LangChain with Together AI.

## Requirements

- Python 3.12
- Docker (for containerized deployment)
- Together AI API Key

## Installation

### Local Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/LangchainAndRAG.git
   cd LangchainAndRAG

2. Create a virtual environment and activate it:
    ```sh
    python3.12 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the required packages:

    ```sh
    pip install --upgrade pip
    pip install -r requirements.txt

4. Create a .env file in the project root and add your Together AI API key:

    ```sh
    echo "API_KEY=your_actual_api_key_here" > .env
5. Run the Streamlit app:

    ```sh
    streamlit run 01_langchainstreamlit.py
5. Docker Setup
    - Build the Docker image:
    ```sh
    docker build -t streamlit-langchain-app .
    ```
    - Run the Docker container:
    ```sh
    docker run -p 8501:8501 -e API_KEY=your_actual_api_key_here 
    ```
    - streamlit-langchain-app.py.

## Usage
Streamlit App
Open your web browser and go to http://localhost:8501.

- Enter a recipe in the text input field (e.g., "dal").

- Click the "Generate" button to see the generated restaurant names and suggested menu items.

