from http.cookiejar import Cookie
from unittest.mock import MagicMock, patch

import pytest
from yt_dlp.cookies import SUPPORTED_BROWSERS
from yt_dlp.utils import YoutubeDLCookieJar

from revChatGPTAuth.openai_cookie_parser import OpenAICookieParser


class TestOpenAICookieParser:

    def test_init_with_unsupported_browser(self):
        with pytest.raises(ValueError):
            OpenAICookieParser(browser_name='Internet Explorer Holy Shit')

    @pytest.mark.parametrize('supported_browser', SUPPORTED_BROWSERS)
    def test_init_with_supported_browser(self, supported_browser: str):
        parser = OpenAICookieParser(browser_name=supported_browser)
        assert parser.BROWSER_NAME == supported_browser

    @pytest.mark.parametrize('supported_browser', SUPPORTED_BROWSERS)
    @patch('revChatGPTAuth.openai_cookie_parser.extract_cookies_from_browser')
    def test_parse_cookie_with_supported_browser(
        self,
        mock_extract_cookies: MagicMock,
        supported_browser: str,
    ):
        # given
        cookie_jar = YoutubeDLCookieJar()
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
        mock_extract_cookies.return_value = cookie_jar
        parser = OpenAICookieParser(browser_name=supported_browser)

        # when
        openai_cookies = parser.parse_cookie()

        # then
        assert openai_cookies == {'cookie1': 'value1', 'cookie2': 'value2', 'cookie3': 'value3'}
