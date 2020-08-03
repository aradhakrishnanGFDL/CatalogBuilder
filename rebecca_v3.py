# overview: 1st function takes files out of dir and puts in list
# 2nd function splits the files by _
# 3rd function puts them into a dictionary
# creating empty list for files to be appended into later
import os
# now going to add the dictionaries into a csv file- function 5
from csv import writer
list_files = []

# creating function that takes the files in list and splits them by _ - function 2
def splitlist(filename):
    splitfile = filename.split("_")
    return (splitfile)


# creating function that inputs variables for split lists ^ and puts it into a function- function 3
# grid label isnt in the csv file so i took it out of the dictionary
def dicting(list):
    dict = {"project": "", "institute": "", "model": list[2], "experiment": list[3], "frequency": "",
            "modeling_realm": "", "mip_table": list[1], "ensemble_member": list[4], "grid_label": list[5],
            "variable": list[0],
            "temporal subset": list[6], "version": "", "path": ""}
    return dict

# going to get values from dict-function 4
def getvalues(dictname):
    return dictname.values()

def file_appender(csvfile, dictinputs):
    # Open file in append mode
    with open(csvfile, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(dictinputs)

#MOVE THE FOLLOWING TO MAIN IF THIS IS NOT PART OF THE ABOVE FUNCTION
# now going to input file one
csvappendf1 = getvalues(dicting(list1))
file_appender("headertemplateinput.csv", csvappendf1)
# now going to input file two
csvappendf2 = getvalues(dicting(list2))
file_appender("headertemplateinput.csv", csvappendf2)


# checking to see if csv file is updated and includes both files as input
# nvm oops II  printed the keys into CSV and not the values

# starting main function that takes files out of dir- function 1
def main():
    print('Get started: list files in a given directory')
    # input dir structure
    drs_structure = r'C:\Users\Rebecca\data_cmip6'
    # pulling files from dir in drs_structure and sorting nc only
    for dir_path, dirs, files in os.walk(drs_structure):
        for filename in files:
            filename = os.path.join(filename)
            if filename.endswith('.nc'):
                filename_split = filename.split(".")
                # taking out the nc
                filename_split = filename_split[0]
                # put the files into list_files
                list_files.append(filename_split)

#MOVE THE FOLLOWING TO MAIN IF THIS IS NOT PART OF ANY OTHER FUNCTION

# making each file in list_files a sep list
list1 = splitlist(list_files[0])
list2 = splitlist(list_files[1])
# printing out dicts created with dicting with each file
print(dicting(list1))
print(dicting(list2))

if __name__ == '__main__':
    main()
