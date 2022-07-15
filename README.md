# lulo_bank
Prueba técnica Lulo Bank - Data engineers

En este repositorio se encuentran los resultados de la prueba técnica, los pasos para ejecutar esto son los siguientes:
* clone este repositorio ```git clone git@github.com:AletzB/lulo_bank.git``` en su carpeta local o descargue el zip 
* Diríjase a la carpeta que contiene un archivo llamado **Dockerfile**
* Abra una terminal nueva y digite lo siguiente ```docker-compose up --build``` automáticamente docker gestionara todos los paquetes y archivos, luego de unos segundos generara una dirección url la cual sera  http://0.0.0.0:5000/ ábrala en su localhost y vera un hola mundo en la pagina de inicio para ver los registros de la base de datos que se creo agreguele a la anterior direccion ```/items/2``` el numero 2 representa cuantos elementes quiere visualizar un ejemplo para 4 elementos seria el siguiente  http://0.0.0.0:5000/items/4, tenga en cuenta que para que funcione el comando anterior debe de tener instalado [docker](https://docs.docker.com/engine/install/ubuntu/) y [docker compose](https://docs.docker.com/compose/install/), a si como también se recomienda seguir el instructivo de pos-instalacion suministrado en la [documentación oficial](https://docs.docker.com/engine/install/linux-postinstall/).
* en la página generada encontrara dos tablas, un input y un botón enviar, si da click enviar sin digitar nada el automáticamente buscara las 150 primeras casas de   [metros cúbicos](https://inmuebles.metroscubicos.com/distrito-federal/), si se digita un numero buscara ese numero de casas en la misma página.
* finalmente en la terminal después de unos segundos se imprime un __OK__ lo cual indica que el proceso termino, puede actualizar la página y se podrán visualizar los datos reflejados en la misma.
