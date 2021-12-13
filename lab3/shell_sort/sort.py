import json
import pickle


def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as read_file:
        local_data = json.load(read_file)
    return local_data


def shell_sort(local_data: list[int]) -> list[int]:
    last_index = len(local_data) - 1
    middle = len(local_data) // 2
    while middle > 0:
        for i in range(middle, last_index + 1, 1):
            j = i
            delta = j - middle
            while delta >= 0 and local_data[delta]['weight'] > local_data[j]['weight']:
                local_data[delta], local_data[j] = local_data[j], local_data[delta]
                j = delta
                delta = j - middle
        middle //= 2
    return local_data


def serialization(local_data: list, path: str) -> None:
    with open(path, 'wb') as file:
        pickle.dump(local_data, file)


def deserialization(path: str) -> list:
    with open(path, 'rb') as file:
        local_data = pickle.load(file)
    return local_data


data = read_data('D:\\out.txt')
shell_sort(data)
out = open('D:\\res.txt', 'w', encoding='utf-8')
new_data = json.dumps(data, ensure_ascii=False, indent=4)
out.write(new_data)
out.close()
