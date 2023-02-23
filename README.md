# R to HDF5

This code is a simple test using the Python pyreadr library to read matrices from RData files and convert to HDF5 (using h5py). The purpose is to reduce file size by reducing precision of the matrices (either by multiplying by a set value and converting to integer, or storing as a lower precision floating point number).

## Setting up environment

```bash
conda env create -f environment.yml
conda activate hdf5
```

## Creating matrix RData files

```bash
Rscript generate_matrices.r
```

## Generate HDF5 files (and convert back to RData for comparison)

```bash
python create_hdf5.py
```