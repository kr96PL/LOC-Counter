import os

loc = 0
cannot_continue = True
allowed_extensions = None
scripts_folder_path = None

def countLinesInFile(file_path):
    if not os.path.exists(file_path):
        print("File: " + file_path + " doesn't exist")
        exit()
    f = open(file_path, "r")
    lines_number = 0
    multi_line_comment_founded = False
    for line in f: 
        line_wo_whitespaces = line.strip()
        if len(line_wo_whitespaces) > 0:
            if line_wo_whitespaces.find("/*") == 0:
                multi_line_comment_founded = True
                continue
            if multi_line_comment_founded:
                if line_wo_whitespaces.find("*/") == 0:
                    multi_line_comment_founded = False
                continue
            if line_wo_whitespaces.find("//") == 0:
                continue

            lines_number += 1
    
    return lines_number

def scan_dir(path):
    global loc
    global allowed_extensions
    x = os.scandir(path)
    for e in x:
        if not e.is_dir() and e.is_file:
            for ext in allowed_extensions:
                if e.name.find(ext) == (len(e.name) - len(ext)):  
                    loc += countLinesInFile(e.path)
            continue
        scan_dir(e.path) 

def run(scripts_folder_path):
    scan_dir(scripts_folder_path)
    return loc

while cannot_continue:
    input_extensions = input("Enter after the decimal point the file extensions for which you want to calculate LOC: ").replace(" ", "")
    input_path = input("Enter the path to the folder with the scripts: ")
    
    if len(input_extensions) > 0 and len(input_path) > 0:
        allowed_extensions = input_extensions.split(",")
        scripts_folder_path = input_path
        break
    else:
        print("Don't leave any blanks.")


print("LOC: " + str(run(scripts_folder_path)))
input("Press enter to exit...")



