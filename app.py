import requests


def get_pun():
    url = 'https://punapi.com/random'
    response = requests.get(url)
    if response.status_code == 200:
        pun_data = response.json()
        return pun_data['pun']
    else:
        return 'Erreur lors de la récupération du jeu de mots.'


if __name__ == "__main__":
    pun = get_pun()
    print(pun)
