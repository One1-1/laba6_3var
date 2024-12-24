def task6_1(filename):
    '''
    Дан файл, в котором записаны цены товаров (в виде 1 руб. 50 коп.). Описать функцию,
    определяющую наименьшую цену, записанную в файле. В новый файл записать все
    строки, соответствующим ценам выше средней цены. Предусмотреть обработку всех
    возможных исключительных ситуаций.

    :return: None
    '''
    def open_file(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                prices = f.readline().split()  # читаем строку и разделяем по пробелам
                prices = list(map(float, prices))  # преобразуем каждый элемент списка в float
            return prices
        except FileNotFoundError:
            print("Ошибка: Файл 'price' не найден.")
            return []
        except ValueError:
            print("Ошибка: Не удалось преобразовать данные в числа.")
            return []

    def min_price(prices):
        if prices:  # Проверяем, что список не пуст
            mini_price = min(prices)  # находим минимальное из цен
            print("Минимальная цена:", mini_price)
        else:
            print("Список цен пуст.")

    def sred_price(prices):
        if prices:  # Проверяем, что список не пуст
            srednie_price = sum(prices) / len(prices)  # находим среднее из цен
            print("Средняя цена:", srednie_price)
            return srednie_price
        else:
            print("Список цен пуст.")
            return 0  # Возвращаем 0, чтобы избежать деления на ноль

    def new_file(srednie_price, prices):
        try:
            with open('new_file', 'a+', encoding='utf-8') as file:  # открываем файл один раз
                for i in prices:
                    if i > srednie_price:
                        file.write(f"{i}\n")  # записываем цены, превышающие среднюю
        except IOError:
            print("Ошибка: Не удалось открыть или записать в файл 'new_file'.")

    prices = open_file(filename)  # Считываем цены из файла
    min_price(prices)     # Находим и выводим минимальную цену
    srednie_price = sred_price(prices)  # Находим и выводим среднюю цену
    new_file(srednie_price, prices)  # Записываем цены, превышающие среднюю




def task6_2(input_string, filename):
    '''
    Дана строка символов. Описать процедуру, которая записывает в текстовый файл все
    цифры из этой строки. Предусмотреть обработку всех возможных исключительных ситуаций

    :param input_string: строка, которая вводится ы файл
    :param filename: путь к файлу
    :return: None
    '''
    import os


    def write_to_file(input_string, filename):
        try:
            # Извлекаем цифры из строки
            digits = ''.join(filter(str.isdigit, input_string))

            # Проверяем, существует ли файл
            if not os.path.exists(filename):
                print(f"Ошибка: Файл '{filename}' не найден.")
                return

            # Открываем файл для записи
            with open(filename, 'w') as file:
                if digits:  # Проверяем, есть ли цифры для записи
                    file.write(digits)
                else:
                    print("В строке нет цифр для записи.")

        except IOError:
            print(f"Ошибка ввода-вывода при работе с файлом '{filename}'.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")




    write_to_file(input_string, filename)

