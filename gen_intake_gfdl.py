#!/usr/bin/env python

import json
import click
import os
from intakebuilder import gfdlcrawler, CSVwriter, builderconfig
from pathlib import Path
import logging
logger = logging.getLogger('local')
logger.setLevel(logging.INFO)
@click.command()
#TODO arguments dont have help message. So consider changing arguments to options?
@click.argument('input_path',required=True, type=click.Path(exists=True),nargs=1)
#,help='The directory path with the datasets to be cataloged. E.g a GFDL PP path till /pp')
@click.argument('output_path',required=True,nargs=1)
#,help='Specify output filename suffix only. e.g. catalog')
@click.argument('config',required=False,nargs=1)
#,help='Pass the yaml config file; This is not required if you pass input_path and output_path as command-line args')
@click.option('--filter_realm', nargs=1)
@click.option('--filter_freq', nargs=1)
@click.option('--filter_chunk', nargs=1)
@click.option('--overwrite', is_flag=True, default=False)
@click.option('--append', is_flag=True, default=False) 
def main(input_path,output_path,filter_realm,filter_freq,filter_chunk,overwrite,append):
    project_dir = input_path
    csv_path = output_path+".csv"
    json_path = output_path+".json"
 
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
    #for dev csvfile =  "/nbhome/$USER/intakebuilder_cats/intake_gfdl2.csv" 
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

    #Grabbing data from template JSON, changing CSV path to match output path, and dumping data in new JSON
    with open("intakebuilder/templates/gfdl_template.json", "r") as jsonTemplate:
        data = json.load(jsonTemplate)
        data["catalog_file"] = os.path.abspath(csv_path)
    jsonFile = open(json_path, "w")
    json.dump(data, jsonFile, indent=2)
    jsonFile.close()
    headers = CSVwriter.getHeader()

    #When we pass relative path or just the filename the following still needs to not choke
    #so we check if it's a directory first
    if os.path.isdir(os.path.dirname(csv_path)):
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csv_path, overwrite, append)
    print("JSON generated at:", os.path.abspath(json_path))
    print("CSV generated at:", os.path.abspath(csv_path))
    logger.info("CSV generated at"+ os.path.abspath(csv_path))
if __name__ == '__main__':
    main()
