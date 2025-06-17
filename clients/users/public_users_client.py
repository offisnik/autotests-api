from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса на регистрацию нового юзера
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с ендпоинтом /api/v1/users (метод POST)
    """
    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        :param request: Словарь с полями email, password, lastName, firstName, middleName
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/users", json=request)
