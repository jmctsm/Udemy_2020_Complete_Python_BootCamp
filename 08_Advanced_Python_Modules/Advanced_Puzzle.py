import zipfile
import os
import re
import send2trash
# import time

# start_time = time.time()
def parse_file(location_of_file, patter_to_find):
    parsing_file = open(location_of_file, 'r')
    text = parsing_file.read()

    if re.search(patter_to_find, text):
        print("Pattern found.")
        print(location_of_file)
        print(text)

zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
zip_obj.extractall("extracted_content")

with open('extracted_content\\extracted_content\\Instructions.txt') as file_instructions:
    content = file_instructions.read()
    print(content)

phone_pattern = r'\d{3}-\d{3}-\d{4}'

main_folder = 'extracted_content\\extracted_content'
for folder, sub_folders, files in os.walk(main_folder):
    for sub_folder in sub_folders:
        new_location = main_folder + '\\' + sub_folder
        for main_sub_folders, secondary_sub_folders, secondary_files in os.walk(new_location):
            for secondary_file in secondary_files:
                file_location = ""
                if secondary_file != "Instructions.txt":
                    file_location = new_location + '\\' + secondary_file
                    parse_file(file_location, phone_pattern)

trash_folder = 'extracted_content'
send2trash.send2trash(trash_folder)

# end_time = time.time()
# print(end_time - start_time)

####  Example way of doing this instead

# start_time = time.time()
import shutil
shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)
pattern = r'\d{3}-\d{3}-\d{4}'


def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


results = []
for folder, sub_folders, files in os.walk(os.getcwd() + "\\extracted_content"):

    for f in files:
        full_path = folder + '\\' + f

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())


trash_folder = 'extracted_content'
send2trash.send2trash(trash_folder)



# end_time = time.time()
# print(end_time - start_time)




