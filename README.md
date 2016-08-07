# Getting Started With Python and Flask

To start just ensure you download and install python and pip, for mac users this can be done using hoem brew:

`brew install python`

You may need to add it to your path as mac come with an outdated python, check the version using
`python --version`

If that's the version you install than you are ready to go, otherwise ensure you add the last version to your path.
To do that you can use the **~/.profile**

```sh
cd ~
nano .profile
```

and add the export in this way
```
export PATH="/usr/local/bin:$PATH"
```

By installing python using **homebrew** you will have pip installed 
we will need it to install **virtualenv** and **virtualenvwrapper**

This will make the development easier and will improve our workflow.

To install this 2 run:
```
pip install virtualenv
pip install virtualenvwrapper
```

Next is to setup some configuration



```
nano ~/.profile
```

and add this to your profile, so your profile should look like that

```
export PATH="/usr/local/bin:$PATH"

# Virtualenvwrapper setup
export WORKON_HOME=$HOME/.envs
export PROJECT_HOME=$HOME/dev
source /usr/local/bin/virtualenvwrapper.sh
```
We are almsot done!

**To create a project using virtualenvwrapper**

`mkproject HelloWorld`
This will create a project and all its depandancies in the isolated enviroment

**To switch to another project**

`workon HelloWorld`
This will cd to the project directory and load the virtualenv associated with the project

**Install depandancies using pip**

This project is using number of packages in order to run the project you will have to install all of them

To do that run this command
```
pip install -r requirements.txt
```



## Run the project

To run the project you will need to create the db first

**Creating and initializng the database**
The following command should create HelloWorld.db file and initializng the tables in the db
```
python manage.py initdb
```

**To drop the database**
You can drop any time the database to start with fresh data using this command
```
python manage.py dropdb
```

**To start the web server**
After initializing the data base you can start the web server using the command
```
python manage.py runserver
```