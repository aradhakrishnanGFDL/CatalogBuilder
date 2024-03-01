#!/usr/bin/env python

import gen_intake_gfdl
import sys

sys.argv = ['INPUT_PATH',None,'--config', '/home/a1r/github/CatalogBuilder/configs/config.yaml']
print(sys.argv)
gen_intake_gfdl.main()

