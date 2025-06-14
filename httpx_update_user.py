import httpx
from tools.fakers import get_random_email

url = "http://localhost:8000"

# Заготавливаем JSON данные для отправки в POST запросах
reg_data = {
    "email": get_random_email(),
    "password": "default",
    "lastName": "default",
    "firstName": "default",
    "middleName": "default"
}

login_data = {
    "email": reg_data["email"],
    "password": reg_data["password"]
}


# Регистрируем нового пользователя
httpx.post(f"{url}/api/v1/users", json=reg_data)


# Выполняем authentication/login для пользователя
login_response = httpx.post(f'{url}/api/v1/authentication/login', json=login_data)

# Берем токен
accesstoken = {
    "Authorization": f"Bearer {login_response.json()['token']["accessToken"]}"
}

# Проверяем что пользователь авторизован и вытаскиваем id
check_response = httpx.get(f'{url}/api/v1/users/me', headers=accesstoken)

# Меняем почту пользователя на новую рандомную
new_data_body = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

update = httpx.patch(f'{url}/api/v1/users/{check_response.json()['user']['id']}', json=new_data_body, headers=accesstoken)
print(update.status_code)
print(update.json())
