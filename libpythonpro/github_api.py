import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar do usuario no Github
    :param usuario:srt com o nome de usuario no github
    :return:str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
