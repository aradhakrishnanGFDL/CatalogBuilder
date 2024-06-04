#!/usr/bin/env python

import click
import json
from jsondiff import diff
import pandas as pd
import sys

@click.command()
@click.argument('json_path', nargs = 1 , required = True)
@click.argument('json_template_path', nargs = 1 , required = False)
@click.option('-tf', '--test-failure', is_flag=True, default = False, help="Errors are only printed. Program will not exit.")
def main(json_path,json_template_path,test_failure):

    #Open JSON
    j = json.load(open(json_path))
    if json_template_path:
        json_template = json.load(open(json_template_path))
    else:
        json_template = json.load(open('cats/gfdl_template.json'))

    #Validate JSON against JSON template
    comp = (diff(j,json_template))
    for key in comp.keys():
        if key != 'catalog_file':
            sys.exit(key, 'section of JSON does not refect template')

    #Get CSV from JSON and open it
    csv_path = j["catalog_file"]
    catalog = pd.read_csv(csv_path)
    
    if len(catalog.index) < 1:
        if test_failure:
            print("Catalog has no values")
        else:
            sys.exit("Catalog has no values")

    #Get required columns
    req = (j["aggregation_control"]["groupby_attrs"])
 
    #Check the csv headers for required columns/values
    errors = 0
    for column in req:
        if column not in catalog.columns:
            print(f"The required column '{column}' does not exist. Double check config file.")
            errors += 1

        if(catalog[column].isnull().values.any()):
            print(f"'{column}' contains empty values.")
            errors += 1
    
    if errors > 0:
        if test_failure:
            print(f"Found {errors} errors.")
        else:
            sys.exit(f"Found {errors} errors.")

if __name__ == '__main__':
    main()

