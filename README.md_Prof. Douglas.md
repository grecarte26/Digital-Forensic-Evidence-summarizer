# 🧠 Digital Evidence Summarizer (GPT-4)
Created by **Jerson Recarte** for **Prof. Douglas** as part of a digital forensics project.

## 📝 Project Overview
This tool allows users to input or upload digital forensic evidence (e.g., carved file notes, metadata, listings)
and receive an automated summary suitable for forensic reports using GPT-4.

## 🚀 Features
- Paste raw forensic data or metadata into a text box
- Upload `.txt` or `.csv` files directly
- GPT-4 processes the input and returns a forensic summary
- Powered by Gradio for an interactive browser-based interface

## 🔐 Prerequisites
- A valid OpenAI API key with GPT-4 access

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/digital-evidence-summarizer.git
cd digital-evidence-summarizer
pip install -r requirements.txt
```

## ⚙️ Setup

1. Create a `.env` file in the project root directory:
```
OPENAI_API_KEY=sk-your-api-key-here
```

2. Run the tool:
```bash
python digital_evidence_summarizer.py
```

## 📂 Input Example
You can paste:
```
Filename: device_log.csv
Location: Recovered from unallocated space
Timestamps: Modified March 3, 2023
Comment: Contains USB device insertion history
```

## 📄 Output Example
```
The file `device_log.csv` was recovered from unallocated space and appears to contain USB device activity. Timestamps suggest relevant user activity occurred on March 3, 2023...
```

## 🧑‍🏫 Instructor
This project is developed for **Prof. Douglas** for use in demonstrating the role of generative AI in digital forensics education.

---

*Made with ❤️ by Jerson Recarte*
