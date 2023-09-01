#!/usr/bin/env python

""" Tests to load the catalog and extend the test capabilities """

__author__ = "A.Radhakrishnan"
__maintainer__ = "GFDL MSD workflow team"

import intake
import intake_esm
import pandas as pd 

def load_cat(catspec=None):
  """Checks if the json and associated csv can be opened by intake_esm""" 
  cat = None
  try:
    cat = intake.open_esm_datastore(catspec)
  except BaseException as e:
    print("Can't load this catalog",str(e))
  return cat
def test_loadcat():
  catspec = "/nbhome/a1r/ciheim/out/gfdl_spec.json"
  cat = load_cat(catspec)
  assert isinstance(cat.df, pd.DataFrame)

