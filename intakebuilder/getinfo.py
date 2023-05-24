import sys
import pandas as pd
import csv
from csv import writer
import os
import xarray as xr
import shutil as sh
from intakebuilder import builderconfig 

'''
getinfo.py provides helper functions to get information (from filename, DRS, file/global attributes) needed to populate the catalog
'''
def getProject(projectdir,dictInfo):
    '''
    return Project name from the project directory input
    :type dictInfo: object
    :param drsstructure:
    :return: dictionary with project key
    '''
    if ("archive" in projectdir or "pp" in projectdir): 
       project = "dev" 
    else: 
       projectdir.split("/")[-1]
    dictInfo["activity_id"]=project
    return dictInfo
def getinfoFromYAML(dictInfo,yamlfile,miptable=None):
    import yaml
    with open(yamlfile) as f:
        mappings = yaml.load(f, Loader=yaml.FullLoader)
        #print(mappings)
        #for k, v in mappings.items():
              #print(k, "->", v)
        if(miptable):
            try:
                dictInfo["frequency"] = mappings[miptable]["frequency"]
            except KeyError:
                dictInfo["frequency"] = "NA"
            try:
                dictInfo["modeling_realm"] = mappings[miptable]["modeling_realm"]
            except KeyError:
                dictInfo["modeling_realm"]  = "NA"
    return(dictInfo)

def getStem(dirpath,projectdir):
    '''
    return stem from the project directory passed and the files crawled within
    :param dirpath:
    :param projectdir:
    :param stem directory:
    :return:
    '''
    stemdir = dirpath.split(projectdir)[1].split("/")  # drsstructure is the root
    return stemdir


def getInfoFromFilename(filename,dictInfo,logger):
    # 5 AR: get the following from the netCDF filename e.g.rlut_Amon_GFDL-ESM4_histSST_r1i1p1f1_gr1_195001-201412.nc
    if(filename.endswith(".nc")):
        ncfilename = filename.split(".")[0].split("_")
        varname = ncfilename[0]
        dictInfo["variable"] = varname
        miptable = ncfilename[1]
        dictInfo["mip_table"] = miptable
        modelname = ncfilename[2]
        dictInfo["model"] = modelname
        expname = ncfilename[3]
        dictInfo["experiment_id"] = expname
        ens = ncfilename[4]
        dictInfo["ensemble_member"] = ens
        grid = ncfilename[5]
        dictInfo["grid_label"] = grid
        try:
           tsubset = ncfilename[6]
        except IndexError:
           tsubset = "null" #For fx fields
        dictInfo["temporal_subset"] = tsubset
    else:
        logger.debug("Filename not compatible with this version of the builder:"+filename)
    return dictInfo

def getInfoFromGFDLFilename(filename,dictInfo,logger):
    # 5 AR: get the following from the netCDF filename e.g. atmos.200501-200912.t_ref.nc
    if(filename.endswith(".nc")):
        ncfilename = filename.split(".")
        varname = ncfilename[-2]
        dictInfo["variable_id"] = varname
        #miptable = "" #ncfilename[1]
        #dictInfo["mip_table"] = miptable
        #modelname = ncfilename[2]
        #dictInfo["model"] = modelname
        #expname = ncfilename[3]
        #dictInfo["experiment_id"] = expname
        #ens = ncfilename[4]
        #dictInfo["ensemble_member"] = ens
        #grid = ncfilename[5]
        #dictInfo["grid_label"] = grid
        try:
           tsubset = ncfilename[1]
        except IndexError:
           tsubset = "null" #For fx fields
        dictInfo["temporal_subset"] = tsubset
    else:
        logger.debug("Filename not compatible with this version of the builder:"+filename)
    return dictInfo

def getInfoFromGFDLDRS(dirpath,projectdir,dictInfo):
    '''
    Returns info from project directory and the DRS path to the file
    :param dirpath:
    :param drsstructure:
    :return:
    '''
   # we need thise dict keys "project", "institute", "model", "experiment_id",
   #               "frequency", "modeling_realm", "mip_table",
   #               "ensemble_member", "grid_label", "variable",
   #               "temporal subset", "version", "path"]
 
#/archive/oar.gfdl.cmip6/ESM4/DECK/ESM4_historical_D1/gfdl.ncrc4-intel16-prod-openmp/pp/atmos/ts/monthly/5yr/DO_NOT_USE/atmos.201001-201412.alb_sfc.nc

    stemdir = dirpath.split("/") 
    nlen = len(builderconfig.output_path_template)
    #lets go backwards and match given input directory to the template, add things to dictInfo 
    for i in range(1,nlen+1):
      try:
          dictInfo[builderconfig.output_path_template[nlen-i]] = stemdir[-i]
      except:
          sys.exit("oops in getInfoFromGFDLDRS")
    return dictInfo

def getInfoFromDRS(dirpath,projectdir,dictInfo):
    '''
    Returns info from project directory and the DRS path to the file
    :param dirpath:
    :param drsstructure:
    :return:
    '''
    stemdir = getStem(dirpath, projectdir)
    #stemdir = dirpath.split(projectdir)[1].split("/")  # drsstructure is the root
    try:
        institute = stemdir[2]
    except:
            institute = "NA"
    try:
        version = stemdir[9]
    except:
        version = "NA"
    dictInfo["institute"] = institute
    dictInfo["version"] = version
    return dictInfo
def return_xr(fname):
    filexr = (xr.open_dataset(fname))
    filexra = filexr.attrs
    return filexra
def getInfoFromGlobalAtts(fname,dictInfo,filexra=None):
    '''
    Returns info from the filename and xarray dataset object
    :param fname: DRS compliant filename
    :param filexr: Xarray dataset object
    :return: dictInfo with institution_id version realm frequency and product
    '''
    filexra = return_xr(fname)
    if dictInfo["institute"] == "NA":
      try:
          institute = filexra["institution_id"]
      except KeyError:
          institute = "NA"
      dictInfo["institute"] = institute
    if dictInfo["version"] == "NA":
        try:
            version = filexra["version"]
        except KeyError:
            version = "NA"
        dictInfo["version"] = version
    realm = filexra["realm"]
    dictInfo["modeling_realm"] = realm
    frequency = filexra["frequency"]
    dictInfo["frequency"] = frequency
    return dictInfo

