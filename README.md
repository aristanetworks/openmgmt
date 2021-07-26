![GitHub](https://img.shields.io/github/license/aristanetworks/openmgmt)
![example workflow](https://github.com/aristanetworks/openmgmt/actions/workflows/main.yml/badge.svg)
![Arista](https://img.shields.io/badge/Arista-OpenMGMT-blue)

# openmgmt

- [Getting Started](#getting-started)
- [Mkdocs](#mkdocs)
  - [Installation](#installation)
  - [Mkdocs Material Theme Installation](#mkdocs-material-theme-installation)
  - [Author Your Content](#author-your-content)
  - [Build Content](#build-content)
  - [Locally View Changes](#locally-view-changes)
- [PR submission](#pr-submission)
- [tooling setup](#tooling-setup)
  - [markdownlint-cli](#markdownlint-cli)
  - [pre-commit](#pre-commit)
    - [python PIP installation](#python-pip-installation)
    - [homebrew installation](#homebrew-installation)
- [pre-commit setup](#pre-commit-setup)
- [Style Guidelines](#style-guidelines)

This repository contains documentation and examples for using open network management tools with Arista's EOS
platforms. These network management protocols include OpenConfig, NETCONF, RESTCONF and others as appropriate.

## Getting Started

If you'd like to submit a contribution simply fork a copy of this repository, install [mkdocs](http://www.mkdocs.org)
and the [mkdocs material](https://squidfunk.github.io/mkdocs-material/) theme. Add your content (in markdown format) and
open a pull request.

For the most part, it's that simple.

## Mkdocs

The OpenMgmt site uses the `mkdocs` tool to render the content into what is displayed on the web site.

### Installation

Installation of mkdocs is handled via pip.

```shell
pip install mkdocs
```

### Mkdocs Material Theme Installation

Since the OpenMgmt site is using the mkdocs-material theme, you will need to install this as well.

```shell
pip install mkdocs-material
```

### Author Your Content

The content for this site is in a collection of markdown files in the 'docs/' directory in this repository.  Add your
content or fixes to this directory.

### Build Content

The following command will build the content so you can take a look at it on the file system.  You're not likely going
to need this that often.  More often you're going to be interested in seeing the rendered content in your browser.

```shell
mkdocs build
```

### Locally View Changes

`mkdocs` makes it easy to see the rendered content locally in your browser.  It is highly recommended that you validate
that your changes do not break anything in the visual rendering of the site. In order to serve the site `mkdocs` will
start a local web server, this can be invoked via the following command from the root of your copy of the repository.

```shell
mkdocs serve
```

**Sample `mkdocs serve` output**

```shell
% mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.68 seconds
INFO     -  [14:55:12] Serving on http://127.0.0.1:8000/openmgmt/
```

You can point your browser at the above URL and you'll be able to see the rendered site.  Now ... assuming everything
looks good, you're able generate a pull request.

## PR submission

If everything looks good, submit a pull request (aka PR).  A series of tests will be applied to validate the tests and
a maintainer will review the PR for incorporation into the `main` branch.  There are a few things that you can do to
streamline the acceptance of your pull request.  Most notable here is conformance to the style guide and aligning with
the linter.

## tooling setup

Taking some time to setup the following tooling and confirming alignment with the [style
guide](contributing/content-style-guide.md) will help to smooth the passage of your pull request.

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

## Style Guidelines

At a high level, documentation contributions should conform to the markdown linting rules as defined in
`.markdownline.yaml`.  Details regarding formating and documentation conventions can be found in the [content style
guide](contributing/content-style-guide.md).
