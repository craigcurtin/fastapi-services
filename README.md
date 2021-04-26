# Demo of FastAPI Services

this is a simple sketleton of a FastAPI Service ...
1. Clone the project, 


## Makefile

```bash
# below will trigger service to add items to the database
make create-items # create items for illustration purposes

# below will trigger serice to return items
make get-items # retrieve items for illustration purposes
```


## to run in PyCharm, 'select main' and run
```bash
$ make create-items

$ make get-items
```


## to get the OpenAPI docs ... try the below urls in browser

### standard openapi
http://0.0.0.0:7000/docs

### redoc descriptions
http://0.0.0.0:7000/redoc

### below will return the json value for importing 
http://0.0.0.0:7000/openapi.json



