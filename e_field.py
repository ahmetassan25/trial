# =============================================================================
# Field measurements from the horizontal and vertical electrodes
# CH1 - CH2 gives horizontal field
# CH1 - CH3 gives vertical field 
# unit is uv/mm
# =============================================================================
def efield_surface(trialno):
    
    import numpy as np
    from functools import reduce
    import scipy.io as sio

    mat = sio.loadmat('trial{}.mat'.format(trialno))
    data = mat['data']; 
    
    ch1 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,0].reshape(10,-1)))))
    ch2 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,1].reshape(10,-1)))))
    ch3 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,2].reshape(10,-1)))))
    
    horizontal = 100*(ch1.max()-np.mean(ch1[2475:2495])-ch2.max()-np.mean(ch2[2475:2495]))/250  
    vertical = 100*(ch1.max()-np.mean(ch1[2475:2495])-ch3.max()-np.mean(ch3[2475:2495]))/250
    
    return [horizontal, vertical]

# =============================================================================
# Field measurements from the helical electrode 
# Two trial (from 125 um and 375 um) are necessary to calculate the field through the depth.
# =============================================================================
def efield_depth(trialno):

    import numpy as np
    from functools import reduce
    import scipy.io as sio
    
    all_chs = []
    for i in trialno:
        mat = sio.loadmat('trial{}.mat'.format(i))
        data = mat['data']; 

        ch1 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,0].reshape(10,-1)))))
        ch2 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,1].reshape(10,-1)))))
        ch3 = np.array(list(map(lambda y: y/10, reduce(lambda x,y: x+y,data[:,2].reshape(10,-1)))))
        
        all_ch = [ch1.max()-np.mean(ch1[2475:2495]),ch2.max()-np.mean(ch2[2475:2495]),ch3.max()-np.mean(ch3[2475:2495])];
        all_chs.append(all_ch)

    all_chs = np.array(all_chs)
    ch_results = 100*(all_chs[0,:]-all_chs[1,:])/250
    
    return ch_results