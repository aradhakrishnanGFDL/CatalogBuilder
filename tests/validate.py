#!/usr/bin/env python

import click
import json
from jsondiff import diff
import csv
import pandas as pd

@click.command()
@click.argument('json_path',required=True,nargs=1)
@click.argument('json_template',required=True,nargs=1)
def main(json_path,json_template):
    
    #Open JSON
    j = json.load(open(json_path))
    json_template = json.load(open(json_template))
    
    #Validate JSON against JSON template
    comp = (diff(j,json_template))
    for key in comp.keys():
        if key != 'catalog_file':
            print(key, 'section of JSON does not refect template')

    #Get CSV from JSON and open it
    csv_path = j["catalog_file"]
    catalog = pd.read_csv(csv_path)
   
    #Get required columns
    req = (j["aggregation_control"]["groupby_attrs"])
 
    #Look for empty values under required columns    
    for column in req:
        try:
            if(catalog[column].isnull().values.any()):
                print(catalog[column].name, 'contains empty values')
        except:
            print("Can't validate",column, "column. Check for typos.")
    

    #Read JSON and find optional headers
   
    #Read CSV and verify that all optional headers exists

if __name__ == '__main__':
    main()

