from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.core.task import Task

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)
print(nr)

sw04=nr.inventory.hosts["sw04"]
sw04Ip=sw04["username"]
print(sw04.keys())
print(sw04Ip)

vSRX = nr.inventory.hosts("vSRX")

ios_devices = nr.filter(platform="ios").inventory.hosts
print(ios_devices)

def multiple_tasks(task: Task):
    task.run(
        task=napalm_cli, commands=["show ip interfaces brief"]
    )

    task.run(
        task=napalm_configure, dry_run=False, configuration="interface loopback 1000"
    )

    task.run(
        task=napalm_get, getters=["interfaces"]
    )

results = nr.run(
    task=multiple_tasks
)

print_result(results)