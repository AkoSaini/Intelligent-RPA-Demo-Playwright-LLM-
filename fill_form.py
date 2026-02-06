from pathlib import Path
from playwright.sync_api import sync_playwright

def fill_form(form_path, fields):
    # Convert local HTML file path into a file:// URL the browser can open
    file_url = Path(form_path).resolve().as_uri()

    with sync_playwright() as p:
        # Launch a Chromium browser and open a new tab
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local form page
        page.goto(file_url)

        # Fill fields using CSS selectors that match element ids in form.html
        page.fill("#name", fields["name"])
        page.fill("#account", fields["account_number"])
        page.fill("#type", fields["request_type"])
        page.fill("#notes", fields["notes"])

        # Save a screenshot as proof the automation ran
        page.screenshot(path="output/result.png")
        browser.close()

if __name__ == "__main__":
    demo_data = {
        "name": "John Smith",
        "account_number": "45678",
        "request_type": "Address Change",
        "notes": "Moved to Dallas"
    }

    fill_form("form.html", demo_data)
    print("Saved screenshot to output/result.png")
