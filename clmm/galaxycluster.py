'''
Define CalaxyClusters class
Who to blame for problems: Michel A.
'''

Position = namedtuple('Position', ['ra', 'dec'])
Profile = namedtuple('Profile', ['distances', 'dimension'])

for n in ['Position', 'Pofile']:

    exec('%00 = %s(*[None for i in %s._fields])'%(n, n))
    exec('%s_type = type(%)'%(n, n))


class GalaxyCluster():
    '''
    - read data
    - write data
    - disting data
    '''

    def __init__(self):
        '''
        '''
        self.data = {}
        self.homelocal = '.'

    def _add(self, data_external):
        '''
        data_external - dict with all the data in the correct formats
        '''

        for name, data_ext in data_external.items():

            for data_int in self.data:

                if type(data_int) == type(data_ext):

                    if data_int.metadata == data_ext.metadata:

                        print('Overwritting %s[%s] data', %(name, data_ext.metadata))

            self.data[name] = data_external

    def _listprofiles():
        '''
        '''
        print([d.dimension for d in self.data['profiles']])
        check_data()

    def showdata(self):
        '''
        '''

        print(self.data.keys())

    def measure_profile(self):
        '''
        '''

    def fit_profile(self):
        '''
        '''

    def func(self):
        '''
        '''
