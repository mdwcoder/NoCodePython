# MDW NoCodePython

¿Cansado de ver mil tutoriales y no aprender Python?  
¿Cansado de no tener una forma fácil de aprender?  

Con **NoCodePython**, eso se acaba. Este programa es fácil de usar y está diseñado para principiantes que quieren empezar a practicar sin tener que aprender lo básico primero. Con **NoCodePython**, puedes crear tus propias aplicaciones y scripts sin necesidad de saber programar en Python, solo necesitas usar lenguaje natural.

**NoCodePython** no está hecho para reemplazar el sistema tradicional de programación, pero sirve para transformar lenguaje natural en código, lo que permite experimentar y aprender la lógica más rápidamente.

## ¿Qué puedes hacer con **NoCodePython**?

Por el momento, el desarrollo está limitado al uso de Python base, sin librerías adicionales. Sin embargo, el desarrollo continúa y no se sabe hasta dónde llegará.

## ¿Cómo programar con **NoCodePython**?

**NoCodePython** tiene una sintaxis propia, pero trata de ser lo más natural posible.

### Sintaxis actual

**Nota:**  
Hay expresiones concretas para strings, como `imprime <texto a imprimir>`, que solo imprimirá el texto sin importar si lleva comillas; de hecho, no debe llevarlas. En cambio, en `concatena textoA con textoB en VariableGuardar` es necesario que si `textoA` o `textoB` no son variables, sean rodeados por comillas.

### Declaración de variables

Para guardar una variable, debes darle un contenido y un nombre.

Ejemplos:
```
guarda "contenido" en nombreVariable
guarda 10 en edad
```

### Usar variables

Ejemplo:
```
guarda 23 en numero1
sumar numero1 con 23 en resultado
```

### Imprimir en consola

Hay dos modos: variables y strings.

- `imprime variable`: imprimirá el contenido de la variable.
- `imprime`: imprimirá como string lo que introduzcas.

Ejemplos:
```
imprime Hola mundo
guarda "Hola Mundo" en cadena
imprime variable cadena
```

### Operaciones

Las operaciones se pueden hacer de la siguiente manera:

Ejemplo:
```
sumar 23 con 21 en resultado
```
(Guardará el resultado en la variable `resultado`).

Para el resto de operaciones es lo mismo con sus respectivos nombres:
- sumar
- restar
- multiplicar 
- dividir 
- elevar (darle un exponente a algo)
- radicar (hacer la raíz de algo)

### Trabajar con texto

Para concatenar texto usamos `concatenar`.

Ejemplo:
```
concatenar "contenido"1 con "contenido2" en resultado
```
(Guardará el resultado en la variable `resultado`).

### Condicionales

Los condicionales funcionan en una línea con comas. Veamos algunos ejemplos:

```
guarda 1 en numero
si 1 es igual a numero, entonces imprime Es igual, guarda igual en como_es
```

```
guarda 2 en numero
si 3 es menor que numero, entonces imprime Es menor, sino imprime Es mayor
```

### Bucles

Tenemos varios tipos de bucles, empezando por los más fáciles.

Repite algo `n` veces.

Ejemplo:
```
repite 32 veces imprime 23
```
(Imprimiría `23` 32 veces).

Otro ejemplo:
```
guarda 0 en contador
repite 10 veces suma 1 con contador en contador
imprime contador
```

Otro tipo es mientras pasa algo, haz algo.
```
guarda 0 en contador
mientras contador es menor que 10, haz imprime Es menor, suma 1 con contador en contador
```

Hay otro tipo que recorre las listas pero aún presenta errores, de momento tenemos esos dos.

### Los operadores

No hay mucho que explicar sobre los operadores, solo son estos:

- es igual a
- es diferente de 
- es mayor que 
- es menor que 
- es mayor o igual que 
- es menor o igual que
