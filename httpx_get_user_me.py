import httpx

url = "http://localhost:8000"

# Сохраняем данные для входа в переменную
email = input('Введите почту: ')
password = input('Введите пароль: ')

# Заготавливаем JSON данные для отправки в POST запросах
reg_data = {
    "email": email,
    "password": password,
    "lastName": "default",
    "firstName": "default",
    "middleName": "default"
}

login_data = {
    "email": email,
    "password": password
}


# Регистрируем нового пользователя
def reg_users():
    httpx.post(f"{url}/api/v1/users", json=reg_data)


# Выполняем authentication/login для пользователя
def user_authentication():
    login_response = httpx.post(f'{url}/api/v1/authentication/login', json=login_data)

    # Вытаскиваем токен и сохраняем его
    accesstoken = login_response.json()['token']["accessToken"]
    return accesstoken


# Проверяем что пользователь авторизован
def check_user():
    # Создаем Headers
    accesstoken = {
        "Authorization": f"Bearer {user_authentication()}"
    }
    check_response = httpx.get(f'{url}/api/v1/users/me', headers=accesstoken)
    print(check_response.json())
    print(check_response.status_code)


reg_users()
user_authentication()
check_user()
