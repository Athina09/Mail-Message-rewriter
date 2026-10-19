# Mail Message Rewriter

A small command-line tool that rewrites an email or message in the tone you choose. Built with LangChain and Google Gemini.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key (free at https://aistudio.google.com/apikey)

## Setup

```bash
git clone https://github.com/Athina09/Mail-Message-rewriter.git
cd Mail-Message-rewriter

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a file named `.env` in the project folder and add your key:

```
GOOGLE_API_KEY=your-key-here
```

The `.env` file is listed in `.gitignore`, so your key is never committed.

## Usage

```bash
python rewriter.py
```

You will be asked for two things:

1. A tone, for example `professional`, `friendly` or `short`. Press Enter for `professional`.
2. The message you want rewritten.

Example:

```
Tone (professional/friendly/short): friendly
Message: send me the report asap

Could you please send me the report as soon as you can?
```

## Project files

| File | Purpose |
|---|---|
| `rewriter.py` | The whole app |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Keeps `.env` and `.venv` out of git |

## Author

Athina09
