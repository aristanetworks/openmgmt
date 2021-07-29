# Overview

Welcome to the style guide for the OpenMgmt repo!

These guidelines are specific to this repository and are not necessarily reflective of Arista style guides more broadly.

## General Notes

Content written for the OpenMgmt repository should use a gender-neutral, third-person voice.  There's no need to strive
for strict formality but avoiding first person references (I, me, we, etc.) and keeping a focus on the action at hand
will help the reader.

DRY (Don't Repeat Yourself) reigns supreme.  In the interests of consistency, reference existing documentation.  This
means examples should refer to a common suite of documentation for frequent operations.  i.e.: There's no need to
replicate the instructions for enabling gnmi on an Arista switch when this is documented in common location.  However,
if there's an additional configuration requirement or a specific bit of functionality that is associated with your
topic(s), please be sure to note this accordingly.

## A Note Regarding Tooling

The small amount of time it takes to incorporate the tooling listed in the README and integrating it into your
environment will pay dividends for you and your co-authors.  Run your linter frequently. Text editors commonly provide
the ability to fully integrate linting into the workflow, such that you can see issues as you're writing.

If your text editor supports it, you are encouraged to enable the [EditorConfig](https://editorconfig.org/) feature to
make your editor "do the right thing" by default. An editorconfig file has been provided in this repository that is
aligned with this style guide.

Enabling pre-commit hooks as outlined in the README will also ensure that you're aligned with the style guide, at least
from a formatting perspective, by default.

## Document Formatting

### Headings

Headings should be used to provide structure within a document and will be leveraged to generate a Table of Contents by
the `mkdocs` tooling.  There should be no Heading Level 1 in the documents. This is enforced by the linter.

Headings should increment at most 1 level at a time. Sibling headings are allowed and enforced per the linter.

### Code Blocks

Code blocks must be fenced with an appropriate language specified for syntax highlighting.  The linter should enforce
this requirement.  As a general rule the following mappings are applicable to documentation in this repository:

- **EOS commands and output** - use format `text`
- **shell commands and output** - use format `shell`
- **json output** - use format `javascript`

Commands should be separated from execution output such that a user who is reading the document can use the "copy"
feature in a code block and get _only_ the relevant elements for experimentation without a need for cleanup prior to
pasting.  Long command output should be bracketed with the `<detail>` tags to allow the reader to expand/contract
content as appropriate.

Shell commands should be free of `./` ornamentation and assume that the command under execution is in the users path and
not specific to the local directory unless this is specific to a series of steps that are associated with the task at
hand.  (e.g.: If a specific build of software is being outlined and the steps are clearly associated with the current
working directory.)

Where possible it is useful to refrain from having unnecessary prompt ornamentation in command output (e.g.: hostname,
path, etc.) However, if a specific privilege mode is required it may be useful to hint this via the prompt.  Use your
judgment here.

JSON output should be fully and indented to expanded to convey hierarchy.

Use of continuation backslashes to break up long command lines should be used where ever possible.  Keeping within the
80 column width for code samples where possible improves readability.  The long nature of OpenConfig paths makes this
difficult so constraining excessively long lines where possible is useful.

**example:** hard to read

```shell
gnmic -a 10.83.13.214:6030 -u cvpadmin -p arastra --insecure --gzip get --path '/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp'`
```

**example:** easier to read

```shell
gnmic -a 10.83.13.214:6030 -u cvpadmin -p arastra --insecure --gzip get \
  --path '/network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp'`
```

In the interests of conveying context particularly for API actions, it's useful to couple the verb (GET, SET, etc.) with
the noun being acted on in the command.

**example:** verb-noun coupling (good)

```shell
gnmi -addr 10.83.13.139 -username admin \
  get '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
```

**example:** verb-noun decoupling (bad)

```shell
gnmi -addr 10.83.13.139 -username admin get \
  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
```
