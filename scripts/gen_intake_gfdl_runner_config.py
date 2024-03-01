#!/usr/bin/env python

from scripts import gen_intake_gfdl
import sys

sys.argv = ['--config', '/home/a1r/github/CatalogBuilder/configs/config.yaml']
print(sys.argv)
gen_intake_gfdl.main()

