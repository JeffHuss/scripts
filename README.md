## Welcome!

**Welcome to my humble script repository.**

#### Directory structure:

- legacy_scripts/
  - An incomplete collection of scripts I've used while working as a support engineer and tech writer ("legacy_scripts") folder.

- archived_assignments/
  - Collection of various scripts I've written while working through online coursework. Much of it is from https://cs50.harvard.edu/python/2022/

- templates/
  - This is where I store any templates that are used in other places. Organization is....emergent :)

#### Useful files:

- ./new_project.sh
  - This bash script is useful for initializing a new Python project. It takes a project name as a command-line argument.
  - It creates a directory named after the command-line argument you provide.
  - It creates a blank requirements.txt which can be populated later.
  - It copies setup.h from templates/ for quickly putting together a venv with the necessary dependencies.
  
- ./templates/setup.sh
  - Running this bash script after copying source files makes it easy to setup a venv if one doesn't already exists.
  - It also reads requirements.txt and installs any needed dependencies (using pip install) that are listed.
  - No need to use this script - it's just there for convenience.

**Note**: I use a quick bash function to clean up the dir once I'm done working so that it's packaged for reuse in the future without having to remember anything about the configuration. That script looks like this:

```bash
pclean() {
    pip freeze > requirements.txt
    pip freeze | xargs pip uninstall -y
    deactivate
    rm -r venv/
}
```
