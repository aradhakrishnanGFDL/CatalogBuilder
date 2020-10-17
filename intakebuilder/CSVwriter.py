import csv
from csv import writer

def getHeader():
    '''
    returns header that is the first line in the csv file
    :return: headerlist with all columns
    '''
    headerlist = ["project", "institute", "model", "experiment_id",
                  "frequency", "modeling_realm", "mip_table",
                  "ensemble_member", "grid_label", "variable",
                  "temporal subset", "version", "path"]
    return headerlist
def writeHeader(csvfile):
  '''
  writing header for the csv
  :param csvfile: pass csvfile absolute path
  :return: csv writer object
  '''
  # list containing header values
  headerlist = ["project", "institute", "model", "experiment_id",
                  "frequency", "modeling_realm", "mip_table",
                  "ensemble_member", "grid_label", "variable",
                  "temporal subset", "version", "path"]
    # inputting these headers into a csv
  with open(csvfile, "w+", newline="") as f:
        writerobject = csv.writer(f)
        writerobject.writerow(headerlist)

def file_appender(dictinputs, csvfile):
    '''
    creating function that puts values in dictionary into the csv
    :param dictinputs:
    :param csvfile:
    :return:
    '''
    # opening file in append mode
    with open(csvfile, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # add contents of list as last row in the csv file
        csv_writer.writerow(dictinputs)

def listdict_to_csv(dict_info,headerlist, csvfile):
    try:
        with open(csvfile, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headerlist)
            writer.writeheader()
            for data in dict_info:
                writer.writerow(data)
    except IOError:
        print("I/O error")