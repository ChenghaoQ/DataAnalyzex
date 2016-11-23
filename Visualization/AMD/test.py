from pylab import *

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]

explode=(0, 0.05, 0, 0)
p = pie(fracs, explode=explode, shadow=True)
title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

for p1, l1 in zip(p[0], labels):
    r = p1.r
    dr = r*0.1
    t1, t2 = p1.theta1, p1.theta2
    theta = (t1+t2)/2.

    xc, yc = r/2.*cos(theta/180.*pi), r/2.*sin(theta/180.*pi)
    x1, y1 = (r+dr)*cos(theta/180.*pi), (r+dr)*sin(theta/180.*pi)
    if x1 > 0 :
        x1 = r+2*dr
        ha, va = "left", "center"
        tt = -180
        cstyle="angle,angleA=0,angleB=%f"%(theta,)
    else:
        x1 = -(r+2*dr)
        ha, va = "right", "center"
        tt = 0
        cstyle="angle,angleA=0,angleB=%f"%(theta,)

    annotate(l1,
             (xc, yc), xycoords="data",
             xytext=(x1, y1), textcoords="data", ha=ha, va=va,
             arrowprops=dict(arrowstyle="-",
                             connectionstyle=cstyle,
                             patchB=p1))

show()
