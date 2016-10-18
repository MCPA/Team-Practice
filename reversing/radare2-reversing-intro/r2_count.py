import os
import r2pipe
import string

r2 = r2pipe.open("count")
char_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
good_string = list('ah_ah_ah_ah_902C7b10fE4a')
#good_string = list('ah')
instring = list('')
dc_count = 1
r2.cmd("doo")
bp_1 = '80485d3'
bp_2 = '80485da'
r2.cmd("db 0x" + bp_1)
r2.cmd("db 0x" + bp_2)
r2.cmd('dbc 0x'+bp_1+' "echo 80485d3"')
r2.cmd('dbc 0x'+bp_2+' "echo 80485da"')
r2.cmd('db')
for dc_count in range (25, 45):
	for test_char in char_list:
		#os.system('clear')
		null = r2.cmd("doo " + "".join(good_string) + "".join(instring)+test_char)
		output = r2.cmd(str(dc_count) +"dc")
		if bp_1 in output:
		   continue
		if bp_2 in output:
		   instring+=test_char
		   print("Instring: " + "".join(instring))
		   break
