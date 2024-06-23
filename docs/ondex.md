## Métodos de aproximacion
 En la resolución de ecuaciones diferenciales ordinarias (ODEs), los métodos numéricos son esenciales para obtener aproximaciones cuando no se dispone de soluciones analíticas.
     A continuación, se presenta una introducción a tres métodos numéricos comunes: el método de Euler, el método de Runge-Kutta de orden 2 (RK2)
         y el método de Runge-Kutta de orden 4 (RK4).

## Método de Euler

 El método de Euler es uno de los métodos numéricos más simples para resolver ODEs. Es un método de primer orden,
     con error proporcional al cuadrado del tamaño del paso. La fórmula básica para el método de Euler es:

 $$ x_i  = x_{i-1} + hf(x_i) $$

 Donde:

 - `x_i` - Es el valor de la funcion a aproximar evaluada en un tiempo t.
 - `h` - Es el tamaño del paso 
 - `f(x_i)` - Es la funcion a la cual se le aplica el metodo.

## Método de Runge-Kutta de orden 2

 El método RK2 utiliza un punto medio para evaluar el método de Euler, logrando una mejor aproximacion con un error del orden del cubo del tamaño del paso
    este método se compone ahora de terminos k que se utlizan de manera recursiva, tal que el metodo se ve de la siguiente manera.
 $$ x_{i+1} = x_i + k_2 $$

 Donde:

 $$ k_1 = hf(x_i) $$
 $$ k_2 = hf(x_i + \frac{k_1}{2}, t + \frac{h}{2}) $$
 
## Método de Runge-Kutta de orden 4 

 El método RK4 es una extension y mejora del metodo RK2, ahora con error de aproximacion del tamaño del paso elevado a la 5
    y con nuevos terminos k, obteniendose la siguiente ecuacion. 
 $$ x_{i+1} = x_{i} + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k4) $$

 Donde:

 $$ k_1 = hf(x_i) $$
 $$ k_2 = hf(x_i + \frac{k_1}{2}, t + \frac{h}{2}) $$
 $$ k_3 = hf(x_i + \frac{k_2}{2}, t + \frac{h}{2}) $$
 $$ k_4 = hf(x_i + k_3, t + \frac{h}{2}) $$



