
# Repo Creation

LinkML was installed within a conda env to work with locally.

LinkML-OWL extension downloaded via pip: 

> pip install linkml-owl

1. Create cookie cutter template repo from LinkML & new GitHub repo in GitHub GUI (https://github.com/new).

<https://github.com/linkml/linkml-project-cookiecutter>

2. Cruft: used to take a template repo and customize through interactive questions

Cruft Version: 2.15.0 (installed via pipx)
Poetry Version 1.8.3 (installed via pipx)

> cruft create https://github.com/linkml/linkml-project-cookiecutter

Accept all defaults past entries through email

3. cd into ```NIST-GEC_Lexicon/``` and set up vm, install dependencies, etc. 

> make setup

4. Push to GitHub

> git remote add origin https://github.com/usnistgov/NIST-GEC_Lexicon.git
> git branch -M main
> git push -u origin main

5. Change settings in GitHub GUI to allow pages documentation workflows

Publish schema documentation - For the documentation tool, set up Pages in GitHub: 
From your repo's page - go to 
    (repo) > Settings > Pages 
        Branch: gh-pages (branch exists from setup, automatically)

**ISSUE** Do not have a gh-pages branch so can't automatically generate documentation
(have message on linkml slack)

# Schema Dev

/src/nist_gec_lexicon/schema/nist_gec_lexicon.yaml

Boilerplate: 

```
id: https://w3id.org/NIST/NIST-GEC_Lexicon
name: NIST-GEC_Lexicon
title: NIST-GEC_Lexicon
description: |-
  NIST Genome Editing Lexicon ontology repo with LinkML
license: MIT
see_also:
  - https://NIST.github.io/NIST-GEC_Lexicon
```

**prefixes**

How to map shorter URIs to longer form URIs
Allows us to map to other ontologies

```
prefixes:
  nist_gec_lexicon: https://w3id.org/NIST/NIST-GEC_Lexicon/
  linkml: https://w3id.org/linkml/
  biolink: https://w3id.org/biolink/
  schema: http://schema.org/
  PATO: http://purl.obolibrary.org/obo/PATO_
  example: https://example.org/
default_prefix: nist_gec_lexicon
default_range: string
```

**Mapping to OWL**

Each LinkML class maps to an OWL class

Each LinkML slot maps to an OWL property

<https://linkml.io/linkml/generators/owl.html>



# Generate OWL 

**note** every time I ran poetry I was getting a 'The virtual environment found in [path] seems to be broken.' 

To resolve: 
> poetry shell
> poetry env use python3.10
> poetry install

--add-root-classes