import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "test@mail.ru",
    "password": "123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

login_access_token = login_response_data["token"]["accessToken"]
login_type_token = login_response_data["token"]["tokenType"]
authorization_token = login_type_token + " " + login_access_token

headers = {"Authorization": authorization_token}

get_user_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Status Code:", get_user_me.status_code)
print(get_user_me.json())

print("______")
print(authorization_token)