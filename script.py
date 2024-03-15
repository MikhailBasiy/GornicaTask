#!.env/bin/python

import re

class InputError(Exception):
    pass

def input_prompt() -> str:
    item = input("Для получения характеристик введите артикул стеклопакета: ")
    return item


def check_input(item: str) -> bool:
    # Проверка соответствия ввода указанному в задании шаблону
    pattern1 = r"(?:[\d]{1,2}[^\\]*\\[\d]{1,2}[^\\]*){1,2}\\[\d]{1,2}[^\\]*" 
    pattern2 = r"[\d]{1,2}[^\\]*" # Пропускает ввод в формате (число// | число)
    check1 = re.match(pattern1, item) or re.match(pattern2, item)
    check2 = len(re.findall(r"\\", item)) in (0, 2, 4)
    return check1 and check2


def parse_item(item: str) -> str:
    raw_lst = re.split(r"\\", item)
    properties_lst = []
    for property in raw_lst:
        if property:
            m = re.match(r"[0-9]{1,2}", property)
            properties_lst.append(m.group(0))
    layers_cnt = len(properties_lst) 
    if layers_cnt < 3:
        chambers = 0
    elif layers_cnt < 5:
        chambers = 1
    elif layers_cnt == 5:
        chambers = 2
    else:
        raise InputError("Введен некорректный артикул")

    print("Камерность: " + str(chambers))
    print("Толщина стеклопакета: " + str(sum(map(int, properties_lst))))
    print("Толщина стекла: " + str(sum(map(int, properties_lst[::2]))))


if __name__ == "__main__":
    while True:
        item = input_prompt()
        if check_input(item):
            parse_item(item)
        else:
            print("Введите корректный артикул")
