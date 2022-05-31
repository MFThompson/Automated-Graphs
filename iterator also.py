import matplotlib.pyplot as plt
import csv
from pandas import *
import numpy as np
import os
import pandas as pd
from os.path import exists
from pathlib import Path
import math

plt.rcParams.update({'font.size':12})
plt.rc('legend', fontsize=8.5)

directory = os.getcwd()
freqdata = []
AllFolders = []
x=0
Freq = []
Level = []
volts_meter = []

herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Avg.csv', skiprows = 1)
hero_safe_r_avg_freq = herosaferpdata['! Hz'].tolist()
hero_safe_r_avg_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO SAFE Restricted Peak.csv', skiprows = 1)
hero_safe_r_peak_freq = herosaferpdata['! Hz'].tolist()
hero_safe_r_peak_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Avg.csv', skiprows = 1)
hero_safe_u_avg_freq = herosaferpdata['! Hz'].tolist()
hero_safe_u_avg_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO SUSCEPTIBLE.csv', skiprows = 1)
hero_susceptible_freq = herosaferpdata['! Hz'].tolist()
hero_susceptible_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE Nuclear.csv', skiprows = 1)
hero_unsafe_nuclear_freq = herosaferpdata['! Hz'].tolist()
hero_unsafe_nuclear_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO UNSAFE.csv', skiprows = 1)
hero_unsafe_freq = herosaferpdata['! Hz'].tolist()
hero_unsafe_level = herosaferpdata['dBuV/m'].tolist()

herosaferpdata = pd.read_csv(directory + '\HERO SAFE Unrestricted Peak.csv', skiprows = 1)
hero_safe_unrestricted_peak_freq = herosaferpdata['! Hz'].tolist()
hero_safe_unrestricted_level = herosaferpdata['dBuV/m'].tolist()



for u in range(len(hero_safe_r_avg_freq)):
    hero_safe_r_avg_freq[u] = hero_safe_r_avg_freq[u] / 1000000

for u in range(len(hero_safe_r_peak_freq)):
    hero_safe_r_peak_freq[u] = hero_safe_r_peak_freq[u] / 1000000

for u in range(len(hero_safe_u_avg_freq)):
    hero_safe_u_avg_freq[u] = hero_safe_u_avg_freq[u] / 1000000

for u in range(len(hero_susceptible_freq)):
    hero_susceptible_freq[u] = hero_susceptible_freq[u] / 1000000

for u in range(len(hero_unsafe_nuclear_freq)):
    hero_unsafe_nuclear_freq[u] = hero_unsafe_nuclear_freq[u] / 1000000

for u in range(len(hero_unsafe_freq)):
    hero_unsafe_freq[u] = hero_unsafe_freq[u] / 1000000

for u in range(len(hero_safe_unrestricted_peak_freq)):
    hero_safe_unrestricted_peak_freq[u] = hero_safe_unrestricted_peak_freq[u] / 1000000




input("press a button")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isdir(f):
        AllFolders.append(f)
#        print(AllFolders[x])
        x = x + 1



for r in range(len(AllFolders)):
    directory_folder = AllFolders[r]
    csv_files = os.listdir(AllFolders[r])  #first iteration of loop. load list of CSV files in directory to csv_files
#    print(AllFolders[r])
    Freq.clear()
    Level.clear()
    volts_meter.clear()
    counter = 0
    for s in range(len(csv_files)):

        temp = csv_files[s]
        l = len(temp)
        temp = (temp[l-4:])
        if temp == ".CSV":
            counter = counter + 1
            print(directory_folder)
            print(csv_files[s])

            freqdata = read_csv(directory_folder + "/" + csv_files[s])
            tempfreq = freqdata['Freq (MHz)'].tolist()
            templevel = freqdata['Max Level Amplitude (dBuV/m)'].tolist()

            for j in range(len(tempfreq)):
                Freq.append(tempfreq[j])
                Level.append(templevel[j])
                volts_meter_temp = (10 ** ((templevel[j]-120)/20))
                volts_meter.append(volts_meter_temp)


            zipped_lists = zip(Freq, Level, volts_meter)
            sorted_pairs = sorted(zipped_lists)

            tuples = zip(*sorted_pairs)
            Freq, Level, volts_meter = [list(tuple) for tuple in tuples]

#            for v in range(len(volts_meter)):
#                print(volts_meter[v])
#                print(Level[v])


#            input("press a button")

#        for n in range(len(Freq)):
#            print(Freq[n])
#            print(Level[n])

    GraphName = AllFolders[r]
    GraphName = GraphName.replace(directory, "")
    GraphName = GraphName[1:]


    if counter >> 2:

        tick = list(range(30, 220))



        fig, ax1 = plt.subplots()
        ax1.set_xlabel('Frequency (MHz)')
        ax1.set_ylabel('Amplitude (dBuV/m)')

        ax1.plot(hero_safe_r_avg_freq, hero_safe_r_avg_level, color = 'tab:orange', linestyle = 'dashed')
        ax1.plot(hero_safe_r_peak_freq, hero_safe_r_peak_level, color = 'black', linestyle = 'dashed')
        ax1.plot(hero_safe_u_avg_freq, hero_safe_u_avg_level, color = 'tab:purple', linestyle = 'dashed')
        ax1.plot(hero_safe_unrestricted_peak_freq, hero_safe_unrestricted_level, color='tab:brown', linestyle='dashed')
        ax1.plot(hero_unsafe_nuclear_freq, hero_unsafe_nuclear_level,color = 'tab:red')
        ax1.plot(hero_unsafe_freq, hero_unsafe_level, color = 'tab:cyan')
        ax1.plot(hero_susceptible_freq, hero_susceptible_level, color='tab:green')

        ax1.legend(['HERO Safe Restricted Avg MILSTD-464C', 'HERO Safe Restricted Peak MILSTD-464C', 'HERO Safe Unrestricted Avg MILSTD_464C',  'HERO Safe Unrestricted Peak MILSTD464-C', 'HERO Unsafe Nuclear AFI91-208', 'HERO Unsafe AFI91-208','HERO Susceptible AFI91-208'], loc = 'lower right')
        ax1.set_xscale('log')
        ax1.plot(Freq, Level, color='tab:blue')
        ax1.set_yticks(np.arange(min(tick), max(tick), 10))

        ax2 = ax1.twinx()
        ax2.set_ylabel("Amplitude (V/m)")

        V_m = lambda level: (10**((level-120)/20))
        ymin, ymax = ax1.get_ylim()
        ax2.set_ylim((V_m(ymin), V_m(ymax)))
        ax2.plot()

        plt.title(GraphName)

        plt.grid()
        plt.show()





