import numpy as np 
import matplotlib.pyplot as plt 
import pdb
import matplotlib.colors as colours




def get_index(index):



    if index=="HdA":
        index_array=HdA
        index_name=r"H$_{\delta, A}$"
    elif index=="HdF":
        index_array=HdF
        index_name=r"H$_{\delta, F}$"
    elif index=="CN1":
        index_array=CN1
        index_name="CN1"
    elif index=="CN2":
        index_array=CN2
        index_name="CN2"
    elif index=="Ca4227":
        index_array=Ca4227
        index_name="Ca4227"
    elif index=="G4300":
        index_array=G4300
        index_name="G4300"
    elif index=="HgA":
        index_array=HgA
        index_name="HgA"
    elif index=="HgF":
        index_array=HgF
        index_name="HgF"
    elif index=="Fe4383":
        index_array=Fe4383
        index_name="Fe4383"
    elif index=="Ca4455":
        index_array=Ca4455
        index_name="Ca4455"
    elif index=="Fe4531":
        index_array=Fe4531
        index_name="Fe4531"
    elif index=="C24668":
        index_array=C24668
        index_name="C24668"
    elif index=="Hb":
        index_array=Hb
        index_name="Hb"
    elif index=="Fe5015":
        index_array=Fe5015
        index_name="Fe5015"
    elif index=="Mg1":
        index_array=Mg1
        index_name="Mg1"
    elif index=="Mg2":
        index_array=Mg2
        index_name="Mg2"
    elif index=="Mgb":
        index_array=Mgb
        index_name="Mgb"
    elif index=="Fe5270":
        index_array=Fe5270
        index_name="Fe5270"
    elif index=="Fe5335":
        index_array=Fe5335
        index_name="Fe5335"
    elif index=="Fe5406":
        index_array=Fe5406
        index_name="Fe5406"
    elif index=="Fe5709":
        index_array=Fe5709
        index_name="Fe5709"
    elif index=="Fe5782":
        index_array=Fe5782
        index_name="Fe5782"
    elif index=="NaD":
        index_array=NaD
        index_name="NaD"
    elif index=="TiO1":
        index_array=TiO1
        index_name="TiO1"
    elif index=="TiO2":
        index_array=TiO2
        index_name="TiO2"
    elif index=="MgFe":
        index_array=MgFe
        index_name="MgFe"

    else:
        print "{} is not a correct index".format(index)
        print "Choose from [HdA,HdF,CN1,CN2,Ca4227,G4300,HgA,HgF,Fe4383,Ca4455,Fe4531,C24668,Hb,Fe5015,Mg1,Mg2,Mgb,Fe5270,Fe5335,Fe5406,Fe5709,Fe5782,NaD,TiO1,TiO2,MgFe]"
        raise NameError
    return index_array, index_name
#################################################################################################################################################

def get_numpy_indices_for_params(alpha_fe=None, Z=None, age=None):

    """
    There are 4 values of alpha/fe, 6 values of Z/H and 20 of age. This function returns the index corresponding to the value you want.

    Must only be called with one of alpha_fe, Z or age! There's probably a better way to do this...

    alpha_fe- the value of Alpha/Fe to find the index at: must be one of  [-0.3, 0.0, 0.3, 0.5]
    Z- the value of Z/H to find the index at: must be one of  [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]
    age- the value of age to find the index at: must be one of  [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]

    """

    if alpha_fe is not None:
        if alpha_fe==-0.3:
            alpha_fe_ind=0
        elif alpha_fe==0.0:
            alpha_fe_ind=1
        elif alpha_fe==0.3:
            alpha_fe_ind=2
        elif alpha_fe==0.5:
            alpha_fe_ind=3
        else:
            ValueError("Alpha/Fe must be one of  [-0.3, 0.0, 0.3, 0.5]")

        return alpha_fe_ind

    if Z is not None:
        if Z == -2.25:
            Z_ind=0
        elif Z == -1.35:
            Z_ind=1
        elif Z == -0.33:
            Z_ind=2
        elif Z == 0.0:
            Z_ind=3
        elif Z == 0.35:
            Z_ind=4
        elif Z == 0.67:
            Z_ind=5
        else:
            ValueError("Z must be one of  [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]")
        return Z_ind

    if age is not None:
        try:
            age_ind=np.where(np.array([0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0])==age)[0][0]
        except:
            ValueError("Age must be one of  [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]")
        return age_ind
#################################################################################################################################################



def plot_index_vs_age(ax, age, index, index_name, alpha_fe=0.0, Z=0.0):

    """Plot one index from the Thomas models against age, at fixed Alpha/Fe abundance and Z/H.

    Inputs:
        ax- an axis object
        Z- Z/H from the tmh_*.dat file
        index- a numpy array from the tmj_*.dat file. 
        index_name- a string used for the plot axis labels
        alpha_fe- the value of Alpha/Fe to plot at: must be one of  [-0.3, 0.0, 0.3, 0.5]
        Z- the Z/H to plot at: must be one of  [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]
    """

    index=index.reshape(4, 6, 20)
    age=age.reshape(4, 6, 20)

    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    Z_ind=get_numpy_indices_for_params(Z=Z)

    
    ax.plot(age[alpha_fe_ind, Z_ind, :], index[alpha_fe_ind, Z_ind, :], label=r"Z/H={}, $\alpha$/Fe={}".format(Z, alpha_fe))

    ax.set_xlabel("Age")
    ax.set_ylabel("{}".format(index_name))
#################################################################################################################################################

def plot_index_vs_Z(ax, Z, index, index_name, alpha_fe=0.0, age=13.0):

    """Plot one index from the Thomas models against Z, at fixed Alpha/Fe abundance and age.

    Inputs:
        ax- an axis object
        Z- Z/H from the tmh_*.dat file
        index- a numpy array from the tmj_*.dat file. 
        index_name- a string used for the plot axis labels
        alpha_fe- the value of Alpha/Fe to plot at: must be one of  [-0.3, 0.0, 0.3, 0.5]
        age- the age to plot at: must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]
    """

    #reshape the arrays to get them into [alpha, age, Z]
    index=np.transpose(index.reshape(4, 6, 20), (0, 2, 1))
    Z=np.transpose(Z.reshape(4, 6, 20), (0, 2, 1))

    #get the indices corresponding to the alpha and age we want
    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    age_ind=get_numpy_indices_for_params(age=age)
    
 
    
    
    ax.plot(Z[alpha_fe_ind, age_ind, :], index2[alpha_fe_ind, age_ind, :], label=r"$\alpha$/Fe={}, age={}".format(alpha_fe, age), linewidth=3.0)

    ax.set_xlabel("Z/H")
    ax.set_ylabel("{}".format(index_name))

#################################################################################################################################################

def _plot_alpha_grid(ax, index1, index2, age=None, Z=None):

    """
    Plot a grid of grey lines of the same alpha, whilst one of Z or age are kept fixed and the other varies along the coloured lines in the graph.

    ax- an axis object to plot on
    index1- a numpy array from the tmj_*.dat file, in the correct shape (4, 6, 20). 
    index2- as above
    age- the fixed value of age to plot everything at. If None, this is the parameter we want to vary
    Z- the fixed value of Z to plot everything at. If None, this is the parameter we want to vary.

    This function is called like:

    _plot_alpha_grid(ax, index1, index2, age=13.0)

    which will plot the appropriate grids of changing alpha enhancement at a fixed age of 13Gyr, whilst the main lines on the plot vary as a function of Z


    """

    if age is None and Z is None:
        ValueError("Pick either age or Z to keep constant")

    if age is not None:
        age_ind=get_numpy_indices_for_params(age=age)
        #Cycle through the 6 metallicities
        for i in range(0, 6, 1):
            ax.plot(index1[:, i, age_ind], index2[:, i, age_ind], c="grey")
        ax.plot(index1[:, -1, age_ind], index2[:, -1, age_ind], c="grey")
    if Z is not None:
        Z_ind=get_numpy_indices_for_params(Z=Z)
        #Cycle through the 20 ages
        for i in range(0, 20, 2):
            ax.plot(index1[:, Z_ind, i], index2[:, Z_ind, i], c="grey")
        ax.plot(index1[:, Z_ind, -1], index2[:, Z_ind, -1], c="grey")

#################################################################################################################################################
def _plot_age_grid(ax, index1, index2, alpha_fe=None, Z=None):

    """
    Plot a grid of grey lines of the same age, whilst one of Z or alpha/fe are kept fixed and the other varies along the coloured lines in the graph.

    ax- an axis object to plot on
    index1- a numpy array from the tmj_*.dat file, in the correct shape (4, 6, 20). 
    index2- as above
    alpha_fe- the fixed value of alpha/fe to plot everything at. If None, this is the parameter we want to vary
    Z- the fixed value of Z to plot everything at. If None, this is the parameter we want to vary.

    This function is called like:

    _plot_age_grid(ax, index1, index2, alpha_fe=0.0)

    which will plot the appropriate grids of changing age at a fixed alpha/fe of 0.0, whilst the main lines on the plot vary as a function of Z


    """

    if alpha_fe is None and Z is None:
        ValueError("Pick either alpha/fe or Z to keep constant")

    if alpha_fe is not None:
        alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
        #Cycle through the 6 metallicities
        for i in range(0, 6, 1):
            ax.plot(index1[alpha_fe, i, :], index2[alpha_fe, i, :], c="grey")
        ax.plot(index1[alpha_fe, -1, :], index2[alpha_fe, -1, :], c="grey")
    if Z is not None:
        Z_ind=get_numpy_indices_for_params(Z=Z)
        #Cycle through the 4 alpha/fe values
        for i in range(0, 4, 1):
            ax.plot(index1[i, Z_ind, :], index2[i, Z_ind, :], c="grey")
        ax.plot(index1[-1, Z_ind, :], index2[-1, Z_ind, :], c="grey")

#################################################################################################################################################
def _plot_Z_grid(ax, index1, index2, alpha_fe=None, age=None):

    """
    Plot a grid of grey lines of the same Z, whilst one of age or alpha/fe are kept fixed and the other varies along the coloured lines in the graph.

    ax- an axis object to plot on
    index1- a numpy array from the tmj_*.dat file, in the correct shape (4, 6, 20). 
    index2- as above
    alpha_fe- the fixed value of alpha/fe to plot everything at. If None, this is the parameter we want to vary
    age- the fixed value of age to plot everything at. If None, this is the parameter we want to vary.

    This function is called like:

    _plot_Z_grid(ax, index1, index2, age=13.0)

    which will plot the appropriate grids of changing Z at a fixed age of 13Gyr, whilst the main lines on the plot vary as a function of alpha/fe


    """

    if alpha_fe is None and age is None:
        ValueError("Pick either alpha/fe or Z to keep constant")

    if alpha_fe is not None:
        alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
        #Cycle through the 20 ages
        for i in range(0, 20, 4):
            ax.plot(index1[alpha_fe, :, i], index2[alpha_fe, :, i], c="grey")
        ax.plot(index1[alpha_fe, :, -1], index2[alpha_fe, :, -1], c="grey")
    if age is not None:
        age_ind=get_numpy_indices_for_params(age=age)
        #Cycle through the 4 alpha/fe values
        for i in range(0, 4, 1):
            ax.plot(index1[i, :, age_ind], index2[i, :, age_ind], c="grey")
        ax.plot(index1[-1, :, age_ind], index2[-1, :, age_ind], c="grey")

#################################################################################################################################################

def _plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.0, Z=0.0):

    """Plot two indices from the Thomas models at fixed Alpha/Fe abundance and Z/H.

    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        alpha_fe- the value of alpha/fe we want. Must be [alpha/Fe] = -0.3, 0.0, 0.3, 0.5
        Z- the value of Z/H we want. Must be [Z/H] = [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]

          

    """
   
    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    Z_ind=get_numpy_indices_for_params(Z=Z)    


    ax.plot(index1[alpha_fe_ind, Z_ind, :], index2[alpha_fe_ind, Z_ind, :], label=r"Z/H={}, $\alpha$/Fe={}".format(Z, alpha_fe), linewidth=3.0)
   
        

#################################################################################################################################################
def _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=13.0):

    """Plot two indices from the Thomas models at fixed Alpha/Fe and age.
    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file, in the correct shape (4, 6, 20). 
        index2- as above       
        alpha_fe- the value of alpha/fe we want. Must be [alpha/Fe] = -0.3, 0.0, 0.3, 0.5
        age- the value of age we want. Must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]

       

    """

    age=float(age)

    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    age_ind=get_numpy_indices_for_params(age=age)

    #The colours are a function of Alpha Enhancements so N=4
    N=4

    c=cm(1.0*alpha_fe_ind/N)


    """
    #Useful for seeing how the model parameters move
    solar_alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=0.0)
    ten_Gyr_age_ind=get_numpy_indices_for_params(age=10.0)
    solar_metallicity_ind=get_numpy_indices_for_params(Z=0.0)
    """
    
   


    ax.plot(index1[alpha_fe_ind, :, age_ind], index2[alpha_fe_ind, :, age_ind], label=r"$\alpha$/Fe={}, age={}".format(alpha_fe, age), linewidth=3.0, zorder=10, c=c)
    ax.scatter(index1[alpha_fe_ind, :, age_ind], index2[alpha_fe_ind, :, age_ind], marker="o", s=np.linspace(50, 300, 6), facecolors="w", linewidth=3.0, zorder=10)


#################################################################################################################################################





#################################################################################################################################################
def _plot_at_fixed_Z_and_age(ax, index1, index2, Z=0.0, age=13.0):

    """Plot two indices from the Thomas models at fixed Z/H and age.
    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        Z- the value of Z/H we want. Must be [Z/H] = [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]
        age- the value of age we want. Must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]

     

    """
    age=float(age)

    Z_ind=get_numpy_indices_for_params(Z=Z)    
    age_ind=get_numpy_indices_for_params(age=age)
    
    ax.plot(index1[:, Z_ind, age_ind], index2[:, Z_ind, age_ind], label="Z/H={}, age={}".format(Z, age), linewidth=3.0)

#################################################################################################################################################  
  
def _plot_line_vary_age(ax, index1, index2, alpha_fe=0.0, Z=0.0):

    """
    Plot a single line varying only the age, keeping alpha/fe and Z fixed at certain values
    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        Z- the value of Z/H we want. Must be [Z/H] = [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]
        age- the value of age we want. Must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]
    """
    Z_ind=get_numpy_indices_for_params(Z=Z)    
    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)

    #Only plot the points at ages 1Gyr, 5Gyr, 10Gyr, 13Gyr
    ages=np.array([0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0])
    points=np.array([1.0, 5.0, 10.0, 13.0])
    age_mask=np.in1d(ages, points)

    ax.scatter(index1[alpha_fe_ind, Z_ind, age_mask], index2[alpha_fe_ind, Z_ind, age_mask], marker="s", s=ages[age_mask]*10, c="r")
    ax.plot(index1[alpha_fe_ind, Z_ind, age_mask], index2[alpha_fe_ind, Z_ind, age_mask], linewidth=2.0, linestyle="dotted", c="r")

    for x, y, age_val in zip(index1[alpha_fe_ind, Z_ind, age_mask], index2[alpha_fe_ind, Z_ind, age_mask], points):
        ax.annotate("{} Gyr".format(age_val), (x, y), xytext=(-10, 5), textcoords='offset points', horizontalalignment='right', verticalalignment='bottom')




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  


def plot_index_vs_index(ax, index1, index1_name, index2, index2_name):
    

    #_plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.3, Z=-2.25, grid=False)
    #_plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.3, Z=-1.35, grid=False)

    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=-0.3, age=13.0)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=13.0)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.3, age=13.0)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.5, age=13.0)
    _plot_alpha_grid(ax, index1, index2, age=13.0)
    

    #_plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=1.0)
    #_plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=5.0)



    _plot_line_vary_age(ax, index1, index2, alpha_fe=0.0, Z=-2.25)
    _plot_line_vary_age(ax, index1, index2, alpha_fe=0.0, Z=0.0)
    _plot_line_vary_age(ax, index1, index2, alpha_fe=0.0, Z=0.67)

       

    #_plot_at_fixed_alpha(ax, index1, index2, 0.0)
   

    ax.set_xlabel("{}".format(index1_name))
    ax.set_ylabel("{}".format(index2_name))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Plot optical indices from the Thomas models against each other, with or without data points")
    parser.add_argument("Index1", type=str, help="The first index to plot. Will be on the Y axis")
    parser.add_argument("Index2", type=str, help="The second index to plot. Will be on the x axis")
    parser.add_argument("-d1", "--datafile1", type=str, help="Data file containing measurements of the first index")
    parser.add_argument("-d2", "--datafile2", type=str, help="Data file containing measurements of the second index")

    args=parser.parse_args()



    index1=args.Index1
    index2=args.Index2
    if args.datafile1 is not None:
        fname1=args.d1
    if args.datafile2 is not None:
        fname2=args.d2



    age,Z_H,alpha_fe,HdA,HdF,CN1,CN2,Ca4227,G4300,HgA,HgF,Fe4383,Ca4455,Fe4531,C24668,Hb,Fe5015,Mg1,Mg2,Mgb,Fe5270,Fe5335,Fe5406,Fe5709,Fe5782,NaD,TiO1,TiO2=np.genfromtxt("tmj/tmj.dat", unpack=True)

    MgFe=np.sqrt(Mgb*(0.72*Fe5270+0.28*Fe5335))



    #Plotting Commands
    Z_sizes=[100, 150, 200, 250, 300, 350]

    cm = plt.get_cmap('plasma') 


    index1, index1_name=get_index(index1)
    index2, index2_name=get_index(index2)


    #Make the indices into the correct shape for plotting
    #We want everything to be in a 3D format, of shape (4, 6, 20)
    #This allows us to choose which 4 slpah enhancements, which 6 Z/Hs and which 20 ages to plot very easily.
    #I.e index[0, 0, :] would plot the index as a function of age, for the first alpha/Fe (-0.3) and first Z/H (-2.25) in the models


    age=age.reshape(4, 6, 20)
    index1=np.swapaxes(np.transpose(index1.reshape(4, 6, 20), (0, 2, 1)), 1, 2)
    index2=np.swapaxes(np.transpose(index2.reshape(4, 6, 20), (0, 2, 1)), 1, 2)

    #alpha_fe=np.swapaxes(np.transpose(alpha_fe.reshape(4, 6, 20), (2, 1,0 )), 0, 2)

    


    #Index 1 vs Index 2
    fig, ax=plt.subplots(ncols=1, nrows=1)
    plot_index_vs_index(ax, index1, index1_name, index2, index2_name)
    legend2=ax.legend(fancybox=True, fontsize=20, loc="best")



    

    plt.show()