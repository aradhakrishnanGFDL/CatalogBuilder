#!/usr/bin/env python

import click
import os
from intakebuilder import gfdlcrawler, CSVwriter, builderconfig
import logging
logger = logging.getLogger('local')
logger.setLevel(logging.INFO)

#Setting up argument parsing/flags
@click.command()
@click.argument("inputdir", required=True, nargs=1) 
@click.argument("outputdir", required=True, nargs=1)
@click.option('--filter_realm', nargs=1)
@click.option('--filter_freq', nargs=1)
@click.option('--filter_chunk', nargs=1)
@click.option('--overwrite', is_flag=True, default=False)
@click.option('--append', is_flag=True, default=False) 
def main(inputdir,outputdir,filter_realm,filter_freq,filter_chunk,overwrite,append):
    project_dir = inputdir
    csvfile = outputdir
   
    ######### SEARCH FILTERS ###########################
    
    dictFilter = {}
    dictFilterIgnore = {}
    if filter_realm:
        dictFilter["modeling_realm"] = filter_realm
    if filter_freq:
        dictFilter["frequency"] = filter_freq
    if filter_chunk:
        dictFilter["chunk_freq"] = filter_chunk

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
    CSVwriter.listdict_to_csv(list_files, headers, csvfile, overwrite, append)
    print("CSV generated at:", os.path.abspath(csvfile))
    logger.info("CSV generated at"+ os.path.abspath(csvfile))
if __name__ == '__main__':
    main()
