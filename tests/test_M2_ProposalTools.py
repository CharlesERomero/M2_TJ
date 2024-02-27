import pytest
import M2_ProposalTools.WorkHorse as WH
import M2_ProposalTools.FilterImages as FI
import M2_ProposalTools.MakeRMSmap as MRM
import numpy as np
import os
import astropy.units as u
import M2_ProposalTools.ModelFitting as MF
from astropy.io import fits                # To read/write fits

def test_locate_xfer_files():

    #xferfile       = "xfer_Function_3p0_21Aonly_PCA5_0f08Filtering.txt"
    xferfile       = "src/M2_ProposalTools/xfer_Function_3p0_21Aonly_PCA5_0f08Filtering.txt"
    fileexists     = os.path.exists(xferfile)
    assert fileexists

    
    
def test_HDU_generation():

    Center  = [280.0, 45.0]                     # Arbitrary RA and Dec
    pixsize = 2.0                               # arcseconds
    xsize   = 12.0                              # arcminutes; this is a bit larger than typical
    ysize   = 12.0                              # arcminutes
    nx      = int(np.round(xsize*60/pixsize))   # Number of pixels (must be an integer!)
    ny      = int(np.round(ysize*60/pixsize))   # Number of pixels (must be an integer!)
    TemplateHDU = MRM.make_template_hdul(nx,ny,Center,pixsize)

    assert len(TemplateHDU) == 1

def test_RMS_generation():    

    Center  = [280.0, 45.0]                     # Arbitrary RA and Dec
    pixsize = 2.0                               # arcseconds
    xsize   = 12.0                              # arcminutes; this is a bit larger than typical
    ysize   = 12.0                              # arcminutes
    nx      = int(np.round(xsize*60/pixsize))   # Number of pixels (must be an integer!)
    ny      = int(np.round(ysize*60/pixsize))   # Number of pixels (must be an integer!)
    Ptgs    = [Center]                          # Pointings should be a list of (RA,Dec) array-like values.
    sizes   = [-3.5]                            # Let's try offset scans! Here, 3.5' scans, offset
    times   = [10.0]                            # 10 hours
    offsets = [1.5]                               # 1.5 arcminute offset (the default, but we may change it)

    TemplateHDU = MRM.make_template_hdul(nx,ny,Center,pixsize)
    RMSmap,nscans = MRM.make_rms_map(TemplateHDU,Ptgs,sizes,times,offsets=offsets)

    nPixX,nPixY = RMSmap.shape
    c1          = (nx == nPixX)
    c2          = (ny == nPixY)
    c3          = (np.max(RMSmap) > 0)
    assert c1*c2*c3

def test_A10_generation():

    M500       = 3.9*1e14*u.M_sun
    z          = 0.86
    pixsize    = 2.0
    ymap       = WH.make_A10Map(M500,z,pixsize=pixsize,Dist=True)
    c1         = np.max(ymap) > 0
    c2         = np.max(ymap) < 1e-2
    
    assert c1*c2

def test_AlphaOmega():


    path    = os.path.abspath(FI.__file__)
    outdir  = path.replace("FilterImages.py","")
    M5_14    = 6.0
    M500     = M5_14*1e14*u.M_sun
    z        = 0.5
    pixsize  = 4.0
    
    times    = [10,10]
    ptgs     = [[180,45.0],[180,45.0]]
    sizes    = [3.5,3.5]
    offsets  = [1.5,0]
    
    FilterHDU,SmoothHDU,SkyHDU = WH.lightweight_simobs_A10(z,M500,conv2uK=True,pixsize=pixsize,ptgs=ptgs,sizes=sizes,times=times,offsets=offsets,Dist=True)

    pixstr = "{:.1f}".format(pixsize).replace(".","p")
    zstr   = "{:.1f}".format(z).replace(".","z")
    Mstr   = "{:.1f}".format(M5_14).replace(".","m")
    sss    = ["{:.1f}".format(mysz).replace(".","s") for mysz in sizes]
    sts    = ["{:.1f}".format(mytime).replace(".","h") for mytime in times]
    ssstr  = "_".join(sss)
    ststr  = "_".join(sts)
    InputStr = "_".join([zstr,Mstr,ssstr,ststr,pixstr])

    #filename = "SimulatedObs_Unsmoothed_"+InputStr+".fits"
    #FilterHDU.writeto(outdir+filename,overwrite=True)
    #filename2 = "SimulatedObs_Smoothed_"+InputStr+".fits"
    #SmoothHDU.writeto(outdir+filename2,overwrite=True)
    #filename3 = "SimulatedSky_"+InputStr+".fits"
    #SkyHDU.writeto(outdir+filename3,overwrite=True)

    SkyHDU[0].data *= -3.3e6 # Run once 

    SBfn = "SimulatedObs_SBprofiles_"+InputStr+".png"
    MF.plot_SB_profiles(FilterHDU,SkyHDU,outdir,SBfn)

    pngname  = "SimulatedObservations_"+InputStr+"_RMSimage.png"
    vmin     = 15.0  # uK
    vmax     = 420.0 # uK
    MRM.plot_rms_general(SmoothHDU,outdir+pngname,ncnts=5,vmin=vmin,vmax=vmax)

    #inputHDU = fits.open(outdir+filename)
    inputHDU = FilterHDU.copy()
    nsteps   = 100
    nsstr    = "_"+repr(nsteps)+"steps"
    outbase = "NP_fit_"+InputStr+nsstr+"_corner.png"
    MF.fit_spherical_model(z,M500,inputHDU,outdir=outdir,nsteps=nsteps,outbase=outbase)   # 100 for testing purposes
