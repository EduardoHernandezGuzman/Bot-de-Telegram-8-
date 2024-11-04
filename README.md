# Bot de Noticias de Telegram

Este proyecto consiste en un bot para Telegram desarrollado en Python utilizando la librería `TeleBot` y la API `NewsAPI` para obtener noticias en español.

## Descripción

Este bot proporciona noticias de diferentes categorías al usuario directamente en Telegram.  Las categorías disponibles incluyen noticias generales, de negocios, tecnología, deportes, entretenimiento, ciencia y salud. El bot utiliza la API de NewsAPI para obtener las noticias más recientes y las presenta al usuario en un formato legible dentro de Telegram.

## Usar el Bot

Puedes interactuar con el bot directamente en Telegram (PROXIMAMENTE)

## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Utiliza Git para clonar este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git 
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza `pip` para instalar las dependencias necesarias:

    ```bash
    cd tu_repositorio
    pip install -r requirements.txt
    ```

3. **Obtener Tokens**: Necesitas dos tokens para que el bot funcione:
    * **Token de Telegram Bot:** Crea un nuevo bot en Telegram utilizando el BotFather y obtén su token.
    * **API Key de NewsAPI:** Crea una cuenta en NewsAPI (newsapi.org) y obtén tu API key.

4. **Configurar las Variables de Entorno**:
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Abre el archivo `.env` en un editor de texto y agrega las siguientes líneas, reemplazando los valores con tus tokens:

    ```plaintext
    TELEGRAM_TOKEN=TU_TELEGRAM_TOKEN
    NEWS_API_KEY=TU_NEWS_API_KEY
    ```

5. **Asegurarse de que `.env` esté en `.gitignore`**:
    - Asegúrate de que el archivo `.env` esté incluido en `.gitignore` para evitar subir tus tokens al repositorio.  `.gitignore` debería contener la línea:

    ```plaintext
    .env
    ```

6. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida con botones para cada categoría de noticias.
- **Comando `/help`**: Muestra información de ayuda sobre los comandos disponibles.
- **Comando `/noticias_[categoria]`**:  Obtiene y muestra las últimas noticias para la categoría especificada (ej. `/noticias_business`, `/noticias_sports`).

## Categorías de Noticias

Las categorías disponibles son:

* `general`: Noticias generales.
* `business`: Noticias de negocios.
* `technology`: Noticias de tecnología.
* `sports`: Noticias deportivas.
* `entertainment`: Noticias de entretenimiento.
* `science`: Noticias de ciencia.
* `health`: Noticias de salud.

## Personalización

Puedes personalizar el bot modificando el archivo `main.py`.  Por ejemplo, puedes:

* Cambiar el número de noticias que se muestran.
* Añadir nuevas categorías de noticias.
* Modificar el formato de las noticias.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.
