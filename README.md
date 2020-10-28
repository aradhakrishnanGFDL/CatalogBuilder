# CatalogBuilder

The CatalogBuilder API will collect building blocks necessary to build a data catalog which can then be ingested in climate analysis scripts/workflow, leveraging the use of intake-esm and xarray.

Tested on posix file system and S3 at this time. 

Two ways To use intakebuilder

[A]
1.setup environment using environment_intake.yml
2. Clone https://github.com/aradhakrishnanGFDL/CatalogBuilder
3. From intakebuilder directory, you can import the package. 
4. Test: import intakebuilder
5. See examples in examples directory, gen_intake_local.py runs on UDA , gen_intake_s3.py  runs on S3 bucket

[B]

1.setup conda environment using environment_intake.yml
conda env create -f environment_intake.yml
2. conda activate intake
3. pip install git+https://github.com/aradhakrishnanGFDL/CatalogBuilder.git
4. Test: import intakebuilder 
5. See examples in examples directory, gen_intake_local.py runs on UDA , gen_intake_s3.py  runs on S3 bucket


