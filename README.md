# WEBCRAWLER

## Este sistema de webcrawler obtiene información de accesorios de la página de mercado libre de argentina.

### Requerimientos para que el programa funcione.

* Tener Python instalado (obviamente)
* Tener instalada la librería [Scrapy](https://scrapy.org/)
* Tener instalada la librería [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/#Download)
* (OPCIONAL) instalar el prompt de [miniconda](https://conda.io/miniconda.html) (en caso de que de algún error las librerías anteriores).

### Pasos para hacerlo funcionar:

1. Clonar el proyecto.
2. Entrar a la consola de comandos.
3. Entrar a la carpeta "webcrawler"
4. Ejecutar el siguiente comando:
   1. scrapy crawl  accesorios -o data.csv -t csv
   1. donde "accesorios" es el nombre del spider, "data" es el nombre del archivo que guardará los datos, y "csv" el nombre del formato que se guardará el archivo.
5. Para detener el webcrawler se debe presionar ctrl+C.
5. El archivo con los datos se creará dentro de la carpeta "webcrawler".
