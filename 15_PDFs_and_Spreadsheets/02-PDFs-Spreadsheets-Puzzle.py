import csv
import PyPDF2
import re


def get_url():
    '''
    This will read in the CSV file and get the URL
    It will then return the latest URL
    '''
    csv_file_to_read = open("Exercise_Files\\find_the_link.csv", encoding="utf-8")
    csv_data = csv.reader(csv_file_to_read)
    data_lines = list(csv_data)
    character_map = 0
    found_url = ""
    url_list = []
    for line in data_lines:
        url_list.append(line[character_map])
        character_map += 1
    for character in url_list:
        found_url = found_url + character
    return found_url


def parse_pdf():
    '''
    Open the PDF
    Parse it
    find the phone number
    '''
    ph_num_patt = r'\d{3}.\d{3}.\d{4}'
    pdf_file = open('Exercise_Files\\Find_the_Phone_Number.pdf', 'rb')

    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()
        if re.search(ph_num_patt, page_text):
            match = re.search(ph_num_patt, page_text)
            print(match.group())


if __name__ == "__main__":
    url = get_url()
    parse_pdf()
