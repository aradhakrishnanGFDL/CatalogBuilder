#!/usr/bin/env python

import os
from intakebuilder import gfdlcrawler, CSVwriter, builderconfig
import logging
logger = logging.getLogger('local')
hdlr = logging.FileHandler(builderconfig.logfile)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def main():
    project_dir = builderconfig.project_dir  
    csvfile =  builderconfig.csvfile 
    ######### SEARCH FILTERS ###########################
    dictFilter = builderconfig.dictFilter 
    dictFilterIgnore = builderconfig.dictFilterIgnore
  
    ''' Override config file if necessary for dev
    project_dir = "/archive/oar.gfdl.cmip6/ESM4/DECK/ESM4_1pctCO2_D1/gfdl.ncrc4-intel16-prod-openmp/pp/"
    csvfile =  "/nbhome/a1r/intakebuilder_cats/intake_gfdl2.csv" 
    dictFilterIgnore = {}
    dictFilter["modeling_realm"]= 'atmos_cmip'
    dictFilter["frequency"] = "monthly"
    dictFilter["chunk_freq"] = "5yr"
    dictFilterIgnore["remove"]= 'DO_NOT_USE'
    '''
    #########################################################
    dictInfo = {}
    project_dir = project_dir.rstrip("/")
    logger.info("Calling gfdlcrawler.crawlLocal") 
    list_files = gfdlcrawler.crawlLocal(project_dir, dictFilter, dictFilterIgnore,logger)
    headers = CSVwriter.getHeader()
    if (not os.path.exists(csvfile)):
        os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csvfile)
    print("CSV generated at:", os.path.abspath(csvfile))
    logger.info("CSV generated at"+ os.path.abspath(csvfile))
if __name__ == '__main__':
    main()
