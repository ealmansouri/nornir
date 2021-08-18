#!/usr/bin/env nornir

from nornir import InitNornir
from nornir.core.inventory import Host
import json

nr = InitNornir(config_file="config.yaml")

#print(json.dumps(Host.schema(), indent=4))

host = (nr.inventory.hosts["SW04.bma"])
print(host.keys())
print(nr.filter(site="bma", role="dist").inventory.hosts.keys())
print("-"*20)
cmh = nr.filter(site="cmh")
print(cmh.filter(role="access").inventory.hosts.keys())
print("-"*20)
print(nr.inventory.children_of_group("cmh"))

SW05_cmh = nr.inventory.hosts["SW05.cmh"]
try:
    print(SW05_cmh["domain"])
except KeyError as e:
    print(f"couldn't find key: {e}")