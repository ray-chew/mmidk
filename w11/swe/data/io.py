import argparse
import os
import h5py
import numpy as np

class writer(object):
    def __init__(self, folder='./output/', filename='swe.h5'):
        self.OUTPUT_FOLDER = folder
        self.OUTPUT_FILENAME = filename
        self.FILE_PATH = self.OUTPUT_FOLDER + '/' + self.OUTPUT_FILENAME

        # If directory does not exist, create it.
        if not os.path.exists(self.OUTPUT_FOLDER):
            os.mkdir(self.OUTPUT_FOLDER)

        # If file exists, rename it with old.
        if os.path.exists(self.FILE_PATH):
            os.rename(self.FILE_PATH, self.FILE_PATH+'_old')

        file = h5py.File(self.FILE_PATH, 'a')
        file.close()

    def f(self):
        file = h5py.File(self.FILE_PATH, 'r+')
        return file

    def write(self, time, name, data):
        time = np.around(time, 4)
        file = self.f()
        file.create_dataset(str(time) + '/' + str(name), data=data, chunks=True, compression='gzip', compression_opts=4)
        file.close()

    def write_attr(self,obj):
        file = self.f()
        for key, value in vars(obj).items():
            try:
                file.attrs.create(key,value)
            except:
                file.attrs.create(key,repr(value),dtype='<S' + str(len(repr(value))))
        file.close()



def get_args():
    """
    Argument parser for initial conditions and userdata file.

    """

    parser = argparse.ArgumentParser(description='Python solver for the heat equation')

    parser.add_argument('-ic', '--initial_conditions', action='store', dest='ic', help='<Required> Set initial conditions', required=True,choices={'bins', 'gw'})

    args = parser.parse_args() # collect cmd line args
    ic = args.ic

    if   ic == 'bins':
        from input.baroclinic_instability import UserData, sol_init
        # raise NotImplementedError("random IC not yet implemented")
    elif ic == 'gw': 
        from input.gravity_wave import UserData, sol_init

    return UserData, sol_init



