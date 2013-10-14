import dptests
import sys

def run_test(test_name):
    func = getattr(dptests, test_name, None)
    assert(func),("Test %s is not defined" % test_name)
    try:
        return func()
    except Exception, e:
        return "Error: %s" % e


# For now, assuming that 
if (len(sys.argv) > 1):
    run_test(sys.argv[1])
