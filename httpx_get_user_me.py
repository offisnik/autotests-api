import httpx

url = "http://localhost:8000"

# Сохраняем данные для входа в переменную
email = input('Введите почту: ')

# Заготавливаем JSON данные для отправки в POST запросах
reg_data = {
    "email": email,
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
accesstoken = login_response.json()['token']["accessToken"]

header = {
    "Authorization": f"Bearer {accesstoken}"
}
check_response = httpx.get(f'{url}/api/v1/users/me', headers=header)
print(check_response.json())
print(check_response.status_code)

