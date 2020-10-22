import os
from intakebuilder import getinfo, localcrawler, CSVwriter

def main():
    #######INPUT HERE OR USE FROM A CONFIG FILE LATER######
    project_dir = "/Users/ar46/data_cmip6/CMIP6/"  # DRS COMPLIANT PROJECT DIR
    csvfile = "/Users/ar46/PycharmProjects/CatalogBuilder/intakebuilder/test/intake_local.csv"
    #######################################################
    dictInfo = {}
    print(project_dir)
    project_dir = project_dir.rstrip("/")
    list_files = localcrawler.crawlLocal(project_dir, dictInfo)
    headers = CSVwriter.getHeader()
    if (not os.path.exists(csvfile)):
        os.makedirs(os.path.dirname(csvfile), exist_ok=True)
    CSVwriter.listdict_to_csv(list_files, headers, csvfile)
    print("CSV generated at:", os.path.abspath(csvfile))


if __name__ == '__main__':
    main()
