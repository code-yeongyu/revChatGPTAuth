from http.cookiejar import Cookie, CookieJar
from unittest.mock import MagicMock, patch

import pytest

from revChatGPTAuth.openai_cookie_parser import OpenAICookieParser
from revChatGPTAuth.supported_browser import SupportedBrowser


class TestOpenAICookieParser:
    SUPPORTED_BROWSERS = [SupportedBrowser(browser_name) for browser_name in OpenAICookieParser.SUPPORTED_BROWSERS]

    @pytest.mark.parametrize('supported_browser', SUPPORTED_BROWSERS)
    def test_init_with_supported_browser(self, supported_browser: SupportedBrowser):
        parser = OpenAICookieParser(browser_name=supported_browser)
        assert parser.BROWSER_NAME == supported_browser

    @pytest.mark.parametrize('supported_browser', SUPPORTED_BROWSERS)
    @patch('revChatGPTAuth.openai_cookie_parser.load_cookies')
    def test_parse_cookie_with_supported_browser(
        self,
        mock_load_cookies: MagicMock,
        supported_browser: SupportedBrowser,
    ):
        # given
        cookie_jar = CookieJar()
        cookie_jar.set_cookie(
            Cookie(
                version=0,
                name='cookie1',
                value='value1',
                port=None,
                port_specified=False,
                domain='chat.openai.com',
                domain_specified=True,
                domain_initial_dot=False,
                path='/',
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={},
            ))
        cookie_jar.set_cookie(
            Cookie(
                version=0,
                name='cookie2',
                value='value2',
                port=None,
                port_specified=False,
                domain='.openai.com',
                domain_specified=False,
                domain_initial_dot=True,
                path='/',
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={},
            ))
        cookie_jar.set_cookie(
            Cookie(
                version=0,
                name='cookie3',
                value='value3',
                port=None,
                port_specified=False,
                domain='.chat.openai.com',
                domain_specified=False,
                domain_initial_dot=True,
                path='/',
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={},
            ))
        mock_load_cookies.return_value = cookie_jar
        parser = OpenAICookieParser(browser_name=supported_browser)

        # when
        openai_cookies = parser.parse_cookie()

        # then
        assert openai_cookies == {'cookie1': 'value1', 'cookie2': 'value2', 'cookie3': 'value3'}
