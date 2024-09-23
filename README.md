# NIST-GEC_Lexicon

NIST Genome Editing Lexicon ontology repo with LinkML

## Website

[https://NIST.github.io/NIST-GEC_Lexicon](https://NIST.github.io/NIST-GEC_Lexicon)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [nist_gec_lexicon](src/nist_gec_lexicon)
    * [schema](src/nist_gec_lexicon/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/nist_gec_lexicon/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
