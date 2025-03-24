# playwright_controller.py
import asyncio
from playwright.async_api import async_playwright, Browser, Page
from commands import BaseCommand
from command_parser import parse_command

class PlaywrightController:
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser: Browser = None
        self.page: Page = None

    async def init(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.headless)
        self.page = await self.browser.new_page()

    async def shutdown(self):
        await self.browser.close()
        await self.playwright.stop()

    async def run_command(self, command: BaseCommand) -> dict:
        try:
            result = await command.execute(self.page)
            return result
        except Exception as e:
            return {"error": str(e)}

# Usage example:


async def main():
    controller = PlaywrightController(headless=True)
    await controller.init()

    # Example command from LLM (as dict)
    cmd_dict = {"action": "navigate", "url": "https://example.com"}
    command = parse_command(cmd_dict)
    result = await controller.run_command(command)
    print(result)

    await controller.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
