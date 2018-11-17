import os
import datetime
import glob


# get the files to read from
class merge_files:

    files_pattern = None

    # def __init__(self):
    #     self.readfile = readfile

    def getfiles(self, files_pattern):
        files = glob.glob(files_pattern)
        return files


    # read the contents from the files
    def readfile(self, files_pattern):
        lines = []
        files_list = self.getfiles(files_pattern)
        for file in files_list:
            with open(file) as f:
                for line in f:
                    lines.append(line)
        return lines

    # create the new file
    def create_file(self):
        date_file = datetime.datetime.now()
        date_name = date_file.strftime("%y-%m-%d-%H-%M-%S-%f")
        file_name = str(date_name) + ".txt"
        open(file_name, "w").close()
        return file_name

    # write content from the old file
    def write_to_file(self, files_pattern):
        get_lines = self.readfile(files_pattern)
        file_name = self.create_file()
        with open(file_name, "w") as f:
            for i in get_lines:
                f.write(str(i) + "\n")
        print str(file_name) + " was written"




if __name__ == "__main__":
    file = merge_files()
    file_create = file.write_to_file("file*.txt")
