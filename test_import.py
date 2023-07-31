def check_import():
 try:
  import intakebuilder
  from intakebuilder import getinfo, localcrawler, CSVwriter
  print("Imported intakebuilder and getinfo, localcrawler, CSVwriter ")
 except ImportError:
  raise ImportError('Error importing intakebuilder and other packages')
  return -97
 return True
def test_import():
    assert check_import() == True
