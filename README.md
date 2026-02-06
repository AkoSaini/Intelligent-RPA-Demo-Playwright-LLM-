# Intelligent RPA Demo (Playwright + LLM)

This project demonstrates a simple “intelligent automation” workflow:
1) An LLM API extracts structured fields (JSON) from unstructured text
2) Playwright uses those fields to fill a web form automatically

## What it does
- Input: a short request message (like an email)
- Output:
  - `output/extracted.json` (structured fields)
  - `output/result.png` (screenshot of the completed form)

## Files
- `main.py` — runs the full pipeline
- `extract_llm.py` — calls the LLM API and returns JSON fields
- `fill_form.py` — Playwright UI automation to fill the form
- `form.html` — local form page the bot interacts with

## Notes
- `.env` is not included because it contains the API key.
- The LLM call uses an OpenAI-compatible endpoint (Groq) and can be swapped to another provider.
