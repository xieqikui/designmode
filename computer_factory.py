#! /usr/bin/env python3
MINI14 = '1.4GHZ Mac mini'

# 这里嵌套了MacMini14类。这是禁止直接实例化一个类的简洁方式
class AppleFactory(object):
	class MacMini14():
		def __init__(self):
			self.memory = 4
			self.hdd = 500
			self.gpu = 'Intel HD Graphics 5000'
		def __str__(self):
			info = {'mini14: %s' %MINI14, 
			'memory: %dGB' %self.memory,
			'hdd: %dGB' %self.hdd,
			'gpu: %s' %self.gpu}
			return '\n'.join(info)
	def bulid_computer(self, model):
		if model == 'MINI14':
			return self.MacMini14()
		else:
			print ('I don\'t know how to make %s' %model)

if __name__ == '__main__':
	af = AppleFactory()
	mac_mini = af.bulid_computer('MINI14')
	print (mac_mini)