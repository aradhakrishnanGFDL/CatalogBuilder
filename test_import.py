def test_import():
 try:
  import intakebuilder
  print("Imported intakebuilder")
 except ImportError:
  raise ImportError('Error importing intakebuilder')
  return -97
 try:
     from intakebuilder import getinfo, localcrawler, CSVwriter
     print("Imported getinfo, localcrawler, CSVwriter")
 except ImportError:
     raise ImportError("Unable to import",  "getinfo, localcrawler, CSVwriter")
     return -98
 return True
