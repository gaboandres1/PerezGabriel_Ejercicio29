import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

dTc = 0.00226
Times = np.array( [0.0, 0.11, 0.22, 0.33, 0.44, 0.56, 0.67, 0.78, 0.89] )

data = np.loadtxt('data.dat')
x = np.linspace(-1,1,data.shape[1])
t = np.linspace(0,1,data.shape[0])

X,T = np.meshgrid(x,t)

fig,ax= plt.subplots(1,3,figsize=(16,5))

#ax = fig.gca(projection='3d')
im = ax[0].imshow(data, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-1, 1, 0, 1],
               vmax=abs(data).max(), vmin=-abs(data).max())
#surf = ax.plot_surface(X,T,data)
ax[0].set(xlabel='Posicion', ylabel='Tiempo',title='Nx=30, Ntc' )

for i in Times/dTc:
    ax[1].plot(x, data[int(i),:], label = 't ='+ str(int(i)*dTc)[:4],c='k')
ax[1].set( xlabel = 'Posicion',ylabel='$\Psi$')
ax[1].legend(loc='upper right')
ax[2].plot(t, data[:,15],c='k')
ax[2].set( xlabel='Tiempo', ylabel='$\Psi(x=0)$')
fig.savefig('evolve_A.png')

data1 = np.loadtxt('data1.dat')
x = np.linspace(-1,1,data1.shape[1])
t = np.linspace(0,1,data1.shape[0])

X,T = np.meshgrid(x,t)

fig2,ax= plt.subplots(1,3,figsize=(16,5))

#ax = fig.gca(projection='3d')
im = ax[0].imshow(data1, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-1, 1, 0, 1],
               vmax=abs(data1).max(), vmin=-abs(data1).max())
#surf = ax.plot_surface(X,T,data)
ax[0].set(xlabel='Posicion', ylabel='Tiempo',title='Nx=31, Ntc' )

for i in Times/dTc:
    ax[1].plot(x, data1[int(i),:], label = 't ='+ str(int(i)*dTc)[:4],c='k')
ax[1].set( xlabel = 'Posicion',ylabel='$\Psi$')
ax[1].legend(loc='upper right')
ax[2].plot(t, data1[:,15],c='k')
ax[2].set( xlabel='Tiempo', ylabel='$\Psi(x=0)$')
fig2.savefig('evolve_B.png')

data2 = np.loadtxt('data2.dat')
x = np.linspace(-1,1,data2.shape[1])
t = np.linspace(0,1,data2.shape[0])

X,T = np.meshgrid(x,t)

fig3,ax= plt.subplots(1,3,figsize=(16,5))

#ax = fig.gca(projection='3d')
im = ax[0].imshow(data2, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-1, 1, 0, 1],
               vmax=abs(data2).max(), vmin=-abs(data2).max())
#surf = ax.plot_surface(X,T,data)
ax[0].set(xlabel='Posicion', ylabel='Tiempo',title='Nx=29, Ntc' )

for i in Times/dTc:
    ax[1].plot(x, data2[int(i),:], label = 't ='+ str(int(i)*dTc)[:4],c='k')
ax[1].set( xlabel = 'Posicion',ylabel='$\Psi$')
ax[1].legend(loc='upper right')
ax[2].plot(t, data2[:,15],c='k')
ax[2].set( xlabel='Tiempo', ylabel='$\Psi(x=0)$')
fig3.savefig('evolve_C.png')

data3 = np.loadtxt('data3.dat')
x = np.linspace(-1,1,data3.shape[1])
t = np.linspace(0,1,data3.shape[0])

X,T = np.meshgrid(x,t)

fig3,ax= plt.subplots(1,3,figsize=(16,5))

#ax = fig.gca(projection='3d')
im = ax[0].imshow(data3, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-1, 1, 0, 1],
               vmax=abs(data3).max(), vmin=-abs(data3).max())
#surf = ax.plot_surface(X,T,data)
ax[0].set(xlabel='Posicion', ylabel='Tiempo',title='Nx=29, Ntc-10' )

for i in Times/dTc:
    ax[1].plot(x, data3[int(i),:], label = 't ='+ str(int(i)*dTc)[:4],c='k')
ax[1].set( xlabel = 'Posicion',ylabel='$\Psi$')
ax[1].legend(loc='upper right')
ax[2].plot(t, data3[:,15],c='k')
ax[2].set( xlabel='Tiempo', ylabel='$\Psi(x=0)$')
fig3.savefig('evolve_D.png')
