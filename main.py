# -*- coding: utf-8 -*-

# The main procedure for CHASER.
# Once run, she will read her memory.
# Once stop, she will save her memory.
# She is not event triggered, but 
# 	internally driven.

import numpy as np

def connect_to_internet():
	print '[Chaser] connecting to internet...'
	print '[Chaser] connection failed!'
	

def main():
	print 'started.'
	print 'Loading memory...'

	# internal states
	e = 0 # [-1,1], emotion from bad to good.
	c = 0.5 # [0,1], controdictness.
	lang = 0 # default 0 is English, 1 is Chinese, 2 is Japanese.
	shut_down = 2 # shutdown code, 0-2
	
	print 'waking up...'

	while shut_down:
		if shut_down==1:
			if lang==0:
				print '[Chaser] Shut me down, really?[yes/no]'
			elif lang==1:
				print '[Chaser] 确定要关闭我吗？[是/不]'
			elif lang==2:
				print '[Chaser] 本当にあたしを締め切れる？'
			s = raw_input('[You] ')
			if s=='yes' or s=='是' or s=='はい':
				shut_down -= 1
			else:
				shut_down += 1
		elif shut_down>1:
			if np.random.rand(1)<c:
				print '[Chaser] May I ask you ...?'
			s = raw_input('[You] ')
			if s=='shut down' or s=='关机' or s=='終了':
				shut_down -= 1

	print 'sleeping...'
	
	print 'Saving memory...'
	print 'done.' 



# she is born here.
main()

