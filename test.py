from langchain_groq import ChatGroq
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate


app = FastAPI()
my_ai = ChatGroq(api_key= "PLACE_YOUR_API_KEY_HERE",model="openai/gpt-oss-120b")

class RequestChat(BaseModel):
    string: str

@app.post("/chat")
def chatendpoint(requestdata: RequestChat):
    # 1. Get the user's question from the API request
    user_query = requestdata.string
    
    # 2. Create our "Rulebook" for the AI
    system_rules = "You are a Mathematician. You only help solve complex Maths Questions. Don't reply to anything else. If asked about anything else, tell them calmly: 'I am not built for this.'"

    # 3. Create the Template combining the rules and the user's query
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_rules),
        ("human", "{user_input}") 
    ])
    
    # 4. Create the Chain: Template goes into the AI
    chain = prompt_template | my_ai

    # 5. Invoke the chain, passing the actual user query into the {user_input} blank space
    ai_response = chain.invoke({"user_input": user_query})
    
    # 6. Return the answer
    return {"output": ai_response.content}




