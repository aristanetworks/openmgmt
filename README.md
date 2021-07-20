# openmgmt

- [Style Guidelines](#style-guidelines)
- [Tooling Setup](#tooling-setup)
  - [markdownlint-cli](#markdownlint-cli)
  - [pre-commit](#pre-commit)
    - [python PIP installation](#python-pip-installation)
    - [homebrew installation](#homebrew-installation)
- [pre-commit setup](#pre-commit-setup)
- [mkdocs Operation](#mkdocs-operation)
  - [installation](#installation)
  - [Theme Installation](#theme-installation)
  - [Build Content](#build-content)
  - [Locally (Re)View Changes](#locally-review-changes)
- [Site Deployment](#site-deployment)

Documentation and examples for using open network management tools such as OpenConfig, NETCONF, RESTCONF or tin cans and
string if strictly necessary.

## Style Guidelines

At a high level, documentation contributions should conform to the markdown linting rules as defined in
`.markdownline.yaml`.  Details regarding formating and documentation conventions can be found in the [content style
guide](contributing/content-style-guide.md).

## Tooling Setup

### markdownlint-cli

Content is to be linted to ensure consistency of formatting. This requires using
[markdown-cli](https://github.com/igorshubovych/markdownlint-cli).

MacOS users can install markdownlint-cli via homebrew.

```shell
brew install markdownlint-cli
```

Alternately, markdownlint-cli can be installed via NPM, details are available at the link above.

### pre-commit

In order to automate the process of linting a pre-commit hook is utilized. This requires the installation of
[pre-commit](https://pre-commit.com). Depending on your environment, the installation process may vary.

#### python PIP installation

If you're using `pyenv` or some other python version manager, pre-commit can be installed via pip. This ensures that
it's installed to your preferred python environment.

```shell
pip install pre-commit
```

#### homebrew installation

```shell
brew install pre-commit
```

## pre-commit setup

From the root of the repository execute `pre-commit install` this will add the necessary hooks to your local git
configuration and setup the necessary tooling in order to suport development.

## mkdocs Operation

### installation

Install mkdocs via pip.

```shell
pip install mkdocs
```

### Theme Installation

```shell
pip install mkdocs-material
```

### Build Content

```shell
mkdocs build
```

### Locally (Re)View Changes

It is possible to see the locally rendered content and it is highly recommended that you validate that your changes do
not break something in the visual rendering of the site. In order to locally serve the site mkdocs will start a local
web server, this can be invoked via the following command.

```shell
mkdocs serve
```

## Site Deployment

The site will be built and generated from `main`. This will ensure that all of the content is integrated and
appropriately rendered. **DO NOT deploy directly from a branch other than `main`.** When there are changes to merge
generate a PR and have it merged into `main`. When contributions have been integrated into the `main` branch a github
action will automatically generate and deploy the site.
