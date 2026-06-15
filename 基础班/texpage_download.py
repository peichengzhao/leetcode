#!/usr/bin/env python3
"""
TexPage 项目下载脚本
由于 TexPage 下载 API 需要登录认证，支持两种方式：
1. Cookie 方式：从浏览器复制登录后的 Cookie
2. Selenium 方式：自动打开浏览器，用户手动登录后自动下载
"""

import os
import sys
import json
import zipfile
import argparse
from pathlib import Path

# 默认下载链接
DEFAULT_DOWNLOAD_URL = (
    "https://www.texpage.com/api/project/download"
    "?projectKey=efc817e1-c6f0-4caf-a998-ec157701bc73"
    "&versionNo=844cf9f1-120d-48fc-93e2-61d46443adc7"
    "&bbl=false"
)


def download_with_cookies(url: str, cookies: str, output_dir: str = ".") -> bool:
    """
    使用 Cookie 下载项目
    :param url: 下载链接
    :param cookies: Cookie 字符串，格式如 "name1=value1; name2=value2"
    :param output_dir: 输出目录
    :return: 是否成功
    """
    try:
        import requests
    except ImportError:
        print("请先安装 requests: pip install requests")
        return False

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "*/*",
        "Referer": "https://www.texpage.com/",
    }

    cookie_dict = {}
    # 支持 "a=1; b=2" 或 每行 "a=1" 的格式
    raw = cookies.strip().replace("\n", "; ")
    for item in raw.split(";"):
        item = item.strip()
        if "=" in item:
            k, v = item.split("=", 1)
            cookie_dict[k.strip()] = v.strip()

    print("正在请求下载...")
    resp = requests.get(url, headers=headers, cookies=cookie_dict, timeout=30)

    # 检查是否是 JSON 错误响应
    content_type = resp.headers.get("Content-Type", "")
    if "application/json" in content_type:
        try:
            data = resp.json()
            if data.get("status", {}).get("code") == 1003:
                print("错误: 未登录或 Cookie 已过期，请重新获取 Cookie")
                return False
            if data.get("status", {}).get("code") != 0:
                print(f"错误: {data.get('status', {}).get('message', '未知错误')}")
                return False
        except json.JSONDecodeError:
            pass

    if resp.status_code != 200:
        print(f"HTTP 错误: {resp.status_code}")
        return False

    # 尝试解析为 zip
    content = resp.content
    if len(content) < 4:
        print("下载内容为空或无效")
        return False

    # ZIP 文件魔数
    if content[:2] == b"PK" or content[:4] == b"PK\x03\x04":
        output_path = Path(output_dir) / "texpage_project.zip"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(content)
        print(f"已保存到: {output_path}")

        # 尝试解压
        extract_dir = Path(output_dir) / "texpage_project"
        try:
            with zipfile.ZipFile(output_path, "r") as zf:
                zf.extractall(extract_dir)
            print(f"已解压到: {extract_dir}")
        except zipfile.BadZipFile:
            print("文件可能不是有效的 zip，已保存原始文件")

        return True
    else:
        # 可能是 JSON 错误
        try:
            data = json.loads(content.decode("utf-8"))
            print(f"API 返回: {json.dumps(data, ensure_ascii=False, indent=2)}")
            return False
        except Exception:
            output_path = Path(output_dir) / "texpage_project.bin"
            with open(output_path, "wb") as f:
                f.write(content)
            print(f"已保存原始内容到: {output_path}")
            return True


def download_with_selenium(url: str, output_dir: str = ".") -> bool:
    """
    使用 Selenium 打开浏览器，用户登录后自动下载
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
    except ImportError:
        print("请先安装: pip install selenium")
        print("并确保已安装 Chrome 浏览器和 chromedriver")
        return False

    chrome_options = Options()
    # 不无头模式，让用户能看到并登录
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    print("正在启动浏览器...")
    print("请在浏览器中登录 TexPage，登录成功后按回车继续...")

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Chrome 启动失败: {e}")
        print("可尝试: pip install webdriver-manager")
        print("然后修改脚本使用 webdriver_manager")
        return False

    try:
        # 先打开登录页
        driver.get("https://www.texpage.com/zh/login")
        input("登录完成后，按回车键继续下载...")

        # 获取 cookies 并下载
        cookies = driver.get_cookies()
        cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies)

        driver.quit()
        return download_with_cookies(url, cookie_str, output_dir)
    except Exception as e:
        print(f"错误: {e}")
        driver.quit()
        return False


def get_cookie_from_browser():
    """打印如何从浏览器获取 Cookie 的说明"""
    print("""
========== 如何获取 Cookie ==========
1. 打开 Chrome/Edge，访问 https://www.texpage.com 并登录
2. 按 F12 打开开发者工具
3. 切换到 Network（网络）标签
4. 刷新页面或点击任意链接
5. 点击任意请求，在 Request Headers 中找到 Cookie
6. 复制整个 Cookie 的值（从第一个 name=value 到最后一个）

或者使用 Cookie 编辑扩展（如 EditThisCookie）导出 Cookie 字符串。
====================================
""")


def main():
    parser = argparse.ArgumentParser(description="TexPage 项目下载工具")
    parser.add_argument(
        "-u", "--url",
        default=DEFAULT_DOWNLOAD_URL,
        help="下载链接（默认使用预设链接）"
    )
    parser.add_argument(
        "-c", "--cookie",
        help="登录后的 Cookie 字符串，或 Cookie 文件路径（每行 name=value）"
    )
    parser.add_argument(
        "-o", "--output",
        default=".",
        help="输出目录（默认当前目录）"
    )
    parser.add_argument(
        "-s", "--selenium",
        action="store_true",
        help="使用 Selenium 模式（打开浏览器手动登录）"
    )
    parser.add_argument(
        "--help-cookie",
        action="store_true",
        help="显示如何获取 Cookie 的说明"
    )

    args = parser.parse_args()

    if args.help_cookie:
        get_cookie_from_browser()
        return

    if args.selenium:
        success = download_with_selenium(args.url, args.output)
    elif args.cookie:
        cookie = args.cookie
        if os.path.isfile(cookie):
            with open(cookie, "r", encoding="utf-8") as f:
                cookie = f.read()
        success = download_with_cookies(args.url, cookie, args.output)
    else:
        print("请选择认证方式：")
        print("  1. 使用 Cookie: python texpage_download.py -c '你的Cookie'")
        print("  2. 使用 Selenium: python texpage_download.py -s")
        print("  3. 查看如何获取 Cookie: python texpage_download.py --help-cookie")
        return

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
