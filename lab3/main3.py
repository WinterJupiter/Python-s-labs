import argparse
from shell_sort.validator import *
from shell_sort.sort import *
from tqdm import tqdm
import random
import json
import pickle
import autopep8

parser = argparse.ArgumentParser()
parser.add_argument('-input', type=str, default="D:\\105.txt", dest='input')
parser.add_argument('-output', type=str, default="D:\\out.txt", dest='output')
parser.add_argument('-output_sort', type=str, default="D:\\res.txt", dest='output_sort')
args = parser.parse_args()

data = json.load(open(args.input, encoding='utf-8'))

true_data = list()
email = 0
weight = 0
snils = 0
passport_number = 0
work_experience = 0
university = 0
political_view = 0
worldview = 0
address = 0
with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not Validator.control_email(person['email']):
            email += 1
            temp = False
        if not Validator.control_weight(person['weight']):
            weight += 1
            temp = False
        if not Validator.control_snils(person['snils']):
            snils += 1
            temp = False
        if not Validator.control_passport(person['passport_number']):
            passport_number += 1
            temp = False
        if not Validator.control_string(person['university']):
            university += 1
            temp = False
        if not Validator.control_experience(person['work_experience']):
            work_experience += 1
            temp = False
        if not Validator.control_string(person['political_views']):
            political_view += 1
            temp = False
        if not Validator.control_string(person['worldview']):
            worldview += 1
            temp = False
        if not Validator.control_address(person["address"]):
            address += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out = open(args.output, 'w', encoding='utf-8')
new_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out.write(new_data)
out.close()

print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'Число невалидных адресов электронной почты:  {email}')
print(f'Число невалидных маcc: {weight}')
print(f'Число невалидных CНИЛС: {snils}')
print(f'Число невалидных паспортных номеров: {passport_number}')
print(f'Число невалидных университетов: {university}')
print(f'Число невалидных рабочих стажей: {work_experience}')
print(f'Число невалидных политических взглядов: {political_view}')
print(f'Число невалидных мировоззрений: {worldview}')
print(f'Число невалидных адрессов: {address}')

shell_sort(true_data)
serialization(true_data, args.output_sort)
print(deserialization(args.output_sort))
