class SystemParameters:
    def __init__(self):
        self.n_Tx = 3  # Bob_1, Bob_2, and Eve
        ###
        self.n_Rx = 30
        self.snrdB_Bob = 5  # Bob_1, Bob_2, ..., Bob_M have the same snrdB
        self.DOA_Bob_1 = - 40.5  # from -90 degree to +90 degree
        self.DOA_Bob_2 = 15
        self.DOA_Bob_list = [self.DOA_Bob_1, self.DOA_Bob_2]
        self.snrdB_Eve = 3
        self.DOA_Eve = 10  # from -90 degree to +90 degree
        ###
        self.Rician_factor = 2
        self.n_NLOS_paths = 10
        ###
        self.SNR_Bob = 10**(self.snrdB_Bob/10)
        self.SNR_Eve = 10**(self.snrdB_Eve/10)
        self.list_of_SNRs = [self.SNR_Bob, self.SNR_Bob, self.SNR_Eve]
        # self.list_of_DOAs = [self.DOA_Bob_1, self.DOA_Bob_2, self.DOA_Eve]
        self.list_of_DOAs = [i for i in self.DOA_Bob_list]
        self.list_of_DOAs.append(self.DOA_Eve)
        self.num_angles = 180
        self.max_delta_theta = 90.0  # 90 degree


# =============================================================================
""" Save the system parameters as an object for later use """
# import pickle
# SysParam = SystemParameters()
# # save the SysParam object as a pickle-type file
# with open('input/mySysParam.pickle', 'wb') as f:
#     pickle.dump(SysParam, f)

# # load the pickle-type file
# with open('input/mySysParam.pickle', 'rb') as f:
#     SysParam = pickle.load(f)
