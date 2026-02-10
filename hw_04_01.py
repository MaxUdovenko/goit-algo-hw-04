def total_salary(path):
    """
    Функція аналізує файл і повертає загальну та середню суму 
    заробітної плати всіх розробників.

    Результатом роботи функції є кортеж із двох чисел: 
    загальної суми зарплат і середньої заробітної плати.
    
    :param path: шлях до файлу
    """

    total = 0
    average = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                tmp = int(line.rstrip().split(",")[1])

                total += tmp
                average += (tmp - average) / line_number
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    
    return total, int(average)


def test(path):
    total, average = total_salary(path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    print("\n")


if __name__ == "__main__":
    test("salary.txt")
    test("salar.txt")
