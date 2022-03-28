#!/usr/bin/env python3
import csv
import re
import sys
import operator

def main_unit(file_location):
  number_of_errors = {}
  per_user = {}

  pattern1 = r"ticky: ERROR ([\w'.:,?! ]*).*\(([\w. ]+)\)"
  pattern2 = r"ticky: INFO ([\w'.:,?! ]*).*\(([\w. ]+)\)"

  file = open(file_location).readlines()

  for log in file:
    log = log.strip()
    
    if re.search(pattern1, log):
      data = re.search(pattern1, log)
      err = data[1].strip()
      usr = data[2].strip()
      
      if err not in number_of_errors:
        number_of_errors[err] = 0
      number_of_errors[err] += 1

      if usr not in per_user:
        per_user[usr] = [0, 0]
      per_user[usr][1] += 1

    elif re.search(pattern2, log):
      data = re.search(pattern2, log)
      inf = data[1].strip()
      usr = data[2].strip()
      
      if usr not in per_user:
        per_user[usr] = [0, 0]
      per_user[usr][0] += 1

  number_of_errors = sorted(number_of_errors.items(), key=operator.itemgetter(1), reverse=True)
  per_user = sorted(per_user.items(), key=operator.itemgetter(0))

  return number_of_errors, per_user

def csv_data_writter(num_of_errs, per_user):
  with open('error_message.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Error", "Count"])
    csv_writer.writerows(num_of_errs)
    file.close()

  with open('user_statistics.csv', 'w') as file:
    csv_right = csv.writer(file)
    csv_right.writerow(["Username", "INFO", "ERROR"])
    for data in per_user:
      csv_right.writerow([data[0], data[1][0], data[1][1]])
    file.close()


num_of_errs, per_user = main_unit(sys.argv[1])
csv_data_writter(num_of_errs, per_user)

