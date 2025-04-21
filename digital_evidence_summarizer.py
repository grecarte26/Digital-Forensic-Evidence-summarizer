import os
import openai
import gradio as gr
from dotenv import load_dotenv

# 🔐 Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please define it in your .env file.")

client = openai.OpenAI(api_key=api_key)

# 🧠 Generate GPT prompt based on mode
def generate_prompt(text, mode):
    if mode == "FTK Imager":
        prompt = (
            "You are a digital forensic analyst reviewing evidence extracted using FTK Imager.\n"
            "Evaluate the files and metadata below. Identify any significant digital artifacts, potential user activity,\n"
            "and summarize the findings in a format suitable for inclusion in a forensic report.\n\n"
            f"FTK Evidence:\n\"\"\"\n{text}\n\"\"\""
        )
    elif mode == "Autopsy":
        prompt = (
            "You are a forensic analyst reviewing a digital timeline and metadata exported from Autopsy.\n"
            "Identify key user actions, important file events, keyword hits, or anomalies.\n"
            "Create a clear chronological summary suitable for an investigative report.\n\n"
            f"Autopsy Evidence:\n\"\"\"\n{text}\n\"\"\""
        )
    else:  # General
        prompt = (
            "You are a digital forensic analyst. Review the following notes, metadata, and file information.\n"
            "Summarize the findings as if preparing a report for a legal or investigative audience. Be clear and concise.\n\n"
            f"Evidence:\n\"\"\"\n{text}\n\"\"\""
        )
    return prompt

# 📄 Process evidence with GPT
def summarize_evidence(text, mode):
    prompt = generate_prompt(text, mode)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# 📁 Handle text + file upload and apply selected mode
def summarize_combined(text, file, mode):
    if file is not None:
        content = file.read()
        text += "\n" + content.decode("utf-8")
    return summarize_evidence(text, mode)

# 📊 Gradio UI with mode selection
interface = gr.Interface(
    fn=summarize_combined,
    inputs=[
        gr.Textbox(lines=20, label="📋 Paste Digital Evidence (or leave blank if uploading file)"),
        gr.File(label="📎 Upload .txt or .csv file", file_types=[".txt", ".csv"]),
        gr.Radio(label="🔍 Choose Analysis Mode", choices=["General", "FTK Imager", "Autopsy"], value="General")
    ],
    outputs=gr.Textbox(label="📑 Summarized Forensic Report"),
    title="Digital Evidence Summarizer",
    description="Paste or upload raw digital evidence or notes. Choose a mode to guide how the report is generated."
)

# 🚀 Launch app
interface.launch()
