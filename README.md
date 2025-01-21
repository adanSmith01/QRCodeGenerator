# Generador de códigos QR

## Resumen

Es un generador de codigos QR que funciona por **consola**.
Podrá guardar links, codigos de seguridad, contraseñas de red
o cualquier tipo de información textual de su preferencia.

## Instalación previa
```
pip install -r requirements.txt
```

## ¿Cómo funciona?

1. Primero, debe ejecutar el archivo `main.py` desde el directorio del proyecto

```
python main.py
```
&nbsp;

2. Debe ingresar la información textual que desee que se almacene. Por ejemplo: https://www.google.com/


&nbsp;

3. Luego, ingresar el color de relleno que desee que tenga el QR en
hexadecimal. Por ejemplo: 000000 (negro) o FF0000 (rojo)

> [!NOTE]
> El color de relleno es el color que van a tener todos los módulos (o cuadraditos)
del código generado. si pulsa ENTER tendr, por defecto, el color negro 

&nbsp;

4. Ingresar el color de fondo del codigo QR en hexadecimal. Por ejemplo:
FFFFFF (blanco)

> [!NOTE]
> El color de fondo debe tener el contraste necesario respecto al color de relleno. Sino, no podrá ser escaneado facilmente.
Por defecto, si pulsa ENTER se le asignará el color blanco.

5. Ingresar un la ruta absoluta del logo de preferencia para su codigo QR (esto es opcional). Puede
utilizar cualquiera de los logos que aparecen en el directorio `test-logo`


Siguiendo los pasos, puede tener un codigo QR como el siguiente:

![Codigo QR con el logo de Google y contiene un enlace a https://www.google.com/](google.png)


> [!IMPORTANT]
> Los codigos QR generados se guardarán en un directorio llamado `QR_Codes`  que, en el caso de que no exista, también 
se va a crear en el directorio personal.
> [!IMPORTANT]
> Si crea una imagen de codigo QR con el mismo nombre de una existente, será reemplazada por la nueva imagen creada.

