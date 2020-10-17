import re
import boto3
from intakebuilder import getinfo

'''
s3 crawler crawls through the S3 bucket, passes the bucket path to the helper functions to getinfo.
Finally it returns a list of dictionaries. 
'''
def sss_crawler(projectdir,dictFilter, dictInfo):
    s3client = boto3.client('s3')
    s3prefix = "s3:/"
    filetype = ".nc"
    project_bucket = projectdir.split("/")[2]
    #######################################################
    listfiles = []
    pat = None
    print(dictFilter.keys())
    if("miptable" in dictFilter.keys()) & (("varname") in dictFilter.keys()):
        pat = re.compile('({}/{}/)'.format(dictFilter["miptable"],dictFilter["varname"]))
    elif("miptable" in dictFilter.keys()):
        pat = re.compile('({}/)'.format(dictFilter["miptable"]))
    elif(("varname") in dictFilter.keys()):
        pat = re.compile('({}/)'.format(dictFilter["varname"]))
    paginator = s3client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=project_bucket, Prefix=dictFilter["source_prefix"], Delimiter=filetype):
        for prefixes in result.get('CommonPrefixes'):
            commonprefix = prefixes.get('Prefix')
            searchpath = commonprefix
            #filepath = '{}/{}/{}'.format(s3prefix,project_bucket,commonprefix)
            print("Search filters applied", dictFilter["source_prefix"], "and", pat)

            if(pat is not None):
                m = re.search(pat, searchpath)
                if m is not None:
                        #print(commonprefix)
                        #print('{}/{}/{}'.format(s3prefix,project_bucket,commonprefix))
                        filepath = '{}/{}/{}'.format(s3prefix,project_bucket,commonprefix)
                        #TODO if filepath already exists in csv we skip
                        dictInfo["path"]=filepath
                        filename = filepath.split("/")[-1]
                        dirpath = "/".join(filepath.split("/")[0:-1])
                        #projectdir passed to sss_crawler should be s3://bucket/project
                        dictInfo = getinfo.getInfoFromFilename(filename, dictInfo)
                        dictInfo = getinfo.getInfoFromDRS(dirpath, projectdir, dictInfo)
                        #Using YAML instead of this to get frequency and modeling_realm  dictInfo = getinfo.getInfoFromGlobalAtts(filepath, dictInfo)
                        #TODO YAML for all mip_tables
                        getinfo.getinfoFromYAML(dictInfo,"table.yaml",miptable=dictInfo["mip_table"])
                        listfiles.append(dictInfo)
            print(listfiles)
    return listfiles