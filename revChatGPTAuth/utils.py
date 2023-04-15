from http.cookiejar import CookieJar
from typing import Callable, Optional

import browser_cookie3


def get_cookie_loader(browser_name: Optional[str]) -> Callable[[str], CookieJar]:
    if not browser_name:
        return browser_cookie3.load
    browser_name = browser_name.lower()
    if browser_name == 'chrome':
        return browser_cookie3.chrome
    elif browser_name == 'firefox':
        return browser_cookie3.firefox
    elif browser_name == 'opera' or browser_name == 'opera_gx':
        return browser_cookie3.opera
    elif browser_name == 'edge':
        return browser_cookie3.edge
    elif browser_name == 'chromium':
        return browser_cookie3.chromium
    elif browser_name == 'brave':
        return browser_cookie3.brave
    elif browser_name == 'vivaldi':
        return browser_cookie3.vivaldi
    elif browser_name == 'safari':
        return browser_cookie3.safari
    else:
        raise NotImplementedError


def load_cookies(browser_name: Optional[str] = None, domain: str = '') -> CookieJar:
    cookie_loader = get_cookie_loader(browser_name)
    return cookie_loader(domain)
