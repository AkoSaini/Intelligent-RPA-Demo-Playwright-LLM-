from extract_llm import extract_fields
from fill_form import fill_form
import json

# Example unstructured input (like an email/request)
text = (
    "Hi, this is John Smith. My account number is 45678. "
    "I moved to Dallas and need my address updated."
)

print("Sending text to LLM...")

# Use the LLM to extract structured fields (returns a Python dict)
fields = extract_fields(text)
print("LLM returned:", fields)

# Save extracted data for traceability/debugging
with open("output/extracted.json", "w") as f:
    json.dump(fields, f, indent=2)

# Use Playwright to fill a UI form with the extracted fields
fill_form("form.html", fields)

print("Done!")
