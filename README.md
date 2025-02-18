# Trilab Tools

This repository contains analysis scripts used within the Tripodi Lab, written in Python for Antelop.

### Purpose

This repository serves two main functions:

* First of all, it allows us to share analysis functions easily between lab members, and between machines (including the cluster).
* Second, it aides with experiment reproducibility by tracking the versions of analysis scripts run over time.

All the analysis functions here are written for integration in Antelop, our lab's SQL-based data storage and preprocessing software suite. As such, functions must be written in a particular way, including decoration and the declaration of some required attributes. For more information, see here:

[Antelop docs](https://antelope.readthedocs.io/en/latest/python/analysis.html)

### Usage

We organise this repository by folders, with each folder corresponding roughly to an experiment. Folders can have multiple scripts, each with multiple functions in them.

You should first of all work on your functions locally, inside your configured Antelop analysis folder. Once you have verified that your scripts work as expected, you can copy them to a folder inside your cloned version of this repository, and commit+push it.

For a given experiment, you should use a single folder in this repository, and include a README and a requirements.txt for additional dependencies beyond that included with the base Antelop installation. It is your responsibility to make sure these requirements are compatible with Antelop.
