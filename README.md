- [English](/README.md/#qr-code-generator)
- [Spanish](/README.md/#geenerador-de-codigos-qr)

# QR Code Generator

## Summary
This is a **console-based** QR code generator.
You can save links, security codes or any type of textual information of your choice.

## Prerequisites
- Python 3+ installed
- Install dependences:
```
pip install -r requirements.txt
```

## How does it work?
1. First, run the main.py file from the project directory:
```
python main.py
```
&nbsp;

2. Enter the text information you want to store. For example: https://www.google.com/

   &nbsp;

3. Next, enter the fill color for the QR code in hexadecimal.

> [!NOTE]
> The fill color is the color of all the modules (or small squares) in the generated code.
If you press ENTER, the default color will be **black**.

&nbsp;

4. Enter the background color of the QR code in hexadecimal.

> [!NOTE]
> The background color must have sufficient contrast with the fill color; otherwise, it won't be easily scannable.
By default, if you press ENTER, the background color will be **white**.

&nbsp;

5. Enter the absolute path of a logo to include in your QR code (this is optional).
You can use any of the logos found in the `test-logo` directory.

&nbsp;

Following these steps, you can generate a QR code like the following:

![Codigo QR con el logo de Google y contiene un enlace a https://www.google.com/](google.png)

> [!IMPORTANT]
> The generated QR codes will be saved in a directory named `QR_Codes`. If it does not exist, it will be created in your personal directory.
>
> If you create a QR code image with the same name as an existing one, it will be replaced by the newly created image.

---

# Generador de códigos QR

## Resumen
Es un generador de codigos QR que funciona por **consola**.
Podrá guardar links, codigos de seguridad o cualquier tipo de información textual de su preferencia.

## Requerimientos previos
- Tener Python 3+ instalado
- Instalación de dependencias:
```
pip install -r requirements.txt
```

&nbsp;

## ¿Cómo funciona?
1. Primero, debe ejecutar el archivo `main.py` desde el directorio del proyecto
```
python main.py
```

&nbsp;

2. Debe ingresar la información textual que desee que se almacene. Por ejemplo: https://www.google.com/ &nbsp;
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

&nbsp;

5. Ingresar un la ruta absoluta del logo de preferencia para su codigo QR (esto es opcional). Puede
utilizar cualquiera de los logos que aparecen en el directorio `test-logo`

&nbsp;

Siguiendo los pasos, puede tener un codigo QR como el siguiente:

![Codigo QR con el logo de Google y contiene un enlace a https://www.google.com/](google.png)


> [!IMPORTANT]
> Los codigos QR generados se guardarán en un directorio llamado `QR_Codes`  que, en el caso de que no exista, también 
se va a crear en el directorio personal.
>
> Si crea una imagen de codigo QR con el mismo nombre de una existente, será reemplazada por la nueva imagen creada.

