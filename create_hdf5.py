#!/usr/bin/python
"""
Read data in datatframes from RData files and save to HDF5
"""
import pyreadr, h5py
import pandas as pd
import numpy as np


def read_rdata(filename, dfname):
    """Read in RData file and return a Pandas dataframe"""
    data = pyreadr.read_r(filename)
    df = data[dfname]
    return df


def write_hdf5(filename, df, dfname, dtype):
    """Write a pandas dataframe to HDF5 using the specified dtype"""
    outfile = h5py.File(filename, "w")
    outfile.create_dataset(dfname, data=df, dtype=dtype)
    outfile.close()


def read_hdf5(filename, dfname):
    """Read a single dataset from a HDF5 file and return as a Pandas dataframe"""
    infile = h5py.File(filename, "r")
    data = infile.get(dfname)
    result = pd.DataFrame(np.array(data))
    infile.close()
    return result


def write_rdata(filename, df, dfname):
    """Write a Pandas dataframe to RDatas"""
    pyreadr.write_rdata(filename, df, df_name=dfname)


"""
Read in R and save to HDF5
    Note - we use reduced precision on save
    Specify numpy dtype as last parameter to write_hdf5 (e.g. float16, i2) 
"""
floatmatrix = read_rdata("floatmatrix.RData", "floatmatrix")
intmatrix = read_rdata("intmatrix.RData", "intmatrix")
write_hdf5("float.hdf5", floatmatrix, "floatmatrix", "float16")
write_hdf5("int.hdf5", intmatrix, "intmatrix", "i2")


"""
Read in HDF5 and save to R
    Note - a float16 will be converted to float64, with artificially high precision!
"""
floatmatrix2 = read_hdf5("float.hdf5", "floatmatrix")
intmatrix2 = read_hdf5("int.hdf5", "intmatrix")
write_rdata("floatmatrix_reduced.RData", floatmatrix2, "floatmatrix")
write_rdata("intmatrix_reduced.RData", intmatrix2, "intmatrix")