import asyncio
from playwright.async_api import async_playwright
import os
import json

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        session_file = os.path.join(os.path.dirname(__file__), 'session.json')
        
        # Check if session.json exists
        if not os.path.exists(session_file):
            print(f"Error: {session_file} not found")
            return

        context = await browser.new_context(storage_state=session_file)
        page = await context.new_page()
        
        # Navigate and wait for content
        await page.goto("https://www.gongkaoleida.com/user/article/2790853")
        await page.wait_for_timeout(3000)
        
        # Check for username in the header
        content = await page.content()
        if "Four Leaf Clover" in content:
            print("SUCCESS: Login state restored. User 'Four Leaf Clover' found.")
        else:
            print("FAILURE: Login state NOT restored.")
            # Print some debug info
            print(f"URL: {page.url}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
