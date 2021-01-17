import csv


def line_break():
    for x in range(0,25):
        print("*", end="")
    print("\n")

# Reading CSV Files
line_break()
data = open("example.csv", encoding="utf-8")
print(data)

# Encoding
line_break()
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)
print(data_lines[:3])
for line in data_lines[:5]:
    print(line)

print(len(data_lines))
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])
print(all_emails)

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])
print(full_names)


# Writing to CSV Files
line_break()

# New File
line_break()
# newline controls how universal newlines works (it only applies to text
# mode).  It can be None, '', '\n', '\r', and '\r\n'
file_to_output = open('to_save_file.csv', 'w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()

# Existing File
line_break()
f = open('to_save_file.csv', 'a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new', 'new', 'new'])
f.close()
