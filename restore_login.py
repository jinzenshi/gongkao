import asyncio
from playwright.async_api import async_playwright
import os
import json

async def main():
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=False)
        
        # 记录 session 文件路径
        session_file = os.path.join(os.path.dirname(__file__), 'session.json')
        
        # 创建一个带有保存好的 storage state 的 context
        context = await browser.new_context(storage_state=session_file)
        
        # 打开页面
        page = await context.new_page()
        await page.goto("https://www.gongkaoleida.com/user/article/2790853")
        
        print("浏览器已打开并尝试恢复登录状态。")
        print("如果看到右上角显示用户名，则说明登录成功。")
        
        # 保持浏览器打开
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
