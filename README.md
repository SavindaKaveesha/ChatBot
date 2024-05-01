# Chatbot

This is a simple chatbot implemented in Python that uses a JSON file as a database to store questions and their corresponding answers. The chatbot leverages the `difflib` library to find the best matching question from the database and provides an appropriate response.

## Features

- **JSON Database:** Questions and answers are stored in a JSON file for easy management.
- **Text Matching:** Uses `get_close_matches` from `difflib` to find the best matching question from the database.
- **Dynamic Learning:** Allows users to teach the chatbot new questions and answers during interactions.

## Technical Details

- **Programming Language:** Python
- **Libraries Used:** `json`, `difflib`
- **Functionality:**
  - `load_database(file_path:str) -> dict`: Loads the JSON database file into the program.
  - `save_database(file_path:str,data) -> dict`: Saves data back to the JSON database file.
  - `find_best_ans(user_question:str,questions:list[str]) -> str | None`: Finds the best matching answer for a given question.
  - `get_ans_for_question(question: str, database:dict) -> str | None`: Retrieves the answer for a specific question from the database.
  - `chatBot()`: Implements the chatbot functionality using the loaded database.

## Usage

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/simple-chatbot.git
   ```

2. Run the Chatbot:
   - Ensure you have Python installed on your system.
   - Navigate to the project directory and run `python chatbot.py`.

3. Interact with the Chatbot:
   - Enter your questions to interact with the chatbot.
   - Type "quit" to exit the chatbot.

4. Teach the Chatbot:
   - If the chatbot doesn't know the answer, it will prompt you to teach it.
   - Enter the question and its corresponding answer to teach the chatbot.

## Database Structure

The JSON database file (`database.json`) contains a list of questions and answers in the following format:

```json
{
  "questions": [
    {
      "questions": "hi",
      "answer": "hello!"
    },
    {
      "questions": "how are you? ",
      "answer": "I am fine, How are you? "
    },
    ...
  ]
}
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.
