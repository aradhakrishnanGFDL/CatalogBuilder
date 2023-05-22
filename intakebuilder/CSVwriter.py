import csv
from csv import writer
from intakebuilder import catalogcols
def getHeader():
    '''
    returns header that is the first line in the csv file, refers catalogcols.py
    :return: headerlist with all columns
    '''
    #TODO move headerlist outside in a separate configuration or 
    #headerlist = ["activity_id", "institution_id", "source_id", "experiment_id",
    #              "frequency", "modeling_realm", "table_id",
    #              "member_id", "grid_label", "variable_id",
    #              "temporal_subset", "chunk_freq","grid_label","platform","dimensions","cell_methods","path"]
    return catalogcols.headerlist
def writeHeader(csvfile):
  '''
  writing header for the csv
  :param csvfile: pass csvfile absolute path
  :return: csv writer object
  '''
  # list containing header values
  # inputting these headers into a csv
  with open(csvfile, "w+", newline="") as f:
        writerobject = csv.writer(f)
        writerobject.writerow(catalogcols.headerlist)

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
            print("writing..")
            writer.writeheader()
            for data in dict_info:
                writer.writerow(data)
    except IOError:
        print("I/O error")
