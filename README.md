# DangerBot

DangerBot is an automated project designed to monitor the HTML-based game [Urban Dead][urban-dead-home].

## Getting Started

### Installation
This project uses [pipenv][pipenv-docs] to manage dependencies. Once pipenv is
installed on your system you can run the following commands to get its dependencies and run it.

```shell
pipenv install
```

### Running DangerBot
You can run DangerBot with the following commands

```shell
# to move the characters in the game
pipenv run python -m dangerbot scout

# to update the wiki from the logs
pipenv run python -m dangerbot report
```

## Tasks

There are 3 main objectives that DangerBot is designed to accomplish
* Check the [Urban Dead wiki][urban-dead-wiki] for stale information about the game's buildings
* Check the [Urban Dead wiki][urban-dead-wiki] for stale information about the game's mobile phone masts
* Walk several characters around the game city to gather information used to update the game's wiki

## Development

To install dependencies for developing DangerBot you should run the following command

```shell
pipenv install --dev
```

To execute the tests, simply run

```shell
pipenv run python -m pytest
```

## License

This project is distributed under the terms of the LICENSE file found at the top level of this repository.


[urban-dead-home]: http://urbandead.com
[urban-dead-wiki]: http://wiki.urbandead.com/index.php/Main_Page
[pipenv-docs]: https://pipenv.readthedocs.io/en/latest/
