from typing import Union

from aomaker.session import BaseLogin
from aomaker.core.http_client import HTTPClient

from apis.mock.apis import LoginAPI

class Login(BaseLogin):


    def login(self) -> Union[dict, str]:
        login_request_data = LoginAPI.RequestBodyModel(
            username=self.account['user'],
            password=self.account['pwd']
        )
        login_api = LoginAPI(
            request_body=login_request_data,
            http_client=HTTPClient()
        )
        resp_login = login_api.send()
        return resp_login.response_model.data.access_token

    def make_headers(self, resp_login: Union[dict, str]) -> dict:
        token = resp_login
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return headers
    
    