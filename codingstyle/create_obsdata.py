#!/usr/bin/env python
import numpy as np
import h5py


def create_obsdata(numstations=10, time=240, freqrange=40):
    """
    Create an HDF5 file simulating observation data

    :param numstations: number of stations
    :param time: observation time in seconds
    :param freqrange: frequency range of observation
    :return: NONE
    """
    obs_data = np.random.rand(numstations, time, freqrange)
    fname = "obs_20180225.h5"
    with h5py.File(fname, 'w') as h5f:
        h5f.create_dataset('obs_data', data=obs_data)
        h5f['obs_data'].dims[0].label = "Station"
        h5f['obs_data'].dims[1].label = "Time_in_Seconds"
        h5f['obs_data'].dims[2].label = "Frequency_in_MHz"


if __name__ == "__main__":
    create_obsdata()
