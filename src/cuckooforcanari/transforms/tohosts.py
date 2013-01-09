#!/usr/bin/env python

from canari.framework import configure
from canari.maltego.entities import IPv4Address
from common.entities import CuckooTaskID, CuckooMalwareFilename
from common.cuckooapi import report
from common.cuckooparse import network

__author__ = 'bostonlink'
__copyright__ = 'Copyright 2013, Cuckooforcanari Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'bostonlink'
__email__ = 'bostonlink@pentest-labs.org'
__status__ = 'Development'

__all__ = [
	'dotransform',
	'onterminate'
]

@configure(
	label='To Hosts [Cuckoo Sandbox]',
	description='Returns host IP addresses associated with the Cuckoo analysis task id.',
	uuids=[ 'cuckooforcanari.v2.IDToHosts_Cuckoo', 'cuckooforcanari.v2.FileToHosts_Cuckoo' ],
	inputs=[ ( 'Cuckoo Sandbox', CuckooTaskID ), ( 'Cuckoo Sandbox', CuckooMalwareFilename ) ],
	debug=True
)

def dotransform(request, response):

	if 'taskid' in request.fields:
		task = request.fields['taskid']
	else:
		task = request.value

	# TODO Figure out the link, notes, and bookmark entity props
	netw = network(report(task))
	for d in netw['hosts']:
			response += IPv4Address(
				d.decode('ascii'),
				taskid = task
			)

	return response