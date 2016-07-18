import nbformat
import os
from os import getcwd, path
import logging
from nbconvert.preprocessors import ExecutePreprocessor
import functools
import codecs
import sys
import tempfile

def _write_notebook(nb, filepath):
    """
    write an executed notebook to file, handling failures gracefully

    Note:
    Writes to tempfile initially & copy to filename on success. 
    This mitigates risk of leaving notebook in unusable state (if, for example, there are problems writing to disk).
    """
    logger = logging.getLogger()
    pathdir, pathfile = path.split(filepath)
    tmp = tempfile.NamedTemporaryFile(dir = pathdir, delete = False)
    try:
        with codecs.open(tmp.name, mode='w', encoding='utf-8') as f:
            # write tempfile with utf-8 encoding
            nbformat.write(nb, f, version=nbformat.NO_CONVERT)
    except Exception as e:
        logger.error(u'Unexpected error writing notebook to temp file: %s %s' % (filepath, e))
        raise
    finally:
        tmp.close()
        os.rename(tmp.name, filepath)


def execute_notebook(notebook_filename,
                     executed_notebook=None,
                     timeout=6000,
                     kernel_name='python',
                     execute_path=None,
                     allow_errors=False
                     ):
    """
    Execute a jupyter notebook using nbconvert

    Parameters 
    ------------
    notebook_filename (str): path to notebook which should be executed
    executed_notebook (str): where to save executed notebook (defaults to in-place execution) 
    timeout (int): at what point should notebook execution be halted (default: 6000)
    kernel_name (str): which kernel to use (default: python2)
    execute_path (str): location in which execution should take place (default: ipynb location)
    allow_errors (bool): whether to continue executing the other cells in the notebook on error (default: False)
    """

    logger = logging.getLogger()
    if not(execute_path):
        execute_path = path.dirname(notebook_filename)
    if not(executed_notebook):
        executed_notebook = notebook_filename

    logger.debug('opening {0}'.format(notebook_filename))
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    logger.debug('starting execution of {} in {}'.format(notebook_filename, execute_path))
    try:
        ep = ExecutePreprocessor(timeout=timeout, kernel_name=kernel_name, allow_errors=allow_errors)
        ep.preprocess(nb, {'metadata': {'path': execute_path}})
    except:
        msg = 'Error executing the notebook "%s".\n' % notebook_filename
        msg += 'See notebook "%s" for the traceback.' % executed_notebook
        logger.error(msg)
        raise
    finally:
        logger.debug('writing results of exeuction to file {0}'.format(executed_notebook))
        _write_notebook(nb, executed_notebook)
