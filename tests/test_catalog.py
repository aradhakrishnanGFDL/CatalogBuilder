#!/usr/bin/env python

import click
import json
from jsondiff import diff
import csv
import pandas as pd
import sys

@click.command()
@click.argument('json_path', nargs = 1 , required = True)
def main(json_path):

    #Open JSON
    j = json.load(open(json_path))
    json_template = json.load(open('cats/gfdl_template.json'))

    #Validate JSON against JSON template
    comp = (diff(j,json_template))
    for key in comp.keys():
        if key != 'catalog_file':
            sys.exit(key, 'section of JSON does not refect template')

    #Get CSV from JSON and open it
    csv_path = j["catalog_file"]
    catalog = pd.read_csv(csv_path)
   
    #Get required columns
    req = (j["aggregation_control"]["groupby_attrs"])
 
    #Look for empty values under required columns    
    for column in req:
        try:
            if(catalog[column].isnull().values.any()):
                sys.exit(catalog[column].name, 'contains empty values')
        except:
            sys.exit("Can't validate",column, "column. Check for typos.")

if __name__ == '__main__':
    main()

