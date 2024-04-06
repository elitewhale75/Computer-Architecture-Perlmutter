"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

plt.title("Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.


flops1_time = [(prob_size/10**6)/time for prob_size, time in zip(problem_sizes, code1_time)]
flops2_time = [(prob_size/10**6)/time for prob_size, time in zip(problem_sizes, code2_time)]
flops3_time = [(prob_size/10**6)/time for prob_size, time in zip(problem_sizes, code3_time)]

plt.plot(flops1_time, "r-o")
plt.plot(flops2_time, "b-x")
plt.plot(flops3_time, "g-^")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS")

#varNames = [var_names[1], var_names[2], var_names[3]]
varNames = [ "direct sum", "vector sum","indirect sum"]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.savefig("MFLOPS")

plt.show()


#### MEMORY BANDWIDTH ####


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

plt.title("Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)
# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.

sys_band = 204.8 * (10 ** 9)

mem1_time = [(0 * prob_size * 8 / time)/sys_band for prob_size, time in zip(problem_sizes, code1_time)]
mem2_time = [(prob_size * 8 / time)/sys_band for prob_size, time in zip(problem_sizes, code2_time)]
mem3_time = [(2 * prob_size * 8 / time)/sys_band for prob_size, time in zip(problem_sizes, code3_time)]

plt.plot(mem1_time, "r-o")
plt.plot(mem2_time, "b-x")
plt.plot(mem3_time, "g-^")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Memory Bandwidth")

#varNames = [var_names[1], var_names[2], var_names[3]]
varNames = [ "direct sum", "vector sum","indirect sum"]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.savefig("MemoryBandwidth")

plt.show()

#### LATENCY  ####


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

plt.title("Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)
# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.

lat1_time = [ 1 * 0 for prob_size, time in zip(problem_sizes, code1_time)]
lat2_time = [ time / (8 * prob_size ) for prob_size, time in zip(problem_sizes, code2_time)]
lat3_time = [ time / (16 * prob_size )for prob_size, time in zip(problem_sizes, code3_time)]

plt.plot(lat1_time, "r-o")
plt.plot(lat2_time, "b-x")
plt.plot(lat3_time, "g-^")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Latency")

#varNames = [var_names[1], var_names[2], var_names[3]]
varNames = [ "direct sum", "vector sum","indirect sum"]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.savefig("Latency")

plt.show()
# EOF
