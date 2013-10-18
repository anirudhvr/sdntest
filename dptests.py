import pprint
from test_base import *

class DataPathTests(TestBase):
    def __init__(self, enabled_tests={}, hypervisor_list={}):
        super(DataPathTests, self).__init__()
        self.initialize_hosts()
        self.install_software()
        self.begin_tests()

    def initialize_hosts(self):
        pass

    def install_software(self):
        pass

    def begin_tests(self):
        pass

    def setup(self):
        print "DataPathTests setup"

    def run(self):
        print "DP options: ", 
        pprint.pprint(self.options)
        print "DataPathTests run"

    def one_packet_ping_same_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def one_packet_ping_diff_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def ping_same_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def ping_diff_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def iperf_same_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def iperf_diff_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def arping_same_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def arping_diff_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def hping3_same_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

    def hping3_diff_hypervisor():
        print "Running test", inspect.stack()[0][3]
        pass

