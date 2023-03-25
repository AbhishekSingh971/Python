import matplotlib.pyplot as py
import numpy as np

font1 = {'family':'serif','color':'blue','size':20}

x=np.array([2,6,3,1])
y=np.array([3,8,1,10])
py.subplot(2,2,1)
py.title("Demonstration 1",font1)
py.xlabel("x - axis")
py.ylabel("y - axis")
# py.plot(x,y,marker='o',c="red",ms=20,mec='y',mfc="b",ls="dotted",lw='10') # ms=marker size  mec = marker edge color   mfc = marker face color
# py.plot(x,y,'o:r')
py.bar(x,y,width=0.7)
py.scatter(x,y)
py.grid(axis='y',c='green',ls='--',lw=1)


y=np.array([3,8,1,10])
py.subplot(2,2,3)
py.title("Demonstration 3",font1)
py.xlabel("x - axis")
py.ylabel("y - axis")
# py.plot(x,y,marker='o',c="red",ms=20,mec='y',mfc="b",ls="dotted",lw='10') # ms=marker size  mec = marker edge color   mfc = marker face color
# py.plot(x,y,'o:r')
py.pie(y)
py.scatter(x,y)
py.grid(axis='y',c='green',ls='--',lw=1)


x=np.array([3,8,1,10])
y=np.array([2,6,3,1])
py.subplot(2,2,2)
py.title("Demonstration 2",font1)
py.xlabel("x - axis")
py.ylabel("y - axis")
# py.plot(x,y,marker='o',c="red",ms=20,mec='y',mfc="b",ls="dotted",lw='10') # ms=marker size  mec = marker edge color   mfc = marker face color
# py.plot(x,y,'o:r')
py.barh(x,y)
py.scatter(x,y,s=30,alpha=0.3)
py.grid(axis='y',c='green',ls='--',lw=1)



py.suptitle("Demo")
py.colorbar()
py.show()

