# lulo_bank
Prueba técnica Lulo Bank - Data engineers

En este repositorio se encuentran los resultados de la prueba técnica, los pasos para ejecutar esto son los siguientes:
* clone este repositorio ```git clone git@github.com:AletzB/lulo_bank.git``` en su carpeta local o descargue el ZIP 
* Diríjase a la carpeta que contiene un archivo llamado **Dockerfile**
* Abra una terminal nueva y digite lo siguiente ```docker-compose up --build``` automáticamente docker gestionara todos los paquetes y archivos, luego de unos segundos generara una dirección url la cual será  http://0.0.0.0:5000/ ábrala en su localhost y verá un **hola mundo** en la página de inicio para ver los registros de la base de datos que se creó agréguele a la anterior dirección web ```/items/2``` el número 2 representa cuantos elementes quiere visualizar un ejemplo para 4 elementos sería el siguiente  http://0.0.0.0:5000/items/4, tenga en cuenta que para que funcione el comando anterior debe de tener instalado [docker](https://docs.docker.com/engine/install/ubuntu/) y [docker compose](https://docs.docker.com/compose/install/), a si como también se recomienda seguir el instructivo de pos-instalación suministrado en la [documentación oficial](https://docs.docker.com/engine/install/linux-postinstall/).

