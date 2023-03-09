# Python Virtual Environments: A primer
> Making sure projects never cause dependancy conflicts
## L.O
- Create and activate a python virtual environment
- Explain why you want to isolate external dependancies
- Visualise what python does when you create a virtual environment
- Customise your virtual environments using optional arguments to venv
- Deactivate and remove virtual environmens
- Choose additional tools for managing your python versions and virtual environments

# How 
Best used when working on a python project that requires you to use external dependancies installed with pip
## Create it

- Bash command:
    python3 -m venv venv
- windows command
    python -m venv venv
    (potentially might have to use the full path instead)
## Activate it 
There is a script that comes with its installation that is used to activate the venv
- Bash command:
source venv/bin/activate
- windows command:
    venv\scripts\activate

you must be in the folder that contains the virtual environment
Once you see the name of the venv in your command prompt you know its activated
## Installing packages into it 
- Bash command:
    python -m pip  install <package-name>
## Deactivating it 
- Bash Command:
    deactivate

This means that you have exited your virtual environment

# Why do you need Virtual Environments
Python installs all external packages in a folder called site-packages in your base python installation

## Avoid System pollution
- packages can mix with operating system packages and cause side affects
- updating system could remove/overwrite previously used packages

## Sidestep Dependency Conflicts
- Allows you to use two different versions of the same package incase one project works with an older verison

## Minimise Reproducibility Issues 
- Allows you to pin dependencies that are relevant to a specific project when sharing project online
- Easier collaboration 
## Dodge installation Privilege lockouts
- installation within your accounts privileges if you are not the admin user.

# What is a Python Virtual Environment 
A folder structure that gives you everything you need to run a lightweight isolated python environment.
## Structure 
In the structure there are copies or symlinks to the python executable files 


# References 
- https://realpython.com/python-virtual-environments-a-primer/