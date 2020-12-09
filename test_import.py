def test_import():
 try:
  import intakebuilder
  print("Imported intakebuilder")
  try:
     from intakebuilder import getinfo, localcrawler, CSVwriter
     print("Imported getinfo, localcrawler, CSVwriter")
  except ImportError:
     raise ImportError("Unable to import",  "getinfo, localcrawler, CSVwriter")
     return -98
 except ImportError:
  raise ImportError('Error importing intakebuilder')
  return -97
 return 0
