#! /usr/bin/python

#
# Copyright (c) 2016 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.
#

import xml.etree.ElementTree as ET
import sys
import os, glob, re
import argparse

parser = argparse.ArgumentParser(
    description="This script generates a ruleset file that contains mapping of HTTP URLs \
     to corresponding HTTPS URLs. The input is a directory containing XML files with ruleset \
     definitions. The output file is generated using Protocol Buffer compiler.")

parser.add_argument('rules_dir', metavar='<XML Directory>', nargs=1,
    help='The input directory that contains ruleset definition XML files')

parser.add_argument('output_file', metavar='<Data File>', nargs=1,
    help='The output file that the script will generate')
parser.add_argument('-v', '--verbose', type=int, default=[0],
    nargs=1, help='Level of verbosity (default 0)')
parser.add_argument('-i', '--include', default=['.'],
    nargs=1, help='Location of secure_connect_ruleset_pb2 package (default = current folder)')

args = parser.parse_args()

rules_dir = args.rules_dir[0];
output_file = args.output_file[0];
verbosity = args.verbose[0]
include_dir = args.include[0]

sys.path.append(include_dir)

import secure_connect_ruleset_pb2

files = glob.glob(rules_dir + '/*.xml')
ruleset_list = secure_connect_ruleset_pb2.RuleSetList()

for file in files:
    if verbosity > 0:
        print "Parsing " + file
    tree = ET.parse(file)
    root = tree.getroot()

    if root.tag == 'ruleset':
        if verbosity > 1:
            print root.tag, root.attrib
        ruleset = ruleset_list.ruleset.add()
        ruleset.name = root.attrib['name']
        if 'default_off' in root.attrib.keys():
            ruleset.default_off = root.attrib['default_off']

        for child in root:
            if verbosity > 2:
                print child.tag, child.attrib
            if child.tag == 'target':
                target = ruleset.targets.add()
                target.host = child.attrib['host']

            if child.tag == 'rule':
                rule = ruleset.rules.add()
                rule.regex = child.attrib['from']
                rule.to = child.attrib['to']

            if child.tag == 'exclusion':
                exclusion = ruleset.exclusions.add()
                exclusion.pattern = child.attrib['pattern']

            if child.tag == 'securecookie':
                securecookie = ruleset.securecookies.add()
                securecookie.host = child.attrib['host']
                securecookie.name = child.attrib['name']

output = open(output_file, "wb")
output.write(ruleset_list.SerializeToString())
output.close()
