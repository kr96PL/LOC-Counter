import os
import time

def getFilesToCount(allowed_extensions, scripts_folder_path):
    if not os.path.exists(scripts_folder_path):
        print("Folder: " + scripts_folder_path + " doesn't exist")
        exit()

    files_to_count = []
    files = os.listdir(scripts_folder_path)

    for file_name in files:
        for ext in allowed_extensions:
            if file_name.find(ext) == (len(file_name) - len(ext)):    
                files_to_count.append(scripts_folder_path + "/" + file_name)

    return files_to_count

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

def run(allowed_extensions, scripts_folder_path):
    loc = 0
    files = getFilesToCount(allowed_extensions, scripts_folder_path)
    for f in files:
        loc += countLinesInFile(f)
    
    return loc

cannot_continue = True
allowed_extensions = None
scripts_folder_path = None

while cannot_continue:
    input_extensions = input("Enter after the decimal point the file extensions for which you want to calculate LOC: ").replace(" ", "")
    input_path = input("Enter the path to the folder with the scripts: ")
    
    if len(input_extensions) > 0 and len(input_path) > 0:
        allowed_extensions = input_extensions.split(",")
        scripts_folder_path = input_path
        break
    else:
        print("Musisz wypełnić wszystkie pola")


print(run(allowed_extensions, scripts_folder_path))
input("Press enter to exit...")