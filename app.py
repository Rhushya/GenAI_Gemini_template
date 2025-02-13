import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# Create Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt here...", label="Input"),
    outputs=gr.Textbox(label="Generated Response", lines=6),
    title="🧠 Gemini AI Chat",
    description="A simple Generative AI app using Google's Gemini Pro model",
    flagging_mode="never"  # This replaces the deprecated allow_flagging parameter
)

if __name__ == "__main__":
    # Run locally without share
    interface.launch(server_name="127.0.0.1", server_port=5000, share=True)