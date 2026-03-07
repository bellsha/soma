<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# SOMA: Schema for Outcomes, Measurements, and Assays

A [LinkML](https://linkml.io/) data model for representing assays, measurements, and experimental
protocols in environmental health sciences (EHS) outcomes research. The schema captures airway biology
assays relevant to respiratory health outcomes and integrates with the Adverse Outcome Pathway (AOP)
framework.

## Key Features

- **Assay-centric architecture** with domain-specific assay classes (CiliaryFunctionAssay,
  LungFunctionAssay, OxidativeStressAssay, etc.) using named measurement slots
- **StudySubject hierarchy** for describing biological systems: cell cultures (CellularSystem,
  TwoDCellCulture), human/animal subjects (InVivoSubject), populations (PopulationSubject)
- **Typed protocol hierarchy**: ImagingProtocol, MolecularAssayProtocol, StainingProtocol,
  SpirometryProtocol
- **AOP Framework integration**: KeyEvent and AdverseOutcomePathway classes with assay linkage
  via `informs_on_key_event`
- **Ontology-backed** entities mapped to GO, ChEBI, CL, UO, OBI, and other biomedical ontologies

## Documentation Website

[https://EHS-Data-Standards.github.io/soma](https://EHS-Data-Standards.github.io/soma)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [soma](src/soma)
    * [schema/](src/soma/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/soma/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
