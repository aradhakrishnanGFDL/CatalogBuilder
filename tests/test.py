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

    #Get required columns
    req = (j["aggregation_control"]["groupby_attrs"])    
    
    #Validate JSON against JSON template (need to refine this for better validation)
    comp = (diff(j,json_template))
    if(len(comp)>1):
        print("Multiple JSON diffs found")
        print('DIFF:',comp)

    #Get CSV from JSON and open it
    csv_path = j["catalog_file"]

    #with open(csv_path, "r+", newline="") as catalog:
    catalog = pd.read_csv(csv_path)
    
        
    for column in req:
        if(catalog[column].isnull().values.any()):
            print(catalog[column].name, 'contains empty values')
    

    #Read JSON and find optional headers
   
    #Read CSV and verify that all optional headers exists

if __name__ == '__main__':
    main()

