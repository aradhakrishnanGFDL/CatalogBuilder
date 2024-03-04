How to generate 
===============

There are a few ways to use the catalog builder.

GFDL Workstation Usage
----------------------

1. module load conda python 

2. Install your own conda environment using intakebuilder/environment_intake.yml OR conda activate /nbhome/a1r/miniconda3/envs/intake

3. Checkout the builderconfig.py for input output specifications and edit as needed. Edit the builderconfig.py to add more columns to csv

4. Run the gen_intake_gfdl.py in the cloned repo and checkout $the csv file generated

[Bonus] use intake-esm package to load the csv/json catalog. Refer to examples in this repo under notebooks

(Title TBD)
-----------
To work with GFDL PP data, please use the following instructions as we refine the instructions and code base to be more unified.

module load conda

Install your own conda environment by using the environment_intake.yml in the repo OR use the conda environment here by doing
conda env create -f environment_intake.yml conda activate [new_env]

You can also activate this environment directly for testing: conda activate /nbhome/a1r/miniconda3/envs/intake

git clone this repository.

Run the gen_intake_gfdl.py in the cloned repo with the PP directory as the first argument and the name of the output file as the second.

The following example generates a sample catalog called output.csv to the home directory: /gen_intake_gfdl.py /archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp /archive/am5/am5/am5f3b1r0/c96L65_am5f3b1r0_pdclim1850F/gfdl.ncrc5-deploy-prod-openmp/pp/output

The above creates an output.csv and an output.json.

Additional flags

In order to overwrite any existing CSV file at the given output path, the '--overwrite' flag can be used. In order to append any existing CSV file at the given output path, the '--append' flag can be used.

The catalog builder wrapper accepts two arguments: an input path where data is stored and an output path to which the final CSV file will be generated.

NOTE: Currently only time series output files are included in output CSV.

External Usage (non-GFDL)
-------------------------

[A] 1.setup environment using environment_intake.yml 2. Clone https://github.com/aradhakrishnanGFDL/CatalogBuilder 3. From CatalogBuilder directory, you can import the package. 4. Test: import intakebuilder 5. See examples in examples directory, gen_intake_gfdl.py, gen_intake_local.py runs on UDA , gen_intake_s3.py runs on S3 bucket

or

[B] 1.setup conda environment using environment_intake.yml conda env create -f environment_intake.yml 2. conda activate intake 3. pip install git+https://github.com/aradhakrishnanGFDL/CatalogBuilder.git 4. Test: import intakebuilder 5. See examples in examples directory, gen_intake_local.py runs on UDA , gen_intake_s3.py runs on S3 bucket

