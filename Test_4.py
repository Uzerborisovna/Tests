
import pytest
import requests
import os
from dotenv import load_dotenv
from homework import create_folder, wrongtoken

load_dotenv()

TOKEN = os.getenv('token')
TEST_FOLDER = "моя_тестовая_папка"


def test_create_folder_success():
    if not TOKEN:
        pytest.skip("Нет токена для теста")

    status_code = create_folder(TEST_FOLDER, TOKEN)
    # Проверяем, что статус-код равен 200 (как указано в требовании задачи)
    assert status_code == 200, f"Ожидался 200, получили {status_code}"

    headers = {'Authorization': f'OAuth {TOKEN}'}
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={TEST_FOLDER}'
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Папка не найдена на Яндекс.Диске!"

    # Удаляем папку после теста
    requests.delete(url, headers=headers)


def test_create_folder_wrong_token():
    wrong_token = wrongtoken

    status_code = create_folder(TEST_FOLDER, wrong_token)
    assert status_code == 401, f"Ожидался 401, получили {status_code}"

    headers = {'Authorization': f'OAuth {wrong_token}'}
    url = f'https://cloud-api.yandex.net/v1/disk/resources?path={TEST_FOLDER}'
    response = requests.get(url, headers=headers)
    assert response.status_code != 200, "Папка не должна существовать"