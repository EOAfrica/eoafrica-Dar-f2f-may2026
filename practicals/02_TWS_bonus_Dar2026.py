#!/usr/bin/env python
# coding: utf-8

# <img src="media/Banner_waterlevel+esalogo.svg" width="100%" alt="Banner for EO AFRICA course" />
# 
# 
# *R. Rietbroek, May 2026*
# 
# <font color=#cf0072>
# 
# # Animating TWS change for the Greater Horn of Africa
# </font>

# In[5]:




# In[6]:


import numpy as np
import xarray as xr
from shxarray.core.logging import setErrorLevel
from glob import glob
import os
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


# In[7]:


import warnings
warnings.filterwarnings("ignore")


# In[8]:


# make animations for dedicated regions

def make_anim(dain,fout):
    # plt.style.use('dark_background')
    #Apply synthesis
    # jakobwsne=[-49.5, 70,68,-46]
    lon=np.arange(36,54,0.1)
    lat=np.arange(-5,11,0.1)
    
    samplelon=np.array([45.20393,38.518])
    samplelat=np.array([4.73760, 3.656])
    alphaselect=2e-1
    # breakpoint()
    dagrd=dain.solution.sel(alpha=alphaselect).compute().sh.tws(ingravtype='stokes').sh.synthesis(engine='shlib',lon=lon,lat=lat)
    
    ddk='DDK9'
    # daddk=dain.solution.sel(alpha=0).compute().sh.filter(ddk).sh.tws(ingravtype='stokes').sh.synthesis(lon=samplelon,lat=samplelat,gtype='point')
    # dagrd.to_netcdf(fout.replace("mkv",'nc'))
    metadata = dict(title='TWS storage change', artist='Matplotlib')
    writer = animation.FFMpegWriter(fps=8, metadata=metadata)

    vmax=0.5
    vmin=-vmax
    cmap='RdBu'
    fig = plt.figure(figsize=(14, 14))
    # proj=ccrs.NorthPolarStereo(central_longitude=-40.0)
    projplate=ccrs.PlateCarree()
    proj=ccrs.PlateCarree()
    
    # proj=ccrs.AlbersEqualArea(central_longitude=-40.0, central_latitude=65.0)
    axline = fig.add_subplot(2, 1, 2)
    dagrd.sel(lon=samplelon[0],lat=samplelat[0],method='nearest').plot(ax=axline,label=f'point 1 grad reg, alpha={alphaselect}',color='tab:orange')
    # dagrd.sel(lon=samplelon[1],lat=samplelat[1],method='nearest').plot(ax=axline,label=f'point 2 grad reg, alpha={alphaselect}',color='tab:orange',ls='--')
    # daddk.sel(lon=samplelon[0],lat=samplelat[0]).plot(ax=axline,color='tab:green',label=ddk)
    # daddk.sel(lon=samplelon[1],lat=samplelat[1]).plot(ax=axline,color='tab:green',label=ddk,ls='--')
    axline.legend()
    axline.set_ylabel('tws [m]')
    ax = fig.add_subplot(2, 1, 1, projection=proj)
    ax.plot(samplelon[0],samplelat[0],marker='+',markersize=30)
    # ax.plot(samplelon[1],samplelat[1],marker='+',markersize=30)
    # ax.set_xlim(lon[0,-1])
    # ax.set_ylim(lat[0,-1])
    
    coastline=ax.coastlines(lw=0.5,zorder=20,resolution='10m')
    plt.tight_layout()
    plt.rcParams.update({'font.size': 17})
    
    with writer.saving(fig, fout, 150):
        for i in tqdm(range(len(dagrd.time))):
            ttag=dagrd.time[i].values
            if i== 0:
                ar=dagrd.isel(time=i).plot(ax=ax,vmin=vmin,vmax=vmax,cmap=cmap,cbar_kwargs=dict(location='right'))
                # ax.add_feature(cf.COASTLINE)
                vbar=axline.axvline(ttag,color='tab:orange')
            else:
                ar.set_array(dagrd.isel(time=i).data)
                vbar.set_data([ttag, ttag], [0, 1])
            ax.set_title(f'time={dagrd.time[i].dt.year.item()}-{dagrd.time[i].dt.month.item():02d}')
            writer.grab_frame()
    





# In[ ]:


fbase='GHAfrica'
outdir_select="../data/ITSG_regv2"
#collect all solutions
grcsolf=sorted(glob(outdir_select+"/ITSG-Grace*.nc"))
alpha_select=1e-3
#read all data and only select a certain alpha
dsgrc=xr.open_mfdataset(grcsolf,combine='nested',concat_dim='time')#.sel(alpha=alpha_select)
#add time coordinate


dsgrc=dsgrc.sh.build_nmindex()
# ddk='DDK9'
# daddk=dsgrc.solution.sel(alpha=0).compute().sh.filter(ddk).sh.tws(ingravtype='stokes')



#make a global animation of tws
fout=f"media/grc_reg_{fbase}.mkv"
dagrd=make_anim(dsgrc,fout=fout)

