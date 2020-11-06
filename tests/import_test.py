try:
  import intakebuilder
  print("Imported intakebuilder")
  try:
     from intakebuilder import getinfo, localcrawler, CSVwriter
  except ImportError:
     print("Unable to import",  "getinfo, localcrawler, CSVwriter")
except ImportError:
  print("Unable to import intakebuilder")
