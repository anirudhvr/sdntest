from dptests import *
import sys
import re
import config
from optparse import OptionParser

class SDNTest(object):
    "Parse options and run tests"

    def __init__(self):
        self.options = None
        self.args = None # additional arguments after option switches
        self.parse_args() 
        self.begin_tests()

    def parse_args(self):
        for args in sys.argv:
         desc = ("The %prog utility creates Mininet network from the\n"
                 "command line. It can create parametrized topologies,\n"
                 "invoke the Mininet CLI, and run tests.")

         usage = ('%prog [options]\n'
                 '(type %prog -h for details)')

         opts = OptionParser(description=desc, usage=usage)
         opts.add_option('--list-tests', '-l', action='callback', 
                 callback=self.list_tests)
         opts.add_option('--run_all', '-a', action='store_true',
                 default=False, help='run all tests')
         opts.add_option('--verbose', '-v', action='store_true',
                 default=False, help='verbose output')

         dptests_list =  config.all_dp_tests.keys(),
         for dptest in dptests_list:
             opts.add_option('--run-dptest-%s' %(dptest),
                     dest='dptest_%s' %(dptest),
                     default=False,
                     help=dptest, action='store_true')

         self.options, self.args = opts.parse_args()

    def list_tests(self):
        print 'Available Data Path tests:'
        print '\t', '\n\t'.join(config.all_dp_tests.keys()), '\n'

    def begin_tests(self):
        self.test_suites = []

        # Create datapath tests and configure
        dptests = DataPathTests()
        if self.options.run_all:
            for test_name in config.all_dp_tests.keys():
                dptests.enable_test(test_name)
        else:
            for opt in self.options:
                if re.match(r'dptest_(\w+)', opt) and opt == True:
                    dptests.enable_test(opt)
        for hyp in config.hypervisors:
            dptests.add_hypervisor(hyp)

        self.tests.append(dptests)

        #
        # Code here for control plane and func tests as well
        #

        for tests in self.test_suites:
            tests.setup()
            tests.run()


if __name__ == "__main__":
    SDNTest()
