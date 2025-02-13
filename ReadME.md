# Gemini AI Chat Application

This is a simple Generative AI application using Google's Gemini Pro model and Gradio for the user interface.

## Files and Directories

- `.env`: Environment variables file. Add your API keys and other sensitive information here.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `.gradio/`: Contains Gradio-related files.
- `.qodo/`: Contains Qodo-related files.
- `app.py`: Main application file.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies file.

## Prerequisites

- Python 3.10 or higher(It is for gradion )
- Docker (optional, for containerized deployment)
- Git (optional, for version control)

## Setup

### Clone the Repository

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Rhushya/GenAI_Gemini_template
    cd gemini-app
    ```

### Create a Virtual Environment

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

### Install Dependencies

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Set Up Environment Variables

4. **Set up environment variables:**

    Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your Gemini API key:

    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Running the Application

### Run Locally

1. **Run the application locally:**

    ```sh
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

### Run Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t gemini-app .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 5000:5000 gemini-app
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Enter your prompt in the input textbox.
3. Click the "Submit" button to generate a response using the Gemini Pro model.

## Extending the Application

You can extend this application by adding more features or integrating with other APIs. Here are some ideas:

- Add more input fields for additional context.
- Integrate with other AI models.
- Add user authentication.
- Deploy the application to a cloud platform.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Gradio](https://gradio.app/)
- [Google Generative AI](https://ai.google/tools/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

Happy coding!
