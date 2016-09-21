#! /usr/bin/python

#
# Copyright (c) 2016 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.
#

import sys
import os, glob, re
import argparse

parser = argparse.ArgumentParser(
    description="This script parses the ruleset file that contains mapping of HTTP URLs to corresponding \
     HTTPS URLs. The input is a file that was generated using Protocol Buffer compiler.")

parser.add_argument('input_file', metavar='<Data File>', nargs=1,
    help='The input protobuf file that contains rulesets')
parser.add_argument('-v', '--verbose', type=int, default=[0],
    nargs=1, help='Level of verbosity (default 0)')
parser.add_argument('-i', '--include', default=['.'],
    nargs=1, help='Location of secure_connect_ruleset_pb2 package (default = current folder)')

args = parser.parse_args()

input_file = args.input_file[0];
verbosity = args.verbose[0]
include_dir = args.include[0]

sys.path.append(include_dir)

import secure_connect_ruleset_pb2

ruleset_list = secure_connect_ruleset_pb2.RuleSetList()
try:
    f = open(input_file, "rb")
    ruleset_list.ParseFromString(f.read())
    f.close()
except IOError:
    print input_file + ": Could not open file.."
    exit()

ruleset_count = 0
ruleset_off = 0
target_count = 0;
rule_count = 0;
exclusion_count = 0;
securecookie_count = 0;

for ruleset in ruleset_list.ruleset:
    if verbosity > 0:
        print "Ruleset: ", ruleset.name.encode('ascii', 'ignore')
    ruleset_count += 1
    if ruleset.HasField('default_off'):
        ruleset_off += 1
        if verbosity > 1:
            print "Off: ", ruleset.default_off

    for exclusion in ruleset.exclusions:
        exclusion_count += 1

    for securecookie in ruleset.securecookies:
        securecookie_count += 1

    for target in ruleset.targets:
        target_count += 1
        if verbosity > 1:
            print "Target: ", target.host.encode('ascii', 'ignore')

    for rule in ruleset.rules:
        rule_count += 1
        if verbosity > 2:
            print "Rule: regex ", rule.regex.encode('ascii', 'ignore')
            print "Rule: to ", rule.to.encode('ascii', 'ignore')

print "----------------------------------------------------"
print "Count: ", ruleset_count
print "Off: ", ruleset_off
print "Targets: ", target_count
print "Rules: ", rule_count
print "Exclusions: ", exclusion_count
print "SecureCookies: ", securecookie_count
print "----------------------------------------------------"
