from pprint import pprint

def get_cats_info(path):
    """
    Функція читає файл та повертає список словників
    з інформацією про кожного кота

    :param path: шлях до файлу
    """

    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                tmp = line.rstrip().split(",")
                cats.append(
                    {"id": tmp[0], "name": tmp[1], "age": tmp[2]},
                )
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    pprint(cats_info)

    cats_info = get_cats_info("cats_fie.txt")
    pprint(cats_info)
