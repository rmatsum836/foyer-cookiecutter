# foyer-cookiecutter
A [cookiecutter](https://github.com/audreyr/cookiecutter) template to develop [foyer](https://github.com/mosdef-hub/foyer) force field classes.

## Features
* Pre-configured `setup.py` for installation and packaging which
  automatically registers with the ``entry_point`` group defined in foyer
* Pre-configured Linux and OSX continuous integration on Travis-CI
* Sample test molecule directory and XML force field file

## Requirements

* Python 3.6 or later
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)

## Usage

With `cookiecutter` installed, execute the following command inside the
folder you want to create your skeletal foyer force field package.

```
cookiecutter /path/to/foyer-cookiecutter/
```
From here, the user will be prompted for information on how to build the
directory with the following prompts:

* `project_name`:  Name of the force field package
* `directory_name`: Name of first directory within the package
* `first_module_name`: Name of module within the directory that contains
  functions to load the force field via foyer
* `class_name`: Name of force field class that will be called via
  `foyer.forcefields`
* `DOI`: DOI of force field that will be placed in the XML file

Once you answer these prompts, your force field package will be created.

## Using `entry-points` with foyer

To connect your force field package to foyer, the first step is to install
your package locally by running `pip install -e .` in the project root
directory.  You can test that your force field is recognized by foyer by
running the following commands:

```
python
import foyer
foyer.forcefields.class_name()
```
