import string
from typing import Dict, Any


class CatalogBuilder:
    """ This is the CatalogBuilder class that has attributes and functions that point to metadata records for a a file that can be
    populated in a DB (csv)
    """

    def __init__(self, path, comment=None):
        self.drs = path
        self.comment = comment

    def list_files(self):
        list_files = []
        # list files in the given directory.
        # HINT: try glob.glob or os.walk
        return list_files

    def extract(self):
        """
         Input: extract takes as input the input dataset directory structure and identifies the values we need to map\n"
         to the keys like model, institute_name,etc\n"
         Output: extract returns a dictionary with key-value pairs for each field that is essential for defining its entry in a data catalog\n"
         case 1: Unified Datagi Archive UDA /data_cmip6/CMIP6/AerChemMIP/NOAA-GFDL/GFDL-ESM4/histSST/r1i1p1f1/Amon/rlut/gr1/v20180701\n"
         :rtype: object
        """
        # SPLIT the string by the delimiter / and extract each of the values.
        dict_header_value: Dict[string, string] = {}
        # Create a dictionary dictMetadata whose keys are our column names that idenfity the dataset
        # The values are extracted from the string based on their positions
        return dict_header_value


# Driver code
if __name__ == '__main__':
    drsPath = "/Users/ar46/data_cmip6/CMIP6/AerChemMIP/NOAA-GFDL/GFDL-ESM4/histSST/r1i1p1f1/Amon/rlut/gr1/v20180701/"
    catalog_block = CatalogBuilder(drsPath, comment="UDA")
    list_files = catalog_block.list_files()
    # loop through the list list_files and apply extract function to get each the dictionary key/value
    dict_col_value = catalog_block.extract()
    print(dict_col_value)
