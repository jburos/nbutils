nbutils
===============================

author: Jacki Buros Novik

Overview
--------

Utilities for working with Jupyter notebooks (ipynbs)

Specifically:
   **nbexecute**: execute all cells in a notebook, replacing original with output

Installation / Usage
--------------------

To install use pip:

    $ pip install git+git://github.com/jburos/nbutils


Or clone the repo:

    $ git clone https://github.com/jburos/nbutils.git
    $ python setup.py install

Usage: 

    $ nbexecute path-to-ipynb1.ipynb [ipynb2.ipynb] ... 

```
$ nbexecute -h
usage: nbexecute [-h] [--timeout TIMEOUT] [--debug] [--allow-errors]
                 files [files ...]

Execute jupyter notebooks using nbconvert

positional arguments:
  files              files (ipynbs) to process

optional arguments:
  -h, --help         show this help message and exit
  --timeout TIMEOUT  timeout for each notebook execution
  --debug            Increase logging output
  --allow-errors     Continue executing notebook on error
  ```

    
Contributing
------------

TBD

Example
-------

TBD
