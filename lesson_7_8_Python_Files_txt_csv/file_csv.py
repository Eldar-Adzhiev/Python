import csv

#  Сгенерировали список и добавили в список
# file_path = 'C:/Users/eadzh/Documents/QA/Python/lesson_7_Python_Files_txt_csv/'
# file_name = 'csv_lesson_7.csv'
# csv_file_name = file_path +file_name

# nane_age = []
#
# users_list = [
#     ['Vadim', 32],
#     ['Alexey', 34],
#     ['Julia', 19]
# ]
#
# new_users_list = []
#
# for item in range(0, 100):
#
#     for ul_item in users_list:
#
#         name_age = []
#
#         new_name = ul_item[0] + '_' + str(item)
#
#         new_age = 10 + item
#         name_age.append(new_name)
#         name_age.append(new_age)
#
#         new_users_list.append(name_age)
#
# for ii in new_users_list:
#     print(ii)
#
# with open(csv_file_name, 'w') as cf:
#     writer = csv.writer(cf)
#
#     writer.writerows(new_users_list)

#===================================================================

# Добавление одной строчки
# with open(csv_file_name, 'a') as csv_f: # Добавление одной строчки
#     writer = csv.writer(csv_f)
#
#     row_1 = ['Vlas', 25]
#
#     writer.writerow(row_1)

#======================================================================

# CSV  with headers
# file_path = 'C:/Users/eadzh/Documents/QA/Python/lesson_7_Python_Files_txt_csv/'
# file_name = 'csv_file_2.csv'
# csv_file_name = file_path +file_name
#
#
# users_list = [
#     ['Vadim', 32],
#     ['Alexey', 34],
#     ['Julia', 19]
# ]
#
# new_users_list = []
#
# with open(csv_file_name, 'w') as cf:
#     columns = ['name', 'age']
#     writer = csv.DictWriter(cf,fieldnames=columns)
#     writer.writeheader()
#
#     # writer.writerow(users_list)
#
#     row_1 = {'name': 'Vlas', 'age': 25}
#
#     writer.writerow(row_1)

#=========================================================================

# Read CSV Files
# file_path = 'C:/Users/eadzh/Documents/QA/Python/lesson_7_Python_Files_txt_csv/'
# file_name = 'csv_file_2.csv'
# csv_file_name = file_path +file_name
#
# with open(csv_file_name, 'r') as csv_f:
#
#     reader= csv.DictReader(csv_f)
#     line_count = 0
#
#     age_list = []
#
#     for row in reader:
#         # print(row['name'], row['age'])
#         # print(row)
#
#         age_list.append(int(row['age']))
#
#     print(age_list)