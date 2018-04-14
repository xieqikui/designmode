#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Computer(object):
	def __init__(self, serial_num):
		self.serial_num = serial_num
		self.memory = None
		self.hdd = None
		self.gpu = None
	def __str__(self):
		info = {'memory: %sGB' %self.memory,
		'hdd: %sGB' %self.hdd,
		'gpu: %s' %self.gpu}
		return '\n'.join(info)

class ComputerBuilder(object):
	def __init__(self):
		self.computer = Computer('AG23385193')
	def configure_memory(self, amount):
		self.computer.memory = amount
	def configure_hdd(self, amount):
		self.computer.hdd = amount
	def congigure_gpu(self, gpu_model):
		self.computer.gpu = gpu_model

class HardwareEngineer:
	def __init__(self):
		self.builder = None
	def construct_computer(self, memory, hdd, gpu):
		self.builder = ComputerBuilder()
		self.builder.configure_memory(memory)
		self.builder.configure_hdd(hdd)
		self.builder.congigure_gpu(gpu)
	@property
	def computer(self):
		return self.builder.computer

def main():
	engineer = HardwareEngineer()
	engineer.construct_computer(memory=8, hdd=500, gpu='GeForce GTX 650 Ti')
	computer = engineer.computer
	print (computer)

if __name__ == '__main__':
	main()