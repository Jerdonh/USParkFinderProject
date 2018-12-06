US PARK FINDER PROJECT README.txt

To run development localhost:FLASK_APP=FlaskPage.py flask run
Heroku Deployment: https://us-park-finder.herokuapp.com/more


Documentation Style: pydoc
	-to run: $pydoc3 moduleName

Testing Style: doctest
	-to run: $python3 moduleName.py

 _________________________________
|ModuleName | Documented | Tested |
|___________|____________|________|
|FlaskPage  |     √      |        |
|PARKSMODEL |     √      |        |
|Importer   |     √      |        |
|Conversions|     √      |  1/2   |
|Weather    |     √      |        |
|___________|____________|________|

********************************************************************************
__________________________________
Files:
__________________________________
    requirements.txt: specifies all modules that need to be downloaded before runtime
    runtime.txt: specifies python version to run on
    Procfile: specifies moduleName and app name for gunicorn deployment
    ParksData.csv: contains all US Park data required to run web app
__________________________________
Subdirs:
__________________________________
    templates: contains html templates for webpage
    Pre-Processing: contains all processes used to build park data
    Static: Contains StyleSheets
