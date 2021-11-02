import zipfile
import os
import requests
import re
import hashlib

# Задание №1
directory_to_extract_to = 'D:\\Test out'
arch_file = 'D:\\Test\\tiff-4.2.0_lab1.zip'
test_zip = zipfile.ZipFile(arch_file)
test_zip.extractall(directory_to_extract_to)
test_zip.close()

# Задание №2.1
txt_files = []
for r, d, f in os.walk(directory_to_extract_to):
    for name in f:
        if ".txt" in name:
            txt_files.append(r + '\\' + name)  # запись в список файлов txt
print("Список всех файлов с расширением txt\n")
print(txt_files)

# Задание №2.2
result = []
for file in txt_files:
    file_data = open(file, "rb")
    content = file_data.read()
    result.append(hashlib.md5(content).hexdigest())
    file_data.close()
print(result)

# Задание №3
target_hash = '4636f9ae9fef12ebd56cd39586d33cfb'
target_file = []
target_file_data = ''
for r, d, f in os.walk(directory_to_extract_to):
    for name in f:
        file_data = open(r + '\\' + name, "rb")
        content = file_data.read()
        if hashlib.md5(content).hexdigest() == target_hash:
            target_file.append(r + '\\' + name)
            target_file_data = content
        file_data.close()
print("\n", target_file)
print(target_file_data)

# Задание №4
r = requests.get(target_file_data)
result_dct = {}
counter = 0
lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
headers = []
for line in lines:
    if counter == 0:
        headers = re.findall('([А-ЯЁа-яё]+ ?[А-ЯЁа-яё]*)+', line)
        counter += 1
    else:
        temp = re.sub('<.*?>', ';', line)
        temp = re.sub('\(.*?\)', '', temp)
        temp = re.sub(';+', ';', temp)
        temp = re.sub('\s(?=\d)', ' ', temp)
        temp = re.sub('(?<=\d)\s', ' ', temp)
        temp = re.sub('(?<=0)\*', ' ', temp)
        temp = re.sub('_', '--', temp)
        temp = temp[1: len(temp) - 1]
        temp = temp[3::].strip()

        tmp_split = temp.split(';')

        country_name = tmp_split[0]

        col1_val = tmp_split[1]
        col2_val = tmp_split[2]
        col3_val = tmp_split[3]
        col4_val = tmp_split[4]

        result_dct[country_name] = {}
        result_dct[country_name][0] = col1_val
        result_dct[country_name][1] = col2_val
        result_dct[country_name][2] = col3_val
        result_dct[country_name][3] = col4_val

        counter += 1


# Задание №5

output = open('data.csv', 'w')
headline = ';'.join(headers)
output.write('Страна;' + headline + '\n')
for key in result_dct.keys():
    output.write(key + ': ' + result_dct[key][0] + ';' + result_dct[key][1] + ';' + result_dct[key][2] + ';' + result_dct[key][3] + ';' + '\n')

output.close()

# Задание №6

target_country = input("Введите название страны: ")
for key in result_dct.keys():
    if key.lower() == target_country.lower():
        print(key + ':' + str(result_dct[key]))
