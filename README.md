# Práctico 2

En esta parte del práctico vamos a retomar los temas ya vistos en clase para construir un web scraper que extrae imágenes de propiedades del [Gallito](gallito.com.uy/).

Vamos a entrar en mayor profundidad en dependencias de python, web scraping, docker, y azure.

## Manejo de dependencias en Python
Usamos [`pip-tools`](https://pip-tools.readthedocs.io/en/latest/) para manejar las dependencias de Python. 
## Scrapy

Usamos [Scrapy](https://docs.scrapy.org/en/latest/) para construir la spider que va a recorrer el sitio del Gallito para extraer los datos de las propiedades.

Dentro de la documentación de Scrapy, les será útil revisar las entradas sobre:
* instalación
* [spiders](https://docs.scrapy.org/en/latest/topics/spiders.html), en especial la [CrawlSpider](https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider) y sus [Rules](https://docs.scrapy.org/en/latest/topics/spiders.html#crawling-rules)
* [link extractors](https://docs.scrapy.org/en/latest/topics/link-extractors.html)
* callbacks
* CSS [selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)
* [Item Pipeline](https://docs.scrapy.org/en/latest/topics/item-pipeline.html), por ejemplo para descargar archivos o imágenes con una [MediaPipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html) como la ImagesPipeline.

## Git

Llegado este práctico ya van a estar familiarizados con [git](https://git-scm.com/docs), [Github](https://github.com/), y sus comandos principales: init, add, commit, push, pull, status.

## Docker

Llegado este práctico ya van a estar familiarizados con el [Dockerfile](https://docs.docker.com/engine/reference/builder/), y los comandos docker [build](https://docs.docker.com/engine/reference/commandline/build/), [run](https://docs.docker.com/engine/reference/commandline/run/) y [push](https://docs.docker.com/engine/reference/commandline/push/). 

## Azure

Todos debemos crearnos una cuenta en Azure usando nuestro email `<usuario@fi365.ort.edu.uy>` para poder obtener los beneficios de la cuenta educacional. 

Para trabajar con Azure vamos a necesitar instalar la [CLI de Azure](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) y habernos logueado corriendo `az login`.

En Azure vamos a ver cómo usar el [Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs) para almacenar las imágenes que extrae nuestro scraper. 

También vamos a ver cómo usar el [Container Registry](https://azure.microsoft.com/en-us/products/container-registry) para registrar la imagen que buildeamos. 

Por último usaremos [Container Instances](https://azure.microsoft.com/en-us/products/container-instances) para correr nuestra spider en la nube.

