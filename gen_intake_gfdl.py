#!/usr/bin/env python

import os
from intakebuilder import gfdlcrawler, CSVwriter
import logging
logger = logging.getLogger('local')
hdlr = logging.FileHandler('/nbhome/a1r/logs/local.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def main():
    #######INPUT HERE OR USE FROM A CONFIG FILE LATER######
#   project_dir = "/Users/ar46/data_cmip6/CMIP6/"  # DRS COMPLIANT PROJECT DIR
    project_dir = "/archive/oar.gfdl.cmip6/ESM4/DECK/ESM4_1pctCO2_D1/gfdl.ncrc4-intel16-prod-openmp/pp/"
    #CMIP/NOAA-GFDL/GFDL-ESM4/"
    csvfile = "/nbhome/a1r/intakebuilder_cats/intake_gfdl.csv" ##"/Users/ar46/PycharmProjects/CatalogBuilder/intakebuilder/test/intake_local.csv"
    #######################################################
    ######### SEARCH FILTERS ###########################
    dictFilter = {}
    dictFilterIgnore = {}
    dictFilter["modeling_realm"]= 'atmos_cmip'
    dictFilter["frequency"] = "monthly"
    dictFilter["chunk_freq"] = "5yr"
    dictFilterIgnore["remove"]= 'DO_NOT_USE'
   #COMMENT  dictFilter["miptable"] = "Amon" #Remove this if you don't want to filter by miptable
   #COMMENT dictFilter["varname"] = "tas"   #Remove this if you don't want to filter by variable name
    #########################################################
    dictInfo = {}
    project_dir = project_dir.rstrip("/")
    logger.info("Calling gfdlcrawler.crawlLocal") 
  #  print("Calling gfdlcrawler.crawlLocal")
    list_files = gfdlcrawler.crawlLocal(project_dir, dictFilter, dictFilterIgnore,logger)
  # print(list_files)

    headers = CSVwriter.getHeader()
    if (not os.path.exists(csvfile)):
        os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csvfile)
    print("CSV generated at:", os.path.abspath(csvfile))
    logger.info("CSV generated at"+ os.path.abspath(csvfile))
if __name__ == '__main__':
    main()
