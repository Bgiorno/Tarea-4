# Welcome to MkDocs

En la resolución de ecuaciones diferenciales ordinarias (ODEs), los métodos numéricos son esenciales para obtener aproximaciones cuando no se dispone de soluciones analíticas. A continuación, se presenta una introducción a tres métodos numéricos comunes: el método de Euler, el método de Runge-Kutta de orden 2 (RK2) y el método de Runge-Kutta de orden 4 (RK4).

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

    $$ X_i $$

## Método de Euler

El método de Euler es uno de los métodos numéricos más simples para resolver ODEs. Es un método de primer orden, lo que significa que el error por paso es proporcional al cuadrado del tamaño del paso. La fórmula básica para el método de Euler es:

$$ x_i = x_{i-1} + h f(x_{i-1}) $$

donde:
- `y_n` - Es la aproximación de la solución en el paso \( n \).
- \( h \) es el tamaño del paso.
- \( f(t, y) \) es la función que define la ODE \( \frac{dy}{dt} = f(t, y) \).

## Método de Runge-Kutta de Orden 2 (RK2)

El método de Runge-Kutta de segundo orden, también conocido como método del punto medio o método de Heun, mejora la precisión del método de Euler. Una forma común del método RK2 es:

$$ k_1 = h f(t_n, y_n) $$
$$ k_2 = h f(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}) $$
$$ y_{n+1} = y_n + k_2 $$

## Método de Runge-Kutta de Orden 4 (RK4)

El método de Runge-Kutta de cuarto orden es uno de los métodos más utilizados debido a su precisión y estabilidad. Este método calcula cuatro incrementos (\( k_1, k_2, k_3, k_4 \)) para obtener una mejor aproximación de la solución. Las fórmulas son:

$$ k_1 = h f(t_n, y_n) $$
$$ k_2 = h f(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}) $$
$$ k_3 = h f(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}) $$
$$ k_4 = h f(t_n + h, y_n + k_3) $$

La actualización de la solución es entonces:

$$ y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4) $$

## MkDocs Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.
- `$x_i$` - Sub indice prueba.


## Project layout


