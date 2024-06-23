import numpy as np
import matplotlib.pyplot as plt

def fun(x_i, t_i):
    return -np.power(x_i, 3) + np.sin(t_i)


def eu(f, x_0, t_0, N, tf):
    """
    Esta funcion implementa el metodo de euler para aproximar una ODE

    Args:
        f (funtion): Funcion a la cual aplicar el metodo de euler
        x_0 (float): Valor de frontera dado, ejemplo x(0)=0
        t_0 (float): Valor inicial desde el cual se va a evaluar la funcion a encontrar
        N (int): Numero de pasos a iterar con cierto tamaño.
        tf (float): Valor final hasta el cual se va a evaluar la funcion a encontrar


    Returns:
        string: Devuele 2 hileras, una con los tiempos en los cuales se evaluo la funcion y la otra hilera es la funcion evaluada en esos puntos, es decir la ODE a encontrar.

    Example:

        >>> eu(fun,0,0,20,10):
        >>> ver seccion ejemplo para la ver la grafica de la funcion


    """


    h=(tf-t_0)/N
    ts=np.linspace(t_0, tf, N)
    xs=np.zeros(len(ts))
    xs[0] = x_0
    for i in range(0,len(ts)-1):
        xs[i+1] = xs[i] + h * f(xs[i], ts[i])
    return ts, xs

def rk2(f,t_0,x_0,N,tf):
    """
    Esta funcion implementa el metodo de RK de segundo orden  para aproximar una ODE

    Args:
        f (funtion): Funcion a la cual aplicar el metodo de RK2
        x_0 (float): Valor de frontera dado, ejemplo x(0)=0
        t_0 (float): Valor inicial desde el cual se va a evaluar la funcion a encontrar
        N (int): Numero de pasos a iterar con cierto tamaño.
        tf (float): Valor final hasta el cual se va a evaluar la funcion a encontrar


    Returns:
        string: Devuele 2 hileras, una con los tiempos en los cuales se evaluo la funcion y la otra hilera es la funcion evaluada en esos puntos, es decir la ODE a encontrar.

    Example:

        >>> rk2(fun,0,0,20,10):
        >>> ver seccion ejemplo para la ver la grafica de la funcion


    """

    h = (tf-t_0)/N
    ts= np.linspace(t_0,tf,N)
    xs = np.zeros(len(ts))
    xs[0] = x_0
    for i in range(len(ts)-1):
        k1=h*f(xs[i],ts[i])
        k2=h*f(xs[i] + k1/2, ts[i] + h/2)
        xs[i+1] = xs[i] + k2
    return ts, xs

def rk4(f,x_0,t_0,N,tf):
    """
    Esta funcion implementa el metodo de RK de cuarto orden para aproximar una ODE

    Args:
        f (funtion): Funcion a la cual aplicar el metodo de RK4
        x_0 (float): Valor de frontera dado, ejemplo x(0)=0
        t_0 (float): Valor inicial desde el cual se va a evaluar la funcion a encontrar
        N (int): Numero de pasos a iterar con cierto tamaño.
        tf (float): Valor final hasta el cual se va a evaluar la funcion a encontrar


    Returns:
        string: Devuele 2 hileras, una con los tiempos en los cuales se evaluo la funcion y la otra hilera es la funcion evaluada en esos puntos, es decir la ODE a encontrar.

    Example:

        >>> rk4(fun,0,0,20,10):
        >>> ver seccion ejemplo para la ver la grafica de la funcion


    """

    h=(tf-t_0)/N
    ts=np.linspace(t_0, tf, N)
    xs=np.zeros(len(ts))
    xs[0]=x_0
    for i in range(len(ts)-1):
        k1=h*f(xs[i],ts[i])
        k2=h*f(xs[i] + k1/2, ts[i] + h/2)
        k3=h*f(xs[i] + k2/2, ts[i] + h/2)
        k4=h*f(xs[i]+k3,ts[i]+h)
        xs[i+1] = xs[i] + (1/6)*(k1+2*k2+2*k3+k4)
    return ts, xs






