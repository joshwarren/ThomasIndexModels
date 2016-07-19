import numpy as np 
import matplotlib.pyplot as plt 
import pdb




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

    else:
        print "{} is not a correct index".format(index)
        print "Choose from [HdA,HdF,CN1,CN2,Ca4227,G4300,HgA,HgF,Fe4383,Ca4455,Fe4531,C24668,Hb,Fe5015,Mg1,Mg2,Mgb,Fe5270,Fe5335,Fe5406,Fe5709,Fe5782,NaD,TiO1,TiO2]"
        raise NameError
    return index_array, index_name


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



def _plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.0, Z=0.0, alpha_grid=False, Z_grid=False):

    """Plot two indices from the Thomas models at fixed Alpha/Fe abundance and Z/H.

    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        index_name1- a string used for the plot axis labels
        index_name2- a string used for the plot axis labels
        alpha_fe- the value of alpha/fe we want. Must be [alpha/Fe] = -0.3, 0.0, 0.3, 0.5
        Z- the value of Z/H we want. Must be [Z/H] = [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]

        alpha_grid- plot a grid by joining values of the same Z/H and age but different alpha/fe??
        Z_grid- plot a grid by joining values of the same alpha and age but different Z/H?

    

    """

    index1=index1.reshape(4, 6,20)
    index2=index2.reshape(4, 6,20)

    
    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    Z_ind=get_numpy_indices_for_params(Z=Z)    


    ax.plot(index1[alpha_fe_ind, Z_ind, :], index2[alpha_fe_ind, Z_ind, :], label=r"Z/H={}, $\alpha$/Fe={}".format(Z, alpha_fe), linewidth=3.0)

    #add grey lines to make a grid- i.e join up all of the first points, some of the middle points and the last point of each line, to show how changing
    #Z/H moves you in the model space 
    if alpha_grid:
        for i in range(0, 20, 4):
            ax.plot(index1[:, Z_ind,  i], index2[:, Z_ind, i],  c="grey")
        ax.plot(index1[:, Z_ind,  -1], index2[:, Z_ind, -1],  c="grey")
    if Z_grid:
        for i in range(0, 20, 4):
            ax.plot(index1[alpha_fe_ind, :,  i], index2[alpha_fe_ind, :, i],  c="grey")
        ax.plot(index1[alpha_fe_ind, :,  -1], index2[alpha_fe_ind, :, -1],  c="grey")
        

#################################################################################################################################################
def _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=13.0, alpha_grid=False, age_grid=False):

    """Plot two indices from the Thomas models at fixed Alpha/Fe and age.
    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        index_name1- a string used for the plot axis labels
        index_name2- a string used for the plot axis labels
        alpha_fe- the value of alpha/fe we want. Must be [alpha/Fe] = -0.3, 0.0, 0.3, 0.5
        age- the value of age we want. Must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]

        alpha_grid- plot a grid by joining values of the same Z/H and age but different alpha/fe??
        age_grid- plot a grid by joining values of the same Z/H and alpha/fe but different age?

    """

    age=float(age)

    alpha_fe_ind=get_numpy_indices_for_params(alpha_fe=alpha_fe)
    age_ind=get_numpy_indices_for_params(age=age)

    

    
    index1=np.transpose(index1.reshape(4, 6, 20), (0, 2, 1))
    index2=np.transpose(index2.reshape(4, 6, 20), (0, 2, 1))



    ax.plot(index1[alpha_fe_ind, age_ind, :], index2[alpha_fe_ind, age_ind, :], label=r"$\alpha$/Fe={}, age={}".format(alpha_fe, age), linewidth=3.0)



    #add grey lines to make a grid- i.e join up all of the first points, some of the middle points and the last point of each line, to show how changing
    #age/alpha/Z moves you in the model space 
    if alpha_grid:
        for i in range(0, 6, 1):
            ax.plot(index1[:, age_ind, i], index2[:, age_ind, i], c="grey")
        ax.plot(index1[:, age_ind, -1], index2[:, age_ind, -1], c="grey")

        #ax.plot(index1[solar_alpha_fe_ind, :, solar_metallicity_ind], index2[solar_alpha_fe_ind, :, solar_metallicity_ind], c="b", linestyle="dotted", marker="s")

    if age_grid:
        for i in range(0, 6, 1):
            ax.plot(index1[alpha_fe_ind, :, i], index2[alpha_fe_ind, :, i], c="grey")
        ax.plot(index1[alpha_fe_ind, :, -1], index2[alpha_fe_ind, :, -1], c="grey")



#################################################################################################################################################
def _plot_at_fixed_Z_and_age(ax, index1, index2, Z=0.0, age=13.0, Z_grid=False, age_grid=False):

    """Plot two indices from the Thomas models at fixed Z/H and age.
    Inputs:
        ax- an axis object
        index1- a numpy array from the tmj_*.dat file. 
        index2- as above
        index_name1- a string used for the plot axis labels
        index_name2- a string used for the plot axis labels
        Z- the value of Z/H we want. Must be [Z/H] = [-2.25, -1.35, -0.33, 0.0, 0.35, 0.67]
        age- the value of age we want. Must be one of [0.1,0.2,0.4,0.6,0.8,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]

        Z_grid- plot a grid by joining values of the same alpha and age but different Z/H?
        age_grid- plot a grid by joining values of the same alpha and Z but different age?

    """
    age=float(age)

    Z_ind=get_numpy_indices_for_params(Z=Z)    
    age_ind=get_numpy_indices_for_params(age=age)
    
    index1=p.transpose(index1.reshape(4, 6, 20), (2, 1,0 ))
    index2=np.transpose(index2.reshape(4, 6, 20), (2, 1,0 ))


    
    ax.plot(index1[age_ind, Z_ind, :], index2[age_ind, Z_ind, :], label="Z/H={}, age={}".format(Z, age), linewidth=3.0)

    #add grey lines to make a grid- i.e join up all of the first points, some of the middle points and the last point of each line, to show how changing
    #Z/H moves you in the model space 
    if Z_grid:
        for i in range(0, 4, 1):
            ax.plot(index1[age_ind, :, i], index2[age_ind, :, i], c="grey")
        ax.plot(index1[age_ind, :, -1], index2[age_ind, :, -1], c="grey")
    if age_grid:
        for i in range(0, 4, 1):
            ax.plot(index1[:, Z_ind, i], index2[:, Z_ind, i], c="grey")
        ax.plot(index1[:, Z_ind, -1], index2[:, Z_ind, -1], c="grey")
#################################################################################################################################################  
    


def plot_index_vs_index(ax, index1, index1_name, index2, index2_name):

    

    #_plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.3, Z=-2.25, grid=False)
    #_plot_at_fixed_alpha_and_Z(ax, index1, index2, alpha_fe=0.3, Z=-1.35, grid=False)

    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=-0.3, age=13.0, alpha_grid=True)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.0, age=13.0, alpha_grid=True)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.3, age=13.0, alpha_grid=True)
    _plot_at_fixed_alpha_and_age(ax, index1, index2, alpha_fe=0.5, age=13.0, alpha_grid=True)


   

    #_plot_at_fixed_alpha(ax, index1, index2, 0.0)
   

    ax.set_xlabel("{}".format(index1_name))
    ax.set_ylabel("{}".format(index2_name))


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


    index1, index1_name=get_index(index1)
    index2, index2_name=get_index(index2)

    MgFe=np.sqrt(Mgb*(0.72*Fe5270+0.28*Fe5335))


    #Index 1 vs Index 2
    fig, ax=plt.subplots(ncols=1, nrows=1)
    plot_index_vs_index(ax, index1, index1_name, index2, index2_name)
    legend2=ax.legend(fancybox=True, fontsize=20, loc="best")



    

    plt.show()