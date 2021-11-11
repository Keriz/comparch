import matplotlib.pyplot as plt
import numpy as np
import glob

mapping_pname = {'FCFS': 0, 'FRFCFS': 1,
                 'FRFCFS_Cap': 2, 'ATLAS': 3, 'BLISS': 4}
mapping_workload = {'HLLL': 0, 'HHLL': 1,
                    'HHHH': 2, 'HHHHHHHH': 3}

policy = t = [[0]*4 for i in range(5)]


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


for input in glob.glob("*.stats"):
    fields = input.split('.')[0].split('_')
    with open(input) as fp:
        for row in fp:
            if "instruction_throughput" in row:
                it = [float(s) for s in row.split() if is_float(s)]
                if "Cap" in fields[1]:
                    policy[mapping_pname["FRFCFS_Cap"]
                           ][mapping_workload[fields[2]]] = it[0]
                else:
                    policy[mapping_pname[fields[0]]
                           ][mapping_workload[fields[1]]] = it[0]


print(policy)

labels = ['HLLL', 'HHLL', 'HHHH', 'HHHHHHHH']

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, policy[0], width*0.3, label='FCFS')
rects2 = ax.bar(x - width/2, policy[1], width*0.3, label='FRFCFS')
rects3 = ax.bar(x, policy[2], width*0.3, label='FRFCFS_Cap')
rects4 = ax.bar(x + width/2, policy[3], width*0.3, label='ATLAS')
rects5 = ax.bar(x + width, policy[4], width*0.3, label='BLISS')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Instruction throughput')
ax.set_xlabel('Workload')
ax.set_title('Metrics of instruction throughput for different policies')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.savefig("blocksize.png")
