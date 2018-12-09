import logging
import matplotlib
# Force matplotlib to not use any Xwindows backend.
# this is important for running on servers without a GUI!
matplotlib.use('Agg')
import matplotlib.pylab as pl
#from mpl_toolkits.mplot3d import Axes3D
#from mpi4py import MPI
from sdfpy import load_sdf
import sys
from thingking import loadtxt

logging.basicConfig()

#comm = MPI.COMM_WORLD
#rank = comm.Get_rank()

#if len(sys.argv) >= 2:
 # file_num = rank + int(sys.argv[-1])
#elif rank > 100:
#  file_num = 100
#else:
#  sys.exit()
 # file_num = rank

# Change me to a file system path if you have the data locally for
# much performance gains
#prefix = "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/"
prefix = "data/"



filenames = [
    "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_1.0000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.9000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.8000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.7000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.6000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.5000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.4000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.3000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.2000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1200"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1100"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.1000"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0900"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0800"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0700"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0600"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0500"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0400"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0300"
    , "http://darksky.slac.stanford.edu/scivis2015/data/ds14_scivis_0128/ds14_scivis_0128_e4_dt04_0.0200"

    ]
count=14;

for file in filenames:
    print("pleaseee")
    print(file)
    # Load N-body particles from a = 1.0 dataset. Particles have positions with
    # units of proper kpc, and velocities with units of km/s.
    particles = load_sdf(filename)

# Load the a=1 Rockstar hlist file. The header of the file lists the useful
# units/information.
    scale, id, desc_scale, desc_id, num_prog, pid, upid, desc_pid, phantom, \
        sam_mvir, mvir, rvir, rs, vrms, mmp, scale_of_last_MM, vmax, x, y, z, \
        vx, vy, vz, Jx, Jy, Jz, Spin, Breadth_first_ID, Depth_first_ID, \
        Tree_root_ID, Orig_halo_ID, Snap_num, Next_coprogenitor_depthfirst_ID, \
        Last_progenitor_depthfirst_ID, Rs_Klypin, M_all, M200b, M200c, M500c, \
        M2500c, Xoff, Voff, Spin_Bullock, b_to_a, c_to_a, A_x, A_y, A_z, \
        b_to_a_500c, c_to_a_500c, A_x_500c, A_y_500c, A_z_500c, T_over_U, \
        M_pe_Behroozi, M_pe_Diemer, Macc, Mpeak, Vacc, Vpeak, Halfmass_Scale, \
        Acc_Rate_Inst, Acc_Rate_100Myr, Acc_Rate_Tdyn = \
        loadtxt(prefix+"rockstar/hlists/hlist_0.{:0>2d}000.list".format(count-2), unpack=True)

    # Now we want to convert the proper kpc of the particle position to comoving
    # Mpc/h, a common unit used in computational cosmology in general, but
    # specifically is used as the output unit in the merger tree halo list loaded
    # in above. First we get the Hubble parameter, here stored as 'h_100' in the
    # SDF parameters. Then we load the simulation width, L0, which is also in
    # proper kpc. Finally we load the scale factor, a, which for this particular
    # snapshot is equal to 1 since we are loading the final snapshot from the
    # simulation.
    h_100 = particles.parameters['h_100']
    width = particles.parameters['L0']
    cosmo_a = particles.parameters['a']
    kpc_to_Mpc = 1. / 1000
    sl = slice(0, None)

    # Define a simple function to convert proper to comoving Mpc/h.
    convert_to_cMpc = lambda proper: (proper + width/2.) * h_100 * kpc_to_Mpc / cosmo_a

    # Plot all the particles, adding a bit of alpha so that we see the density of
    # points.

    fig = pl.figure(figsize=[20,20])
    ax = fig.add_subplot(111, projection="3d")
    # set a dark background cause it looks cooler
    ax.patch.set_facecolor('0.2')

    # shift it to start at 0
    particles_x = convert_to_cMpc(particles['x'][sl])
    particles_y = convert_to_cMpc(particles['y'][sl])
    particles_z = convert_to_cMpc(particles['z'][sl])
    particles_x = particles_x - particles_x.min()
    particles_y = particles_y - particles_y.min()
    particles_z = particles_z - particles_z.min()
    ax.scatter(particles_x, particles_y, particles_z, color='white', s=0.05, alpha=0.05)

    # Plot all the halos in red.
    ax.scatter(x, y, z, color='#FFFF00', alpha=0.1)

    fig_size = fig.get_size_inches()
    w, h = fig_size[0], fig_size[1]

    # Turn off all the axis and labels
    ax.set_frame_on(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.axis('off')

    if rank >= 100:
      ax.azim = (ax.azim + rank - 100) % 360
    if rank >= 460:
      new_range = (1484 - rank) * (ax.get_xlim() / 1024.0)
      ax.set_xlim(new_range)
      ax.set_ylim(new_range)
      ax.set_zlim(new_range)

    print "Finished at {:d}, saving figure".format(rank)
    pl.savefig("output/3d_scatter{:0>4d}.png".format(rank), bbox_inches="tight", pad_inches=0, facecolor="0.2")

    # Plot all the halos in magenta
    ax.scatter(x, y, z, color='m', alpha=0.1)
    pl.savefig("output/3d_scatter_with_halos{:0>4d}.png".format(rank), bbox_inches="tight", pad_inches=0, facecolor="0.2")
    print "Process {:d} completed".format(file_num)
