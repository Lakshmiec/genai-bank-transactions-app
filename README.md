# genai_app-for-bank_transactions
## Instructions to Run the Submission

Below are the step-by-step instructions to set up and run the code for asking questions about transactions:
### Project Directory

├── .env <br> 
├── chat_completion.py <br>
├── data_retriever.py<br>
├── data.csv<br>
├── date_query_templates.py<br>
├── intent_handlers.py<br>
├── main.py<br>
├── README.md<br>
└── requirements.txt<br>
### Prerequisites
- Ensure you have Python and the required dependencies installed. 
- The dependencies are listed in requirements.txt.

### Steps:

1. **Clone the Repository:**

- Download or clone the repository to your local machine.

2. **Install Dependencies:**
- Navigate to the project directory:

```bash
cd path/to/project

```
- Install the required dependencies
```bash
pip install -r requirements.txt

```
- Set up environment variables:
   - Create a .env file in the root directory of your project.
   - Acquire an API key through makersuite.google.com and put it in .env file:

  ```toml
  GEMINI_API_KEY = "your-google-api-key"
  ```

3. **Run the Application:**

- Run the Streamlit app by executing the main script:

    ```bash
    streamlit run main.py
    ```

### How to Interact with the QA System

**Ask a Question**: <br>
    - Enter your queries related to your transactional data in the text input field and click on enter <br>
    - The system will display the answer fetched from the transactional data using the LLM Prompts. <be>

<img width="1432" alt="Screenshot" src="https://github.com/Lakshmiec/genai_app-for-bank_transactions/blob/main/App_image.png">
