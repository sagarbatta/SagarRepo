#!/usr/bin/env python
#
# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Copyright (c) 2016 Qualcomm Technologies, Inc.
# All Rights Reserved.
# Confidential and Proprietary - Qualcomm Technologies, Inc.
#

import fnmatch
import optparse
import os
import sys

REPOSITORY_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

sys.path.append(os.path.join(REPOSITORY_ROOT, 'build/android/gyp/util'))
import build_utils

def ExtractZip(options):

  zip_path = options.zip
  extract_path = options.exdir
  build_utils.DeleteDirectory(extract_path)
  build_utils.MakeDirectory(extract_path)
  unzip_cmd = ['unzip', '-qq', zip_path, '-d', extract_path]
  build_utils.CheckOutput(unzip_cmd)

def main():
  parser = optparse.OptionParser()
  build_utils.AddDepfileOption(parser)
  parser.add_option('--zip', help='Zip file path.')
  parser.add_option('--exdir', help='Extract files into exdir')
  parser.add_option('--stamp', help='Path to touch on success.')

  options, _ = parser.parse_args()

  ExtractZip(options)

  if options.depfile:
    build_utils.WriteDepfile(options.depfile, build_utils.GetPythonDependencies())

  if options.stamp:
    build_utils.Touch(options.stamp)


if __name__ == '__main__':
  sys.exit(main())
