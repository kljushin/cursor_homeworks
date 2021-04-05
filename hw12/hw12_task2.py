# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language
#
# Based on this info generate a new report of average salary.
import argparse
import csv
import os


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-so", "--source_file_path", required=True)
    parser.add_argument("-ss", "--start_salary", type=float, help='Starting point of salary')
    parser.add_argument("-es", "--end_salary", type=float, help='The max point of salary')
    parser.add_argument("-pos", "--position", help='Position role')
    parser.add_argument("-age", type=int, help='Age of person')
    parser.add_argument("-lan", "--language", help='Programming language')

    return parser.parse_args()


def report(filename, param):
    with open(filename, newline='') as f:
        quantity = 0
        result = 0
        reader = csv.DictReader(f)
        for row in reader:
            _start = param.start_salary or float(row['salary'])
            _end = param.end_salary or float(row['salary'])
            _pos = param.position or row['position']
            _age = param.age or int(row['age'])
            _lan = param.language or row['language']
            if _start <= float(row['salary']) <= _end:
                if row['position'] == _pos and int(row['age']) == _age and row['language'] == _lan:
                            quantity += 1
                            result += float(row['salary'])
    if quantity:
        result = round(result / quantity, 2)
    else:
        result = 0
    with open('report.txt', 'w') as f:
        print(
            f'Average salary for parameters start_salary = {param.start_salary} end_salary = {param.end_salary} '
            f'position = {param.position} age = {param.age} '
            f'language = {param.language} is'
            f' {result}', file=f)


if __name__ == '__main__':
    args = arg_parse()
    print(args)
    report(args.source_file_path, args)

# python3 hw12_task2.py -so ./2020_june_mini.csv -ss 5500 -es 10000 -pos "System Architect" -age 34 -lan Python
# Output to report.txt
