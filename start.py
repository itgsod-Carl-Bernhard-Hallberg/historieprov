 # -*- coding: utf-8 -*-
#from pprint import pprint
import yaml


with open("bernadotte.yaml") as f:
    family=yaml.load(f)

for x in family['bernadotte']['barn'][0]:
    print x