#project_dir = "/Users/ar46/data_cmip6/CMIP6/"  # DRS COMPLIANT PROJECT DIR
project_dir = "/archive/oar.gfdl.cmip6/ESM4/DECK/ESM4_1pctCO2_D1/gfdl.ncrc4-intel16-prod-openmp/pp/"

#/archive/oar.gfdl.cmip6/ESM4/DECK/ESM4_1pctCO2_D1/gfdl.ncrc4-intel16-prod-openmp/pp/atmos/ts/monthly/5yr/atmos.014601-015012.evap.nc 

#what kind of directory structure to expect? 

output_path_template = ['source_id','activity_id','experiment_id','platform','custom_pp','modeling_realm','custom_cell_methods','frequency','chunk_freq']

output_file_template = ['modeling_realm','temporal_subset','variable_id']

#catalog headers 

headerlist = ["activity_id", "institution_id", "source_id", "experiment_id",
                  "frequency", "modeling_realm", "table_id",
                  "member_id", "grid_label", "variable_id",
                  "temporal_subset", "chunk_freq","grid_label","platform","dimensions","cell_methods","path"]

#OUTPUT FILE  

csvfile = "/nbhome/a1r/intakebuilder_cats/intake_gfdl.csv" 
logfile = "/tmp/intakegfdl.log"
#######################################################
######### ADDITIONAL SEARCH FILTERS ###########################

dictFilter = {}
dictFilterIgnore = {}
dictFilter["modeling_realm"]= 'atmos_cmip'
dictFilter["frequency"] = "monthly"
dictFilter["chunk_freq"] = "5yr"
dictFilterIgnore["remove"]= 'DO_NOT_USE'
