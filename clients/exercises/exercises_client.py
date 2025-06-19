from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class CreateExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с ендпоинтами группы "exercises":
    /api/v1/exercises
    /api/v1/exercises/{exercise_id}
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def create_exercise_api(self, request: CreateExercisesQueryDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления курса.

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')
