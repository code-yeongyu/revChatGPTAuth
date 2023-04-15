from typing import Union

import httpx

from revChatGPTAuth.supported_browser import SupportedBrowser

from .openai_cookie_parser import OpenAICookieParser


class ChatGPTAccessTokenParser:

    def __init__(self, browser_name: SupportedBrowser):
        self.openai_cookie_parser = OpenAICookieParser(browser_name)

    def get_access_token(self) -> str:
        cookie = self._get_stringified_cookies()
        response = self._auth_openai(cookie)
        response.raise_for_status()
        return response.json()['accessToken']

    def _get_stringified_cookies(self) -> str:
        cookies = self.openai_cookie_parser.parse_cookie()
        return '; '.join([f'{key}={value}' for key, value in cookies.items()])

    def _auth_openai(self, cookie: str) -> httpx.Response:
        URL = 'https://chat.openai.com/api/auth/session'
        headers = {'cookie': cookie}
        response = httpx.get(URL, headers=headers)
        return response


def get_access_token(browser_name: Union[str, SupportedBrowser]) -> str:
    if isinstance(browser_name, str):
        browser_name = SupportedBrowser(browser_name)
    chatgpt_access_token_parser = ChatGPTAccessTokenParser(browser_name)
    return chatgpt_access_token_parser.get_access_token()
