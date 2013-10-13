####################################
# SDNTest configuration scripts
####################################

##################
# General config 
##################

# openstack controller
os_controller = {
        'root@cleopatra.t-labs.us':'Tlabs5050'
}

# openstack credentials
os_username='admin'
os_password='contrail123'
os_tenant_name='admin'
os_auth_url='http://192.168.1.241:5000/v2.0/'

# the list of credentials to bareemetal machines used for the test with 
hypervisors = {
        'root@rome2.t-labs.us':'Tlabs5050'
        'root@rome3.t-labs.us':'Tlabs5050'
}

#######################################################
# Data path tests - enable or disable tests here
#######################################################

# Currently, these tests are between a pair 
# of VMs on otherwise unloaded hypervisors
dp_tests = {
        'one_packet_ping_same_hypervisor': {'times': 20}, 
        'one_packet_ping_diff_hypervisor': {'times': 20},
        'ping_same_hypervisor': {'duration': 30 }, 
        'ping_diff_hypervisor': {'duration': 30 },  
        'iperf_same_hypervisor': {'duration': 30, 'interfaces': {'eth2'}, 'formats': {'tcp', 'udp' }}, 
        'iperf_diff_hypervisor': {'duration': 30, 'interfaces': {'eth2'}, 'formats': {'tcp', 'udp' }},  
        'arping_same_hypervisor': {'duration': 60, 'interfaces': {'eth2'}}, 
        'arping_diff_hypervisor': {'duration': 60 , 'interfaces': {'eth2'}},
        'hping3_same_hypervisor': {'duration': 60, 'interfaces': {'eth2'} , 'uinterval': {1, 10, 50, 100, 500, 1000}, 'args': '-2 -p ++1024'},
        'hping3_diff_hypervisor': {'duration': 60, 'interfaces': {'eth2'} , 'uinterval': {1, 10, 50, 100, 500, 1000}, 'args': '-2 -p ++1024'}
        }


