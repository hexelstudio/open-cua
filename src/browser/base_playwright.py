from playwright.sync_api import sync_playwright

with sync_playwright()  as p:
    #launch chrominum browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    # Create new page
    page = context.new_page()
    page.goto("https://hexelstudio.com")
    browser.close()
