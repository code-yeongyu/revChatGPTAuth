from unittest.mock import MagicMock, patch

from revChatGPTAuth.chatgpt_access_token_parser import ChatGPTAccessTokenParser, get_access_token


class TestChatGPTAccessTokenParser:

    @patch('revChatGPTAuth.chatgpt_access_token_parser.OpenAICookieParser')
    @patch('httpx.get')
    def test_get_openai_chatgpt_access_token(
        self,
        mock_httpx_get: MagicMock,
        mock_openai_cookie_parser: MagicMock,
    ) -> None:
        # given
        ## mock cookies
        mock_cookie_parser = MagicMock()
        mock_cookie_parser.parse_cookie.return_value = {'cookie_key': 'cookie_value'}
        mock_openai_cookie_parser.return_value = mock_cookie_parser

        ## mock access token response
        expected_access_token = 'access_token'
        mock_response = MagicMock()
        mock_response.json.return_value = {'accessToken': expected_access_token}
        mock_httpx_get.return_value = mock_response

        chatgpt_access_token_parser = ChatGPTAccessTokenParser('chrome')

        # when
        access_token = chatgpt_access_token_parser.get_access_token()

        # then
        mock_cookie_parser.parse_cookie.assert_called_once()
        mock_httpx_get.assert_called_once_with(
            'https://chat.openai.com/api/auth/session',
            headers={'cookie': 'cookie_key=cookie_value'},
        )
        mock_response.raise_for_status.assert_called_once()
        assert access_token == expected_access_token


@patch('revChatGPTAuth.chatgpt_access_token_parser.ChatGPTAccessTokenParser')
def test_get_access_token(mock_chatgpt_access_token_parser: MagicMock) -> None:
    # given
    expected_access_token = 'access_token'
    mock_chatgpt_access_token_parser.return_value.get_openai_chatgpt_access_token.return_value = expected_access_token

    # when
    access_token = get_access_token('chrome')

    # then
    mock_chatgpt_access_token_parser.assert_called_once_with('chrome')
    assert access_token == expected_access_token
