from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(config_file="config.yaml")

ios_devices = nr.filter(platform="ios").inventory.hosts.keys())

results = nr.run(
    task=napalm_cli, ios_devices, commands=["show interface summary"]
)

print_result(results)