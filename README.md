# CatalogBuilder
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5196586.svg)](https://doi.org/10.5281/zenodo.5196586)

The CatalogBuilder API will collect building blocks necessary to build a data catalog which can then be ingested in climate analysis scripts/workflow, leveraging the use of intake-esm and xarray.

Tested on posix file system, S3 and GFDL post-processed (select simulations, components) at this time. 
This repository has unit tests (pytest) and incorporated the same in GitHub Actions, when a PR is open or a push is initiated.

Two ways To use intakebuilder

[A]
1.setup environment using environment_intake.yml
2. Clone https://github.com/aradhakrishnanGFDL/CatalogBuilder
3. From CatalogBuilder directory, you can import the package. 
4. Test: import intakebuilder
5. See examples in examples directory, gen_intake_gfdl.py, gen_intake_local.py runs on UDA , gen_intake_s3.py  runs on S3 bucket

[B]

1.setup conda environment using environment_intake.yml
conda env create -f environment_intake.yml
2. conda activate intake
3. pip install git+https://github.com/aradhakrishnanGFDL/CatalogBuilder.git
4. Test: import intakebuilder 
5. See examples in examples directory, gen_intake_local.py runs on UDA , gen_intake_s3.py  runs on S3 bucket


[C]

This is specifically for GFDL workstations.
Use branch testgfdl

From GFDL workstations.

1. module load conda
2. Install your own conda  environment by using the environment_intake.yml in the repo OR use the conda environment here by doing 
    conda activate /nbhome/a1r/miniconda3/envs/intake 
3. Checkout the builderconfig.py for input output specifications and edit as needed. Edit the builderconfig.py to add more columns to csv  
4. Run the gen_intake_gfdl.py in the cloned repo and checkout $the csv file generated
5. [Bonus] use intake-esm package to load the csv/json catalog. Refer to examples in this repo under notebooks   
 
