# openmgmt

Documentation and examples for using open network management tools such as OpenConfig

## Tools Setup

### markdownlint-cli

Content is to be linted to ensure consistency of formatting. This requires using
[markdown-cli](https://github.com/igorshubovych/markdownlint-cli).

MacOS users can install markdownlint-cli via homebrew.

```shell
brew install markdownlint-cli
```

Alternately, markdownlint-cli can be installed via NPM, details are available at
the link above.

### pre-commit

In order to automate the process of linting a pre-commit hook is utilized. This
requires the installation of [pre-commit](https://pre-commit.com). Depending on
your environment, the installation process may vary.

#### python PIP installation

If you're using `pyenv` or some other python version manager, pre-commit can be
installed via pip. This ensures that it's installed to your preferred python
environment.

```shell
pip install pre-commit
```

#### homebrew installation

```shell
brew install pre-commit
```

## pre-commit setup

From the root of the repository execute `pre-commit install` this will add the
necessary hooks to your local git configuration and setup the necessary tooling
in order to suport development.

## mkdocs

Install mkdocs via pip:

```shell
pip install mkdocs
```

Install material theme

```shell
pip install mkdocs-material
```

Build and deploy

```shell
mkdocks build
mkdocs gh-deploy
```

Rendered site will stay in `gh-deploy` branch
but keep the source code in `main` or working branches
