# main.py

def add_item(lst, item):
    """Додає елемент до списку"""
    lst.append(item)
    return lst

def remove_item(lst, item):
    """Видаляє елемент зі списку, якщо він є"""
    if item in lst:
        lst.remove(item)
    return lst

def print_list(lst):
    """Виводить список у зручному форматі"""
    print("Список:", lst)

# Приклад використання
if __name__ == "__main__":
    my_list = []
    add_item(my_list, "apple")
    add_item(my_list, "banana")
    remove_item(my_list, "apple")
    print_list(my_list)
