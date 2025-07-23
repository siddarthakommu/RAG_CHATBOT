from agents.message_protocol import MCPMessage
import uuid
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  

class LLMResponseAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def respond(self, message):
        trace_id = str(uuid.uuid4())
        context = "\n".join(message.payload["retrieved_context"])
        query = message.payload["query"]
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        response = self.model.generate_content(prompt)
        return MCPMessage(
            sender="LLMResponseAgent",
            receiver="UI",
            type_="FINAL_RESPONSE",
            trace_id=trace_id,
            payload={
                "answer": response.text,
                "sources": context
            }
        )
