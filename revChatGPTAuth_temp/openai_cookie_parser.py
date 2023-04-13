from http.cookiejar import Cookie
from typing import Any, Optional

from yt_dlp.cookies import SUPPORTED_BROWSERS, extract_cookies_from_browser
from yt_dlp.utils import YoutubeDLCookieJar


class OpenAICookieParser:

    def __init__(self, browser_name: str):
        if browser_name not in SUPPORTED_BROWSERS:
            raise ValueError(f'Browser {browser_name} is not supported. Supported browsers are: {SUPPORTED_BROWSERS}')
        self.BROWSER_NAME = browser_name

    def parse_cookie(self):
        all_cookies: YoutubeDLCookieJar = extract_cookies_from_browser(self.BROWSER_NAME)
        openai_cookies = self._get_openai_cookies(all_cookies.__dict__)
        openai_cookies_dict: dict[str, Optional[str]] = {key: cookie.value for key, cookie in openai_cookies.items()}
        return openai_cookies_dict

    def _get_openai_cookies(self, all_cookies_dict: dict[str, Any]):
        try:
            chat_openai_cookies: dict[str, Cookie] = all_cookies_dict['_cookies']['chat.openai.com']['/']
            dot_chat_openai_cookies: dict[str, Cookie] = all_cookies_dict['_cookies']['.chat.openai.com']['/']
            dot_openai_cookies: dict[str, Cookie] = all_cookies_dict['_cookies']['.openai.com']['/']
            openai_cookies = {**chat_openai_cookies, **dot_chat_openai_cookies, **dot_openai_cookies}
            return openai_cookies
        except KeyError as error:
            raise ValueError(
                f'OpenAI cookies not found. Please log in to OpenAI using your browser {self.BROWSER_NAME} to proceed.'
            ) from error
