import chainlit as cl
from textblob import TextBlob
from gpt4all import GPT4All

#
# Models available:
#   - ggml-mpt-7b-chat.bin
#   - ggml-gpt4all-j-v1.2-jazzy.bin
#   - ggml-vicuna-13b-1.1-q4_2.bin
#
# default model dir: /Users/pmui/Library/Application Support/nomic.ai/GPT4All/
#

gpt = GPT4All(model_name="ggml-mpt-7b-chat.bin")
# continuous on a loop
@cl.on_message
def main(message: str):
    
    # Your custom logic goes here...
    if "sentiment" in message:
        text = message[message.index("sentiment")+10:]
        print(f"sentiment of: {text}")
        blob = TextBlob(text)

        # Send a response back to the user
        cl.Message(
            content=f"sentiment: {blob.sentiment}",
        ).send()
 
    else:
        # LLM 
        response = gpt.chat_completion([{
            "role": "assistant",
            "content": message
        }])
        result = response["choices"][0]["message"]["content"]
        cl.Message(
            content=f"{result}",
        ).send()

@cl.on_chat_start
def start():
    cl.Message(
        content=f"Hello there!"
    ).send()


    # file = None
    # # Wait for the user to upload a file
    # while file == None:
    #     file = cl.AskFileMessage(
    #         content="Please upload a text file to begin!", accept=["text/plain"]
    #     ).send()
    # # Decode the file
    # text = file.content.decode("utf-8")
    # # Let the user know that the system is ready
    # cl.Message(
    #     content=f"`{file.name}` uploaded, it contains {len(text)} characters!"
    # ).send()

