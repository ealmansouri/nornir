from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file="config.yaml")

# Used these to check the attributes for the hosts
#sw04 = nr.inventory.hosts["sw04"]
#print(sw04["password"])
#print(sw04.keys())
#vsrx = nr.inventory.hosts["vSRX"]
#print(vsrx["password"])
#print(vsrx.keys())
#print(nr.filter(platform="junos").inventory.hosts.keys())

results = nr.run(
    task=napalm_get, getters=["facts", "interfaces"]
)

print_result(results)