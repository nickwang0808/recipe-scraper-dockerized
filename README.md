# Recipe Scraper Dockerized

This is a implementation of the lib `recipe-scrapers`, in-order to use the script in another service without setting up a http server. I am simply dockerizing the code and running it as child process from the main server.

## Usage

simply call `docker run <name> <url> <true>?` to return the parsing result
