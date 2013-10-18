import sys

class TestBase(object):
    def __init__(self):
        self.options = {
                'tests': [],
                'hypervisors': [],
                'openstack_config': {},
                'verbose': False
                }

    def enable_test(test_name):
        self.options['tests'].append(test_name)

    def add_hypervisor(hyp):
        self.options['hypervisors'].append(hyp)

    def add_option(key, value):
        self.options[key] = value

    def setup(self):
        # to be filled in by 
        pass

    def run(self):
        for test in self.options.tests:
            try:
                test()
            except AttributeError:
                sys.stderr.write("Test %s does not exist; skipping.." %(test))

