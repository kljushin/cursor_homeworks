# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...

import argparse
import csv
import os


def args_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-exp", type=float)
    parser.add_argument("-job_exp", "--current_job_exp", type=float)
    parser.add_argument("-sex")
    parser.add_argument("-city", action='append')
    parser.add_argument("-pos", "--position")
    parser.add_argument("-age", type=int)
    parser.add_argument("-s_path", "--path_to_source_files", required=True)
    parser.add_argument("-s_file", "--source_filename", default='2020_june_mini.csv')
    parser.add_argument("-d_path", "--destination_path", default='.')
    parser.add_argument("-d_fname", "--destination_filename", default='output.csv')

    _args = parser.parse_args()
    if not _args.current_job_exp:
        # current_job_exp; required: false; default: max(current_job_exp)
        _args.current_job_exp = find_max_job_exp(os.path.join(_args.path_to_source_files, _args.source_filename))
    if not _args.exp:
        # exp; required: false; default: min(exp)
        _args.exp = find_min_exp(os.path.join(_args.path_to_source_files, _args.source_filename))

    return _args


def find_min_exp(file_name):
    # exp; required: false; default: min(exp)
    min_exp = float('inf')
    with open(file_name, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            min_exp = min(min_exp, float(row['exp']))
    return min_exp


def find_max_job_exp(file_name):
    # current_job_exp; required: false; default: max(current_job_exp)
    max_exp = float('-inf')
    with open(file_name, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            max_exp = max(max_exp, float(row['current_job_exp']))
    return max_exp


def report_csv(source_filename, dest_filename, param):
    result = []
    fieldnames = []
    with open(source_filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not fieldnames:
                fieldnames = list(row.keys())
            if float(row['exp']) == float(param.exp) and float(row['current_job_exp']) == float(param.current_job_exp):
                _sex = param.sex or row['sex']
                _city = param.city or row['city']
                _position = param.position or row['position']
                _age = param.age or int(row['age'])
                if row['sex'] == _sex and row['city'] in _city and row['position'] == _position and int(row['age']) == _age:
                    result.append(row)

    with open(dest_filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)


if __name__ == '__main__':
    args = args_parse()
    print(args)
    if not os.path.exists(args.destination_path):
        os.makedirs(args.destination_path)
    source_filename = os.path.join(args.path_to_source_files, args.source_filename)
    result_filename = os.path.join(args.destination_path, args.destination_filename)
    report_csv(source_filename, result_filename, args)

# python3 hw12_task1.py -exp 3 -job_exp 2 -sex male --position DevOps -city Kyiv --path_to_source_files . -d_path ./out -d_fname out1.csv
# Output to ./out/out1.csv



