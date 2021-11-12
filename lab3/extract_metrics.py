import matplotlib.pyplot as plt
import numpy as np
import glob

mapping_pname = {'FCFS': 0, 'FRFCFS': 1,
                 'FRFCFS_Cap': 2, 'ATLAS': 3, 'BLISS': 4}
mapping_workload = {'HLLL': 0, 'HHLL': 1,
                    'HHHH': 2, 'HHHHHHHH': 3}

it_measurements = [[0]*4 for i in range(5)]
ms_measurements = [[0]*4 for i in range(5)]


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


for input in glob.glob("*.stats"):
    if input == "low.stats" or input == "high.stats":
        continue
    fields = input.split('.')[0].split('_')
    with open(input) as fp:
        for row in fp:
            if "instruction_throughput" in row:
                it = [float(s) for s in row.split() if is_float(s)]
                if "Cap" in fields[1]:
                    it_measurements[mapping_pname["FRFCFS_Cap"]
                                    ][mapping_workload[fields[2]]] = it[0]
                else:
                    it_measurements[mapping_pname[fields[0]]
                                    ][mapping_workload[fields[1]]] = it[0]


alone_H = [32102297, 31695820, 31695820, 32091700, 32091700]
alone_L = [6948948, 6946081, 6946081, 6948948, 6948948]


for input in glob.glob("*.stats"):
    if input == "low.stats" or input == "high.stats":
        continue
    fields = input.split('.')[0].split('_')
    workloads = ""
    max_slowdown = 0
    slowdown = 0
    plcy = fields[0]

    if "Cap" in fields[1]:
        workloads = fields[2]
        plcy += "_" + fields[1]
    else:
        workloads = fields[1]

    with open(input) as fp:
        for row in fp:
            if "record_cycs_core_" in row:
                core = int(row.split()[0].split('_')[3])
                cycles = int(row.split()[1])
                if workloads[core] == 'H':
                    max_slowdown = max(
                        cycles / alone_H[mapping_pname[plcy]], max_slowdown)
                else:
                    max_slowdown = max(
                        cycles / alone_L[mapping_pname[plcy]], max_slowdown)
    ms_measurements[mapping_pname[plcy]
                    ][mapping_workload[workloads]] = max_slowdown


labels = ['HLLL', 'HHLL', 'HHHH', 'HHHHHHHH']

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

""" fig, ax = plt.subplots()
rects1 = ax.bar(x - width, it_measurements[0], width*0.3, label='FCFS')
rects2 = ax.bar(x - width/2, it_measurements[1], width*0.3, label='FRFCFS')
rects3 = ax.bar(x, it_measurements[2], width*0.3, label='FRFCFS_Cap')
rects4 = ax.bar(x + width/2, it_measurements[3], width*0.3, label='ATLAS')
rects5 = ax.bar(x + width, it_measurements[4], width*0.3, label='BLISS')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Instruction throughput')
ax.set_xlabel('Workload')
ax.set_title('Metrics of instruction throughput for different policies')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.savefig("instruction_throughput.png") """


fig, ax = plt.subplots()
rects1 = ax.bar(x - width, ms_measurements[0], width*0.3, label='FCFS')
rects2 = ax.bar(x - width/2, ms_measurements[1], width*0.3, label='FRFCFS')
rects3 = ax.bar(x, ms_measurements[2], width*0.3, label='FRFCFS_Cap')
rects4 = ax.bar(x + width/2, ms_measurements[3], width*0.3, label='ATLAS')
rects5 = ax.bar(x + width, ms_measurements[4], width*0.3, label='BLISS')
ax.set_ylabel('Maximum slowdown')
ax.set_xlabel('Workload')
ax.set_title('Maximum slowdown of applications for different policies')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.savefig("maximum_slowdown.png")
