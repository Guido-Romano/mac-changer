# MAC Changer v1.0

Script en Python diseñado exclusivamente para sistemas **Linux** que permite cambiar automáticamente la dirección MAC de una interfaz de red. Utiliza colores para mejorar la presentación y la experiencia de uso.

## Características

- **Cambio Automático de Dirección MAC**: Genera y configura una nueva dirección MAC de manera eficiente.
- **Visualización Clara**: Utiliza colores para resaltar mensajes clave, mejorando la usabilidad.
- **Código claro y legible**: este codigo respeta las normas PEP8.
- **Exclusivo para Linux**: Diseñado específicamente para sistemas basados en Linux.

## Requisitos

- Python 3.x
- Dependencias adicionales:
  - `colorama` (instalable con pip)

### Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/Guido-Romano/mac-changer
    cd /RUTA-DEL-ARCHIVO/mac-changer
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install colorama
    ```

### Uso

1. Ejecuta el script desde la línea de comandos:

    ```bash
    sudo python3 mac_changer.py
    ```

2. El script cambiará automáticamente la dirección MAC de la interfaz predeterminada (`eth0` en este caso).

### Compatibilidad

Este script ha sido probado en las siguientes distribuciones Linux:
- Debian y derivadas (Ubuntu, Kali, Parrot).
- Arch Linux y derivadas.

## Funcionamiento

1. **Obtención de la MAC Actual**: El script identifica la dirección MAC asignada actualmente a la interfaz de red especificada.
2. **Generación de MAC Aleatoria**: Genera automáticamente una dirección MAC válida utilizando un algoritmo aleatorio.
3. **Aplicación de la Nueva MAC**: Configura la nueva dirección MAC, asegurando que la interfaz esté activa después del cambio.
4. **Resultados en Pantalla**: Muestra tanto la MAC anterior como la nueva, con mensajes destacados.

## Advertencias

- **Permisos**: Este script requiere permisos de superusuario (root) para modificar la dirección MAC de la interfaz de red.
- **Compatibilidad**: Asegúrate de usarlo exclusivamente en entornos Linux.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Agradecimientos

Gracias a la comunidad de Python y a las herramientas proporcionadas como `subprocess` y `colorama`, que hicieron posible este proyecto.
