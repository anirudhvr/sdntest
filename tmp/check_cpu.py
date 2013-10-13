import re
import sys
import time

class cpu_stats:
    def __init__(self, u, n, s, i):
        self.user = u
        self.nice = n
        self.system = s
        self.idle = i

def extract_cpu_stats():
    f = open('/proc/stat', 'r')
    str = f.readline().strip()
    s = re.findall("cpu\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", str)
    f.close()

    return cpu_stats(int(s[0][0]), int(s[0][1]), int(s[0][2]), int(s[0][3]))

def extract_cpu_load(interval):
    #cpu0 278455 33 59090 2023985 4781 384 253 0
    #cpu1 616108 4 531523 1217828 848 0 597 0

    stat1 = extract_cpu_stats()
    time.sleep(interval);
    stat2 = extract_cpu_stats()

    active_jiffies = stat2.user + stat2.nice + stat2.system - stat1.user - stat2.nice - stat2.system
    idle_jiffies = stat2.idle - stat1.idle;

    if (active_jiffies + idle_jiffies != 0):
        util = 1 - idle_jiffies * 1.0 / (active_jiffies + idle_jiffies)
    else:
        util = 0

    return util


interval = float(sys.argv[1])
print extract_cpu_load(interval)
