# lulo_bank
Prueba técnica Lulo Bank - Data engineers

En este repositorio se encuentran los resultados de la prueba técnica, los pasos para ejecutar esto son los siguientes:
* clone este repositorio ```git clone git@github.com:AletzB/lulo_bank.git``` en su carpeta local o descargue el ZIP 
* Diríjase a la carpeta que contiene un archivo llamado **Dockerfile**
* Abra una terminal nueva y digite lo siguiente ```docker-compose up --build``` automáticamente docker gestionara todos los paquetes y archivos, luego de unos segundos generara una dirección url la cual será  http://0.0.0.0:5000/ ábrala en su localhost y verá un **hola mundo** en la página de inicio para ver los registros de la base de datos que se creó agréguele a la anterior dirección web ```/items/2``` el número 2 representa cuantos elementes quiere visualizar un ejemplo para 4 elementos sería el siguiente  http://0.0.0.0:5000/items/4, tenga en cuenta que para que funcione el comando anterior debe de tener instalado [docker](https://docs.docker.com/engine/install/ubuntu/) y [docker compose](https://docs.docker.com/compose/install/), a si como también se recomienda seguir el instructivo de pos-instalación suministrado en la [documentación oficial](https://docs.docker.com/engine/install/linux-postinstall/).
* Lo que realiza el contenedor es: 
1. Realiza pruebas unitarias a la API de tvmaze. 
2. Realiza las peticiones para descargar la información del mes de diciembre de 2020. 
3. Crea la tabla de SQLite y la llena con la información del parquet previamente creado. 
4. Inicia la instancia web para ver la información almacenada en la db

* Para ejecutar el notebook abra una nueva terminal Linux en la carpeta base del proyecto y ejecute el comando ```jupyter-lab``` o ```jupyter notebook``` el que sea de su agrado y posteriormente abra el archivo llamado *analysis.ipynb* en el se realiza la limpieza, análisis y profiling de la data para finalmente guardar la data resultante en un archivo llamado *data.parquet* tenga en cuenta que para abrir este archivo tiene que tener instalado [Anaconda](https://www.anaconda.com/) o algún editor notebook.
* En el repositorio se adjuntaron los archivos HTML del profiling y análisis realizado que es lo mismo que está en el archivo *analysis.ipynb* si no puedes abrir dicho archivo tenga la libertad de revisar los archivos HTML.
* Dentro de app encontrará las siguientes carpetas:
1. *json_response* donde podrá visualizar los archivos JSON de la respuesta de la API
2. *db* donde se encuentra la base de datos creada
3. *test* donde está el archivo de pruebas unitarias
4. *images* donde adjunte algunas imágenes de los resultados obtenidos y de la ejecución del docker
