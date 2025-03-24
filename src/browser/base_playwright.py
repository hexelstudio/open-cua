from abc import abstractmethod
from dataclasses import dataclass
from playwright.sync_api import sync_playwright


@dataclass
class BrowserConfig:
    # user_oauth: dict
    start: str = "https://google.com/"
   
    
class BrowserBase:
    
    def __init__(self):
        self.config = BrowserConfig()
        self._launch()
    
    def _launch(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.config.start)
            browser.close()
            
        
if __name__ == "__main__":
    browser = BrowserBase()  

