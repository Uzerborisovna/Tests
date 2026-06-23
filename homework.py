import requests
import os


def calculate_square(a):
    perimeter = a * 4
    return ('Периметр:', perimeter)


def discriminant(a, b, c):
    for arg in a, b, c:
        if not isinstance(arg, int):
            return "Аргументы должны быть целыми числами!"
    d = b ** 2 - (4 * a * c)
    return d


def solution_quadratic_equation(a, b, c):
    d = discriminant(a, b, c)
    if not isinstance(d, int):
        return d
    if d < 0:
        return "корней нет"
    elif d == 0:
        return - b / (2 * a)
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)


def vote(votes):
    if not votes or not isinstance(votes, list):
        return "Входной аргумент должен быть заполненным списком!"
    for vote in votes:
        if not isinstance(vote, int) or vote <= 0:
            return "Список должен содержать только целые положительные числа!"
    replay_numbers = {}
    for num in votes:
        replay_numbers[num] = replay_numbers.get(num, 0) + 1
    replay_numbers_for_check = replay_numbers
    replay_numbers = sorted(replay_numbers.items(), key=lambda x: -x[1])
    max_vote = replay_numbers[0][0]
    max_value = replay_numbers_for_check[max_vote]
    if tuple(replay_numbers_for_check.values()).count(max_value) > 1:
        return "Максимальное число всегда уникально."
    return max_vote


def create_folder(path, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(f'{url}?path={path}', headers=headers)
    sc = response.status_code
    return sc

wrongtoken = 'y0wgBEJxvw4Y25YDIMeB0_QXhbCyb2Kq5GqiwSwJhqwMn6hORWQ'