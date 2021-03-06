#!/usr/bin/env python

import argparse
import os
from os import getcwd, path
from . import notebooks
import logging

def parse_args():
    parser = argparse.ArgumentParser(usage=__doc__,
                 description='Execute jupyter notebooks using nbconvert',
                 fromfile_prefix_chars='@' ## allow @files=filename.txt param
                 )
    parser.add_argument('files', help='files (ipynbs) to process', nargs='+')
    parser.add_argument('--timeout', help='timeout for each notebook execution', 
                       type=int, default=6000)
 #   parser.add_argument('--output-dir', help='output dir for executed notebooks (default: overwrite existing)',
 #                       default=getcwd())

    parser.add_argument('--kernel-name', help='Specify kernel name',
                        default=None)
    parser.add_argument('--debug', help='Increase logging output',
                        default=False, action='store_true')
    parser.add_argument('--allow-errors', help='Continue executing notebook on error',
                        default=False, action='store_true')
    opts = parser.parse_args()
    return opts

def main():
    opts = parse_args()

    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    ## todo process output-dir param
    for f in opts.files:
        notebooks.execute_notebook(f, timeout=opts.timeout, allow_errors=opts.allow_errors, kernel_name=opts.kernel_name)



if __name__ == '__main__':
    main()
