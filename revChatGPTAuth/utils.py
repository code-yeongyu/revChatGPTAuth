from http.cookiejar import CookieJar
from typing import Callable, Optional

import browser_cookie3

from revChatGPTAuth.supported_browser import SupportedBrowser


def get_cookie_loader(browser_name: Optional[SupportedBrowser]) -> Callable[[str], CookieJar]:
    if not browser_name:
        return browser_cookie3.load
    if browser_name == SupportedBrowser.CHROME:
        return browser_cookie3.chrome
    if browser_name == SupportedBrowser.FIREFOX:
        return browser_cookie3.firefox
    if browser_name == SupportedBrowser.OPERA:
        return browser_cookie3.opera
    if browser_name == SupportedBrowser.OPERA_GX:
        return browser_cookie3.opera_gx
    if browser_name == SupportedBrowser.EDGE:
        return browser_cookie3.edge
    if browser_name == SupportedBrowser.CHROMIUM:
        return browser_cookie3.chromium
    if browser_name == SupportedBrowser.BRAVE:
        return browser_cookie3.brave
    if browser_name == SupportedBrowser.VIVALDI:
        return browser_cookie3.vivaldi
    if browser_name == SupportedBrowser.SAFARI:
        return browser_cookie3.safari
    raise ValueError(f'Unsupported browser: {browser_name}')


def load_cookies(browser_name: Optional[SupportedBrowser] = None, domain: str = '') -> CookieJar:
    cookie_loader = get_cookie_loader(browser_name=browser_name)
    return cookie_loader(domain)
