# AI Math Teacher API

This is a FastAPI project that uses LangChain and Groq to create a role-specific AI assistant. 

### Features:
- Uses `ChatPromptTemplate` to enforce a strict "Math Teacher" persona.
- The AI will only answer complex math questions. 
- If asked about anything else (e.g., history, geography), it will politely decline to answer.

### How to run locally:
1. Clone this repository.
2. Install the requirements: `pip install -r requirements.txt`
3. Add your Groq API key inside the code (replace `"YOUR_API_KEY_HERE"`).
4. Start the server: `uvicorn test:app --reload` (Replace 'test' with your actual python file name).