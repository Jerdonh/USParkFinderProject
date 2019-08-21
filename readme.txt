US PARK FINDER PROJECT README.txt

To run development localhost:FLASK_APP=FlaskPage.py flask run
Heroku Deployment: https://us-park-finder.herokuapp.com


Documentation Style: pydoc
	-to run: $pydoc3 moduleName

Testing Style: doctest
	-to run: $python3 -m doctest -v moduleName.py

 _________________________________
|ModuleName | Documented | Tested |
|___________|____________|________|
|FlaskPage  |     √      |        |
|PARKSMODEL |     √      |    √   |
|Importer   |     √      |    √   |
|Conversions|     √      |    √   |
|Weather    |     √      |    √   |
|___________|____________|________|

********************************************************************************
__________________________________
Files:
__________________________________
    requirements.txt: specifies all modules that need to be downloaded before runtime
    runtime.txt: specifies python version to run on
    Procfile: specifies moduleName and app name for gunicorn deployment
    ParksData.csv: contains all US Park data required to run web app
    MANIFEST.in: specifies all non-python files and dirs to be included in dist
__________________________________
Subdirs:
__________________________________
    templates: contains html templates for webpage
    Pre-Processing: contains all processes used to build park data
    static: Contains StyleSheets
    build: Contains .py duplicates for distribution
    dist: Contains tar.gz of entire project for easy distribution
