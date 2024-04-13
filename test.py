from uagents import Agent, Context
import google.generativeai as genai
import requests

        
alice = Agent(name="alice",  port=8000,
    seed="alice secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],)
    

# list = ["i am happy","i am sad","ok"]


# Prints the unique address of the agent
#used to identitfy the agent on fetch network
print("uAgent address: ", alice.address)

# Network Adddress
print("Fetch network address: ", alice.wallet.address())


genai.configure(api_key="AIzaSyB0CxS1AjgcQUb2QEMvASd60854XKrSBCY")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

convo = model.start_chat(history=[])
	
# Runs Only on start up
@alice.on_event("startup")
async def say_hello(ctx: Context):
    # Set up the model
    print("Start")
        
    
@alice.on_interval(period=2)
async def loop(ctx:Context):
    textIn = input()
    convo.send_message(textIn)
    print(convo.last.text)

if __name__ == "__main__":
    alice.run()
