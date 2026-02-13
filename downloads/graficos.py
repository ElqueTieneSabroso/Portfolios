# Importar las librerías:
import numpy as np
import matplotlib.pyplot as plt

# Definir la función a graficar:
def f(x, y):
    return 0.02*(x**2) + (8+0.6*y)/(y+1)

# Definir la función de graficación:
def graficacion(f, x_min, x_max, y_min, y_max, h=1, modo='traza'):

    if modo == 'puntos':
        # Calcular las particiones:
        N_x = int((x_max - x_min) / h + 1)
        N_y = int((y_max - y_min) / h + 1)

        x = np.linspace(x_min, x_max, N_x)
        y = np.linspace(y_min, y_max, N_y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for x_i in x:
            for y_i in y:
                z = f(x_i, y_i)
                ax.scatter3D(x_i, y_i, z, c='g')

        ax.set_xlabel('Eje $x$')
        ax.set_ylabel('Eje $y$')
        ax.set_zlabel('Eje $z$')

    elif modo == 'traza':
        fija = input('¿Qué variable deseas mantener fija? (x/y): ').lower()
        c = float(input('¿En qué valor se mantendrá constante?: '))

        fig = plt.figure()
        ax = fig.add_subplot(111)

        if fija == 'y':
            x = np.linspace(x_min, x_max, 200)
            y = np.full_like(x, c)
            z = f(x, y)
            ax.plot(x, z)
            ax.set_xlabel('Eje $x$')
            ax.set_ylabel('Eje $z$')

        else:
            y = np.linspace(y_min, y_max, 200)
            x = np.full_like(y, c)
            z = f(x, y)
            ax.plot(y, z)
            ax.set_xlabel('Eje $y$')
            ax.set_ylabel('Eje $z$')

    elif modo == 'trazas2D':
        fija = input('¿Qué variable deseas fijar? (x/y): ').lower()
        c_min = float(input('Valor mínimo constante: '))
        c_max = float(input('Valor máximo constante: '))
        h = float(input('Espaciado entre trazas: '))

        N_c = int((c_max - c_min) / h + 1)
        c = np.linspace(c_min, c_max, N_c)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        if fija == 'y':
            x = np.linspace(x_min, x_max, 200)
            for c_i in c:
                y = np.full_like(x, c_i)
                z = f(x, y)
                ax.plot(x, z, label=f'y = {c_i:g}')

            ax.set_xlabel('Eje $x$')
            ax.set_ylabel('Eje $z$')
            ax.legend()

        else:
            y = np.linspace(y_min, y_max, 200)
            for c_i in c:
                x = np.full_like(y, c_i)
                z = f(x, y)
                ax.plot(y, z, label=f'x = {c_i:g}')

            ax.set_xlabel('Eje $y$')
            ax.set_ylabel('Eje $z$')
            ax.legend()

    elif modo == 'trazas3D':
        h = float(input('Introduce el espaciado entre trazas: '))

        N_x = int((x_max - x_min) / h + 1)
        N_y = int((y_max - y_min) / h + 1)

        c_x = np.linspace(x_min, x_max, N_x)
        c_y = np.linspace(y_min, y_max, N_y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(x_min, x_max, 200)
        y = np.linspace(y_min, y_max, 200)

        for c in c_y:
            y_c = np.full_like(x, c)
            z = f(x, y_c)
            ax.plot3D(x, y_c, z, c='b')

        for c in c_x:
            x_c = np.full_like(y, c)
            z = f(x_c, y)
            ax.plot3D(x_c, y, z, c='g')

        ax.set_xlabel('Eje $x$')
        ax.set_ylabel('Eje $y$')
        ax.set_zlabel('Eje $z$')

    elif modo == 'curvas':
        x = np.linspace(x_min, x_max, 200)
        y = np.linspace(y_min, y_max, 200)

        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        C = int(input('¿Cuántas curvas de nivel deseas?: '))

        contour = ax.contour(X, Y, Z, levels=C)
        ax.clabel(contour, inline=True)

        ax.set_xlabel('Eje $x$')
        ax.set_ylabel('Eje $y$')

    else:
        print("Modo no válido.")

    plt.show()


# Llamada de ejemplo:
graficacion(f, 0, 40, 0, 5, 1, 'trazas3D')

