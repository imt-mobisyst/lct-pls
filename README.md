# Lecture: Python Libs. pour les Sciences

Ce _repo_ (privé) regroupe les support de cours _PLS_ (Python Librairies pour les Science) proposé aux étudiants du parcours ID de l'IMT- Nord Europe.
Les supports de cours sont servie cours sur [imt-mobisyst.github.io/lct-pls](https://imt-mobisyst.github.io/lct-pls/).

## Install:

_lct-pls_ can be cloned and relies mainly on _mkdods_.
Also, the proposed command tools based on [toml](https://toml.io) configuration file.

```sh
pip install mkdocs toml toml-cli
git clone https://github.com/imt-mobisyst/lct-pls.git
cd lct-pls
```

## Get Stated:

The documentation is on [Markdown](https://en.wikipedia.org/wiki/Markdown) format starting by `index.md` in the `docs` directory.
It can be served as a _HTML_ web site thanks to [MkDocs](https://www.mkdocs.org/).

```sh
mkdocs serve
```

You can then refer to the [http://127.0.0.1:8000/](documentation).
The navigation structure is defined on the `mkdocs.yml` file.

## Contribute 


### WebPages

Doc. deployment is achieved with a public github repository (_imt-mobisyst.github.io.git_), by copying the _mkdocs_ generated site in the `lct-pls` directory of this public repository.

```sh
mkdocs build
git clone git@github.com:imt-mobisyst/imt-mobisyst.github.io.git ../imt-mobisyst-site
rm -fr ../imt-mobisyst-site/lct-pls
mv ./site ../imt-mobisyst-site/lct-pls
git -C ../imt-mobisyst-site commit -am "lct-pls updates"
git -C ../imt-mobisyst-site push
```

For convenience, this manipulation is automatized with the script `./bin/docs-deploy.sh`.
To notice that the documentation repository can be cloned anywhere on your computer while your `config.toml` is updated accordingly.


### Slide Presentations

The presentation/slides are prepared using `marp` (an extantion to Markdown permiting to generate slides pdf).
`marp` is fully integrated to _VisualCode_:

- Get *Marp for VS Code* extention
- On `VS Code parameters > working space > Marp for VS Code` you can add elements on `Markdown › Marp: Themes` : `slides/style/imt.css`.
- Also authorise html tag. activate `marp: Enable HTML` in settings.

