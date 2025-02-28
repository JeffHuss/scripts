## Welcome!

**Welcome to my humble script repository.**

#### Directory structure:

- `legacy_scripts/`
  - An incomplete collection of scripts I've used while working as a support engineer and tech writer ("legacy_scripts") folder.

- `archived_assignments/`
  - Collection of various scripts I've written while working through online coursework. Much of it is from [CS50’s Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/)

- `templates/`
  - This is where I store any templates that are used in other places. Organization is....emergent :)

#### Useful files:

- `./new_project.sh`
  - This bash script is useful for initializing a new Python project. It takes a project name as a command-line argument.
  - It creates a directory named after the command-line argument you provide.
  - It creates a blank requirements.txt which can be populated later.
  - It copies setup.h from templates/ for quickly putting together a venv with the necessary dependencies.
  
- `./templates/setup.sh`
  - Run this to create a venv in the project directory.
  - If requirements.txt contains any dependencies, it will install them with `pip`

**Note**: I use a quick bash function to clean up the dir once I'm done working so that it's packaged for reuse in the future without having to remember anything about the configuration. That script looks like this:

```bash
pclean() {
    pip freeze > requirements.txt
    pip freeze | xargs pip uninstall -y
    deactivate
    rm -r venv/
}
```
