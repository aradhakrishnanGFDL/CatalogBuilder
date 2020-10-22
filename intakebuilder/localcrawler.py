import os
from intakebuilder import getinfo
'''
localcrawler crawls through the local file path, then calls helper functions in the package to getinfo.
It finally returns a list of dict
'''

def crawlLocal(projectdir, dictInfo):
    '''
    Craw through the local directory and run through the getInfo.. functions
    :param projectdir:
    :return:listfiles which has a dictionary of all key/value pairs for each file to be added to the csv
    '''
    listfiles = []
    for dirpath, dirs, files in os.walk(projectdir):
        for filename in files:
            dictInfo = {}
            getinfo.getProject(projectdir, dictInfo)
            # get info from filename
            print(filename)
            filepath = os.path.join(dirpath,filename)  # 1 AR: Bugfix: this needs to join dirpath and filename to get the full path to the file
            dictInfo["path"]=filepath
#            print("Calling getinfo.getInfoFromFilename(filename, dictInfo)..")
            dictInfo = getinfo.getInfoFromFilename(filename, dictInfo)
#            print("Calling getinfo.getInfoFromDRS(dirpath, projectdir, dictInfo)")
            dictInfo = getinfo.getInfoFromDRS(dirpath, projectdir, dictInfo)
#            print("Calling getinfo.getInfoFromGlobalAtts(filepath, dictInfo)")
            dictInfo = getinfo.getInfoFromGlobalAtts(filepath, dictInfo)
            listfiles.append(dictInfo)
            print(listfiles)
    return listfiles
