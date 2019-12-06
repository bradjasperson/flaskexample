# flaskexample
A simple flask CRUD server with sqlite

## Container Setup
1. Run `docker-compose up` (use -d if you want it to run in the background)

## Usage
* To add an entry `curl -H "Content-Type: application/json" --request POST --data '{"name":"Brad"}' localhost:5000/name` (name must be unique)
* Get all entries `curl -H "Content-Type: application/json" --request Get localhost:5000/name`
* Get entry by id `curl -H "Content-Type: application/json" --request Get localhost:5000/name/ID` (ids are numerical starting with 1)
* Update entry `curl -H "Content-Type: application/json" --request PUT --data '{"name":"Brad"}' localhost:5000/name/id` (name must be unique)
* Delete entry `curl -H "Content-Type: application/json" --request DELETE localhost:5000/name/id`
