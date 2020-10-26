import os
from intakebuilder import getinfo
import re
'''
localcrawler crawls through the local file path, then calls helper functions in the package to getinfo.
It finally returns a list of dict
'''
def crawlLocal(projectdir, dictFilter,dictInfo):
    '''
    Craw through the local directory and run through the getInfo.. functions
    :param projectdir:
    :return:listfiles which has a dictionary of all key/value pairs for each file to be added to the csv
    '''
    listfiles = []
    pat = None
    if("miptable" in dictFilter.keys()) & (("varname") in dictFilter.keys()):
        pat = re.compile('({}/{}/)'.format(dictFilter["miptable"],dictFilter["varname"]))
    elif("miptable" in dictFilter.keys()):
        pat = re.compile('({}/)'.format(dictFilter["miptable"]))
    elif(("varname") in dictFilter.keys()):
        pat = re.compile('({}/)'.format(dictFilter["varname"]))
    orig_pat = pat
    for dirpath, dirs, files in os.walk(projectdir):
        #print(dirpath, dictFilter["source_prefix"])
        if(dictFilter["source_prefix"] in dirpath): #TODO improved filtering 
            searchpath = dirpath 
            if (orig_pat is None):
                pat = dirpath  #we assume matching entire path
          #  print("Search filters applied", dictFilter["source_prefix"], "and", pat)
            if(pat is not None):
                m = re.search(pat, searchpath)
                for filename in files:
                   print(filename)

                   dictInfo = {}
                   dictInfo = getinfo.getProject(projectdir, dictInfo)
                   # get info from filename
                   #print(filename)
                   filepath = os.path.join(dirpath,filename)  # 1 AR: Bugfix: this needs to join dirpath and filename to get the full path to the file
                   dictInfo["path"]=filepath
#                  print("Calling getinfo.getInfoFromFilename(filename, dictInfo)..")
                   dictInfo = getinfo.getInfoFromFilename(filename, dictInfo)
#                  print("Calling getinfo.getInfoFromDRS(dirpath, projectdir, dictInfo)")
                   dictInfo = getinfo.getInfoFromDRS(dirpath, projectdir, dictInfo)
#                  print("Calling getinfo.getInfoFromGlobalAtts(filepath, dictInfo)")
#                  dictInfo = getinfo.getInfoFromGlobalAtts(filepath, dictInfo)
                   listfiles.append(dictInfo)
                   #print(listfiles)
    return listfiles
