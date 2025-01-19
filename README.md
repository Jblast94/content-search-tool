# Comprehensive Search Tool

This project is a comprehensive search tool that allows users to search for information across various sources, including public records, social media platforms, online directories, and dark web databases.

## Features

- Search across multiple sources
- User-friendly GUI built with Tkinter
- Error handling and logging
- Dockerized for easy deployment

## Requirements

- Python 3.9
- Docker
- The following Python packages:
  - requests
  - beautifulsoup4
  - selenium

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Jblast94/content-search-tool.git
    cd content-search-tool
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have Docker installed and running.

## Running the Application

### Locally

1. Run the Python script:
    ```sh
    python main.py
    ```

### Using Docker

1. Build the Docker image:
    ```sh
    docker build -t content-search-tool .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8080:8080 content-search-tool
    ```

## Usage

1. Enter your search query in the input field.
2. Click the "Search" button.
3. View the search results in the new window.

## License

This project is licensed under the MIT License.
