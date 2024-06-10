import numpy as np

def hessian_matrix(f,x,deltaX):
    fx = f(x)
    N = len(x)
    H = []
    for i in range(N):
        hi = []
        for j in range(N):
            print(i,j,end=' ')
            if i == j:
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i] + deltaX
                xn[i] = xn[i] - deltaX
                hi.append( ( f(xp)- 2*fx + f(xn))/ (deltaX**2) )
            else:
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()
                xpp[i] = xpp[i] + deltaX
                xpp[j] = xpp[j] + deltaX

                xpn[i] = xpn[i] + deltaX
                xpn[j] = xpn[j] - deltaX

                xnp[i] = xnp[i] - deltaX
                xnp[j] = xnp[j] + deltaX

                xnn[i] = xnn[i] - deltaX
                xnn[j] = xnn[j] - deltaX

                hi.append( (f(xpp)-f(xpn)-f(xnp)+f(xnn)) / (4*deltaX**2))
        H.append(hi)
        print()
    return H

