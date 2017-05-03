"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg # if this is imported I dont need to write read functions anymore...
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct', 
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    return df

 
def CrossValidPregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    val = True

    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        if (len(indices) != pregnum):
    	    print('Caseid: {}, Preg: {}, Resp.pregnum: {}'.format(caseid, len(indices), pregnum))
    	    val = False
    return val
	


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()
    print('Pregnancy number counts:\n')
    print(resp.pregnum.value_counts().sort_index())

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(CrossValidPregnum(resp))
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
