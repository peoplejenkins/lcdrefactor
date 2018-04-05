# LCD Printer

Objetivo: Crear un programa que imprime números en estilo de una pantalla LCD

Entrada: La entrada contiene varias líneas. Cada línea contiene 2 números separados por coma. El primer número representa el tamaño de la impresión (entre 1 y 10, esta variable se llama “size”). El segundo número es el número a mostrar en la pantalla. Para terminar, se debe digitar 0,0. Esto terminará la aplicación.

Salida: Imprimir los números especificados usando el caracter “-“ para los caracteres horizontales, y “|” para los verticales. Cada dígito debe ocupar exactamente size+2 columnas y 2*size + 3 filas.

Entre cada impresión debe haber una línea blanca.

## Uso

### Docker way

```bash
docker pull xxdrackleroxx/psl-printer:1.0
docker run --rm -it xxdrackleroxx/psl-printer:1.0
```

### Regular usage
```
$ git clone https://github.com/AmauryOrtega/lcdrefactor.git
$ python main.py
    LCD_Printer
    @author: Amaury Ortega <amauryocortega@gmail.com>
    
    Program to print numbers in LCD style.
    
    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    
Input: 1,1234
     -   -     
  |   |   | | |
     -   -   - 
  | |     |   |
     -   -     
Input: 4,965
 ----   ----   ---- 
|    | |      |     
|    | |      |     
|    | |      |     
|    | |      |     
 ----   ----   ---- 
     | |    |      |
     | |    |      |
     | |    |      |
     | |    |      |
 ----   ----   ---- 
Input: 0,0
Thanks for using this software

```

### Error message

```
$ python main.py                                                                                               (04-05 18:13)
    LCD_Printer
    @author: Amaury Ortega <amauryocortega@gmail.com>
    
    Program to print numbers in LCD style.
    
    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    
Input: 8,5 
 -------- 
|         
|         
|         
|         
|         
|         
|         
|         
 -------- 
         |
         |
         |
         |
         |
         |
         |
         |
 -------- 
Input: a,2123
Wrong input 'a,2123' please, verify the format.

    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    
Input: 1,2123
 -       -   - 
  |   |   |   |
 -       -   - 
|     | |     |
 -       -   - 
Input: 0,0
Thanks for using this software

```
