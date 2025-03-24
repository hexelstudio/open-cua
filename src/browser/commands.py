# commands.py
from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Optional, Dict
from playwright.async_api import Page


# Base command schema
class CommandSchema(BaseModel):
    action: str
    url: Optional[str] = None
    selector: Optional[str] = None
    text: Optional[str] = None
    options: Dict = {}


# Abstract base command
class BaseCommand(ABC):
    def __init__(self, schema: CommandSchema):
        self.schema = schema

    @abstractmethod
    async def execute(self, page: Page) -> Dict:
        pass


# Navigate Command
class NavigateCommand(BaseCommand):
    async def execute(self, page: Page) -> Dict:
        if not self.schema.url:
            raise ValueError("URL is required for navigation")
        await page.goto(self.schema.url)
        return {"status": "navigated", "url": self.schema.url}


# Click Command
class ClickCommand(BaseCommand):
    async def execute(self, page: Page) -> Dict:
        if not self.schema.selector:
            raise ValueError("Selector is required for click")
        await page.click(self.schema.selector, **self.schema.options)
        return {"status": "clicked", "selector": self.schema.selector}


# Fill Command
class FillCommand(BaseCommand):
    async def execute(self, page: Page) -> Dict:
        if not self.schema.selector or self.schema.text is None:
            raise ValueError("Selector and text are required for fill")
        await page.fill(self.schema.selector, self.schema.text)
        return {"status": "filled", "selector": self.schema.selector, "text": self.schema.text}


# Screenshot Command
class ScreenshotCommand(BaseCommand):
    async def execute(self, page: Page) -> Dict:
        path = self.schema.options.get("path", "screenshot.png")
        await page.screenshot(path=path)
        return {"status": "screenshot taken", "path": path}
