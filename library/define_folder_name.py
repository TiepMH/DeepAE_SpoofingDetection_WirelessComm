def cast_DOA_to_string(DOA):
    DOA_str = str(DOA)  # for example, str(-1.2) = ['-1.2']
    temp = DOA_str.split('.')  # temp = ['-1', '2'] with temp[0] = '-1'
    if len(temp) > 1:
        if DOA >= 0:
            kq = temp[0] + 'p' + temp[1]
        else:
            kq = 'minus' + str(abs(int(temp[0]))) + 'p' + temp[1]
    else:
        if DOA >= 0:
            kq = temp[0]
        else:
            kq = 'minus' + str(abs(int(temp[0])))
    return kq + 'deg'


def name_of_folder(n_Rx,
                   SNR_Bob, DOA_Bob,
                   SNR_Eve, DOA_Eve,
                   K, NLOS):
    DOA_Bob_str = cast_DOA_to_string(DOA_Bob)
    DOA_Eve_str = cast_DOA_to_string(DOA_Eve)
    name = 'nRx' + str(n_Rx) \
            + '__B' + str(SNR_Bob) + 'dB_' + DOA_Bob_str \
            + '__E' + str(SNR_Eve) + 'dB_' + DOA_Eve_str \
            + '__K' + str(K) + '__NLOS' + str(NLOS)
    return name


# =============================================================================
def srt_for_multiple_Bobs(n_Tx, snrdB_Bob, DOA_Bob_list):
    Bob_angles = ''
    for i in range(n_Tx-1):  # excluding Eve
        DOA_Bob_i = DOA_Bob_list[i]
        DOA_Bob_i_str = cast_DOA_to_string(DOA_Bob_i)
        Bob_angles += DOA_Bob_i_str + '_'
    kq = '__B' + str(snrdB_Bob) + 'dB_' + Bob_angles
    return kq


def my_folder_name(n_Tx, n_Rx,
                   snrdB_Bob, DOA_Bob_list,
                   snrdB_Eve, DOA_Eve,
                   K, NLOS):
    # DOA_Bob_str = cast_DOA_to_string(DOA_Bob)
    DOA_Eve_str = cast_DOA_to_string(DOA_Eve)
    name = 'nRx' + str(n_Rx) \
            + srt_for_multiple_Bobs(n_Tx, snrdB_Bob, DOA_Bob_list) \
            + '_E' + str(snrdB_Eve) + 'dB_' + DOA_Eve_str \
            + '__K' + str(K) + '__NLOS' + str(NLOS)
    return name
