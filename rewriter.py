from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

tone = input("Tone (professional/friendly/short): ") or "professional"
text = input("Message: ")

reply = llm.invoke(f"Rewrite this message in a {tone} tone. Keep the meaning. Return only the rewritten text.\n\n{text}")
print("\n" + reply.content)
