import requests

# URL файла
url = "https://gbcdn.mrgcdn.ru/uploads/asset/5561247/attachment/f5d1b3d79db99a54dabc1c195db68588.ipynb"

# Скачивание файла
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Сохранение файла
    with open("downloaded_file1.ipynb", "wb") as file:
        file.write(response.content)
    print("Файл успешно скачан и сохранен как 'downloaded_file.ipynb'.")
else:
    print("Ошибка при скачивании файла:", response.status_code)