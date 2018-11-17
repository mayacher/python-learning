import os
import datetime
import glob

files_list=[]
lines=[]


# get the files to read from
def getfiles():
    files = glob.glob("file*.txt")
    return files


# read the contents from the files
def readfile():
    files_list=getfiles()
    for file in files_list:
        with open(file) as f:
            for line in f:
                lines.append(line)
    return lines

# create the new file
def create_file():
    date_file = datetime.datetime.now()
    date_name = date_file.strftime("%y-%m-%d-%H-%M-%S-%f")
    file_name = str(date_name) + ".txt"
    open(file_name, "w").close()
    return file_name

# write content from the old file
def write_to_file():
    get_lines = readfile()
    file_name = create_file()
    with open(file_name, "w") as f:
        for i in get_lines:
            f.write(str(i) + "\n")



if __name__== "__main__":
  print getfiles()

