from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli, napalm_configure
from nornir.plugins.tasks.networking.netmiko_send_command import netmiko_send_command
from nornir.core.task import Task
from pprint import pprint
from netmiko import ConnectHandler

nr = InitNornir(
    config_file="mpbn-config.yaml", dry_run=True
)

BENSR01 = nr.inventory.hosts["BENSR01"]
BENSR02 = nr.inventory.hosts["BENSR02"]
FWTSR01 = nr.inventory.hosts["FWTSR01"]
FWTSR02 = nr.inventory.hosts["FWTSR02"]


BENSR01Contexts = ["OM_RC","H_OSS","SS7","H_SIG","CN","SN","CH","H_PS_Access","H_PS_CN","H_Billing","RAN","H_LTE","DCN","speedtest"]
BENSR02Contexts = ["OM_RC","H_OSS","CN","SS7","H_SIG","H_CS_Access","SN","CH","H_PS_Access","H_PS_CN","H_Billing","RAN","H_ABIS","H_IUB","H_LTE","DCN"]
FWTSR01Contexts = ["OM_RC","SS7","SIGN_LDAP","CN","RAN","CH","INTERNET","IAC","speedtest","IGW"]
FWTSR02Contexts = ["OM_RC","SS7","SIGN_LDAP","CN","RAN","CH","DCN","IAC","INTERNET","IGW"]

termLen = "term len 0"
showIpRoute = "show ip route 10.214.3.255"
contextsAll = "show context all"

def multipleTasks(task: Task):
    task.run(netmiko_send_command, command_string=showIpRoute)

results = nr.run(task=multipleTasks)

print_result(results)

# net_connect = ConnectHandler(**FWTSR01)
# pprint("-"*22)
# pprint(FWTSR01["session_log"])
# termLenCmd = net_connect.send_command(termLen)
# showIpRouteCmd = net_connect.send_command(showIpRoute)
# for context in FWTSR01Contexts:
#     enterContext = net_connect.send_command("context %s"%context)
#     contextRoutes = net_connect.send_command(showIpRoute)
#     pprint(contextRoutes)
# 	#for line in contextsAll.splitlines():
# 	#	currentContext = line.split()[0]
#     #    configContext = net_connect.send_command("context ", currentContext)
#     #    showIpRouteCmd = net_connect.send_command(showIpRoute)
#     #    print(showIpRouteCmd)
#     print(net_connect.find_prompt())
#     net_connect.disconnect()


