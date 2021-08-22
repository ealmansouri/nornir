from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.plugins.tasks.networking.netmiko_send_command import netmiko_send_command
from nornir.core.task import Task
from pprint import pprint

nr = InitNornir(
    config_file="config.yaml", dry_run=True
)

result = nr.run(netmiko_send_command, command_string="show version")

print_result(result)