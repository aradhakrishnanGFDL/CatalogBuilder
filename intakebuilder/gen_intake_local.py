import os
from intakebuilder import getinfo, localcrawler, CSVwriter

import logging
logger = logging.getLogger('local')
hdlr = logging.FileHandler('/Users/ar46/PycharmProjects/CatalogBuilder/logs/local.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def main():
    #######INPUT HERE OR USE FROM A CONFIG FILE LATER######
    project_dir = "/Users/ar46/data_cmip6/CMIP6/"  # DRS COMPLIANT PROJECT DIR
    csvfile = "/Users/ar46/PycharmProjects/CatalogBuilder/intakebuilder/test/intake_local.csv"
    #######################################################
    ######### SEARCH FILTERS ###########################
    dictFilter = {} #CMIP6 CMIP6/CMIP/NOAA-GFDL/GFDL-ESM4/
    dictFilter["source_prefix"] = 'CMIP6/AerChemMIP/NOAA-GFDL/GFDL-ESM4'  # /CMIP/NOAA-GFDL/GFDL-ESM4/' #Must specify something here, at least the project level
    # COMMENT  dictFilter["miptable"] = "Amon" #Remove this if you don't want to filter by miptable
    # COMMENT dictFilter["varname"] = "tas"   #Remove this if you don't want to filter by variable name
    #######################################################
    dictInfo = {}
    project_dir = project_dir.rstrip("/")
    print("Running")
    list_files = localcrawler.crawlLocal(project_dir, dictFilter,logger)
    headers = CSVwriter.getHeader()
    if (not os.path.exists(csvfile)):
        os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csvfile)
    logger.info("CSV generated at"+ os.path.abspath(csvfile))
    print("CSV generated at:", os.path.abspath(csvfile))


if __name__ == '__main__':
    main()
