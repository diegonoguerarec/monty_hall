[![en](https://img.shields.io/badge/lang-en-blue.svg)](readme.md)
[![es](https://img.shields.io/badge/lang-es-red.svg)](readme.es.md)

# Monty Hall

Imagina que estás en un programa de televisión para jugar un juego en el que puedes ganarte un auto nuevo. Hay tres puertas y solo detrás de una de ellas está el premio. El presentador te dice que elijas una de las puertas. Tú eliges una. A continuación, el presentador (que sabe en cuál puerta está el premio) abre una de las puertas vacías y te hace una pregunta:

**Participante, ¿quieres cambiar de puerta o mantener tu elección?**

Hasta este momento aún hay dos puertas cerradas. Detrás de una de ellas está el auto nuevo. El presentador abrió una de las puertas vacías para mostrarte que no hay nada detrás. Tienes dos opciones:

1) Mantener tu elección
2) Cambiar de puerta

Recuerda que el presentador sabe en cuál puerta está el premio, así que podría estar tratando de engañarte para que elijas la puerta incorrecta.

**¿Qué haces?**

Quizás pienses en no cambiar de puerta porque crees que el presentador quiere hacerte perder. También puede que pienses que no importa si cambias o no de puerta, puesto que solo una de ellas tiene el auto nuevo, y la probabilidad de acertar es siempre 1/3 o 33,33%.

---

## Cambio de elección

En realidad, lo mejor que puedes hacer es cambiar de puerta.

Cuando eliges una puerta al principio, las probabilidades de ganar son 1/3 o 33,33%, y las de perder son 2/3 o 66,66%, porque solo una de las tres puertas tiene el premio. Si decides no cambiar de puerta, es equivalente a mantener 1/3 de probabilidad de ganar.

Cuando el presentador abre una puerta, la puerta que elegiste sigue con 1/3 de probabilidad de ser la correcta. Lo que ocurre es que la otra puerta concentra los otros 2/3 de probabilidad restante.

Al cambiar de puerta, no apuestas a que elegiste bien al principio (lo cual era poco probable, 1/3), sino a que elegiste mal (lo más probable, 2/3). Como el presentador siempre elimina una opción incorrecta, esa probabilidad se transfiere a la otra puerta cerrada.

---

## Conclusión

Al cambiar de puerta, las probabilidades de ganar pasan a ser 2/3 o 66,66%, en vez del 1/3 o 33,33% del principio.

---

## Implementación

En el archivo monty_hall.py se encuentra la implementación de este juego.

Para ejecutar el programa en Windows:

``` python monty_hall.py <numero_de_iteraciones> ```

En Linux:

``` python3 monty_hall.py <numero_de_iteraciones> ```

Ejemplo:

``` python monty_hall.py 1000 ```


El programa simula el juego de Monty Hall e imprime la cantidad de veces que resultó en victoria, primero cuando no se hace el cambio de puerta y luego cuando sí se hace el cambio de puerta.

Cuando no se hace el cambio de puerta, el juego termina en victoria el 33,33% de las veces. Cuando se hace el cambio de puerta, el juego termina en victoria el 66,66% de las veces.