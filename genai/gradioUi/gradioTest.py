import gradio as gr
import time

# Define a simple function
def myFunc(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]



#-----------
myInterface = gr.ChatInterface(
    myFunc,
    type="messages",
    chatbot=gr.Chatbot(height=300),
    
    title="Yes Man",
    description="Ask Yes Man any question",
    theme="ocean",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    
    multimodal=True,
    textbox = gr.MultimodalTextbox(placeholder="your question...", container=False, scale=7, sources=["microphone"]),

)

myInterface.launch()


# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot(type="messages")
#     msg = gr.Textbox()
#     clear = gr.ClearButton([msg, chatbot])

    

#     msg.submit(myFunc, [msg, chatbot], [msg, chatbot])
    

# demo.launch()


