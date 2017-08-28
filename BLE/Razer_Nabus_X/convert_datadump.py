#!/usr/bin/env python

def clean(instr):
	out = ""
	for c in instr:
		if ord(c) > 31 and ord(c) < 127:
			out += c
		else:
			out += "."
	return out
		

for rline in open('datadump.commands', 'r').readlines():
	hex_bytes = clean(rline[rline.index('value: ') + 6:].replace(' ', '').strip().decode('hex'))

	print rline.strip() + " | " + hex_bytes


