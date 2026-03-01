# SummarizeText

A Python application that automatically summarizes PDF documents using LangChain and OpenAI's GPT-3.5 model.

## Description

This project loads PDF files from a data directory and generates concise 3-4 sentence summaries for each document using OpenAI's language model. It uses LangChain for document loading and prompt management, making it easy to process multiple PDFs and track token usage.

## Features

- **PDF Processing**: Loads and extracts text from multiple PDF files
- **AI-Powered Summarization**: Uses GPT-3.5-turbo for intelligent text summarization
- **Token Tracking**: Monitors token usage for cost optimization
- **Batch Processing**: Processes multiple documents in sequence

## Requirements

- Python 3.7+
- OpenAI API key
- Dependencies listed in requirements.txt

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your PDF files in the `data/` directory
2. Run the application:
```bash
python main.py
```

The script will:
- Load all PDF files from the `data/` directory
- Extract text from each PDF
- Generate summaries using GPT-3.5
- Display token count and summary for each document

## Project Structure

```
SumarizeText/
├── main.py           # Main application script
├── data/             # Directory for PDF files
│   ├── study_text1.pdf
│   └── study_text2.pdf
└── README.md         # This file
```

## Configuration

- **Model**: GPT-3.5-turbo (configurable in main.py)
- **Temperature**: 0.7 (controls randomness of responses)
- **Summary Length**: 3-4 sentences

## Dependencies

- `langchain` - LLM orchestration
- `langchain-openai` - OpenAI integration
- `langchain-community` - Document loaders
- `python-dotenv` - Environment variable management

## Notes

- Ensure your OpenAI account has sufficient credits
- PDF files should be readable and contain extractable text
- Token usage is logged for each article to monitor API costs
