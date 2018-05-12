#!/usr/bin/python

import xml.etree.ElementTree as ET
import json
		
def parseXML(xmlfile):

	
	# create element tree object
	tree = ET.parse(xmlfile)

	# get root element
	root = tree.getroot()

	# create empty list for response items
	responseitems = []

	# iterate news items
	for item in root.findall('./response'):

		# empty response dictionary
		response = {}

		# response id from xml
		responseid = item.get('id')
		response.__setitem__('id',responseid)

		# iterate child elements of item
		for child in item:
			if len(list(child)) > 0:
				response.__setitem__('type',child.tag)
				elemresult = {}
				elemresult.__setitem__(child[0].tag,child[0].text)
				elemresult.__setitem__(child[1].tag,child[1].text)
				response.__setitem__(child.tag,elemresult)

		# append news dictionary to news items list
		responseitems.append(response)

	parsed =  json.dumps(responseitems)
	print parsed

	# return news items list
	return parsed
	
def main():
	
	# parse xml file
	responseitems = parseXML('/Users/ramesh.dhavala/projects/elk_ws_xml_poc/test.xml')

		
if __name__ == "__main__":

	# calling main function
	main()
