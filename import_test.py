try:
  import intakebuilder
  print("Imported intakebuilder")
  try:
     from intakebuilder import getinfo, localcrawler, CSVwriter
     print("Imported getinfo, localcrawler, CSVwriter")
  except ImportError:
     print("Unable to import",  "getinfo, localcrawler, CSVwriter")
     return -98
except ImportError:
  print("Unable to import intakebuilder")
  return -97
