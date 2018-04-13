# -*- coding:utf-8 -*-
import json
import xml.etree.ElementTree as etree

class A(object):
	pass

# 自定义JSONConnector解析JSON文件
class JSONConnector(object):
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, mode='r', encoding='utf-8') as f:
			self.data = json.load(f)
	@property
	def parsed_data(self):
		return self.data

# 自定义XMLConnector解析JSON文件
class XMLConnector(object):
	def __init__(self, filepath):
		self.tree = etree.parse(filepath)

	@property
	def parsed_data(self):
		return self.tree

# 工厂方法，根据输入文件后缀返回解析特定文件类型的类实例
def connector_factory(filepath):
	if filepath.endswith('json'):
		connector = JSONConnector
	elif filepath.endswith('xml'):
		connector = XMLConnector
	else:
		raise ValueError('Cannot connect to {}'.format(filepath))
	return connector(filepath)

# 对工厂方法进行包装，增加了异常处理
def connect_to(filepath):
	factory = None
	try:
		factory = connector_factory(filepath)
	except ValueError as ve:
		print (ve)
	return factory

def main():
	sqlite_factory = connect_to('data/person.sq3')
	print()

	xml_factory = connect_to('data/person.xml')
	# xml_data = xml_factory.parsed_data()
	xml_data = xml_factory.parsed_data
	liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
	print ('Found: {} persons'.format(len(liars)))
	for liar in liars:
		print ('first name: {}'.format(liar.find('firstName').text))
		print ('last name: {}'.format(liar.find('lastName').text))
		[print ('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
	print ()

	json_factory = connect_to('data/donut.json')
	json_data = json_factory.parsed_data
	print ('Found: {} donuts'.format(len(json_data)))
	for donut in json_data:
		print ('Name: {}'.format(donut['name']))
		print ('Price: ${}'.format(donut['ppu']))
		[print ('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
	# a = A()
	# b = A()
	# print (id(a) == id(b))
	# print (a)
	# print (b)
	main()