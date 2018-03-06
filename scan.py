import os, sys, json, time

macs = []
dt = "" + time.strftime("%Y-%m-%d") + ".txt"
the_pi = []


#os.system("nmap -v 192.168.1.*")
os.system("arp -a > " + str(dt) + ".txt")

with open(dt) as a:
	print a
	for b in a:
		macs.append(b)

devices = []

for c in macs:
	device = []
	device.append("mac")
	device.append("ip")
	device["mac"] = "yes"
	device["ip"] = "no"
	devices.append(device)

	# print devices["device"]

	

	# print d
	print devices



