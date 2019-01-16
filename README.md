# DangerBot

DangerBot is an automated project designed to monitor the HTML-based game [Urban Dead][urban-dead-home].

## Getting Started

This project uses [pipenv][pipenv-docs] to manage dependencies. Once pipenv is
installed on your system you can run the following command to get its dependencies.

```shell
pipenv install
```

## Tasks

There are 3 main tasks that DangerBot attempts to complete
* Check the [Urban Dead wiki][urban-dead-wiki] for stale information about the game's buildings
* Check the [Urban Dead wiki][urban-dead-wiki] for stale information about the game's mobile phone masts
* Walk several characters around the game city to gather information used to update the game's wiki

## License

This project is distributed under the terms of the LICENSE file found at the top level of this repository.


[urban-dead-home]: http://urbandead.com
[urban-dead-wiki]: http://wiki.urbandead.com/index.php/Main_Page
[pipenv-docs]: https://pipenv.readthedocs.io/en/latest/
