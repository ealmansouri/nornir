#!/usr/bin/env nornir

from nornir import InitNornir
from nornir.core.inventory import Host
import json

nr = InitNornir(config_file="config.yaml")

#print(json.dumps(Host.schema(), indent=4))

host = (nr.inventory.hosts["SW04.bma"])
# prints out all of the keys belonging to the above defined host SW04
print(host.keys())
# this uses the filter function, filtering all hosts with the site "bma"
# and also with a role of "dist"
print(nr.filter(site="bma", role="dist").inventory.hosts.keys())
# Just prints 20 x dashes
print("-"*20)
# Another way of filtering uses two lines instead of the one above
cmh = nr.filter(site="cmh")
print(cmh.filter(role="access").inventory.hosts.keys())
print("-"*20)
# You can also display all the children of a particular group
print(nr.inventory.children_of_group("cmh"))
# Trying to display the "domain" value of SW05 with error handling, 
# which will print out an error if it is not able to.
SW05_cmh = nr.inventory.hosts["SW05.cmh"]
try:
    print(SW05_cmh["domain"])
except KeyError as e:
    print(f"couldn't find key: {e}")