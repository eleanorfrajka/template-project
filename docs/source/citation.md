# Citable software

Suppose your software project is software to be associated with a paper or as an output on a project.  To make it straightforward for people to cite it, add a [CITATION.cff](https://github.com/eleanorfrajka/template-project/blob/main/CITATION.cff) file to the root directory.  Here you can add multiple authors, refer to the version number (which should match the PyPI and GitHub version) and specify the date.

For example,
```markdown
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
- family-names: Frajka-Williams
  given-names: Eleanor
  orcid: https://orcid.org/0000-0001-8773-7838
  affiliation: University of Hamburg, Bundesstraße 53, 20146 Hamburg, Germany
title: amocarray
version: 0.0.2
date-released: 2025-04-12
url: https://github.com/AMOCcommunity/amocarray
```