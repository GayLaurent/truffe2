Truffe 2
========

Truffe 2 is the new intranet for AGEPoly - The EPFL's students' association.

## License

Truffe 2 is licensed under the [BSD](http://opensource.org/licenses/BSD-2-Clause) license. Check LICENSE.md

## Authors

### Core developpers

* [Maximilien Cuony](https://github.com/the-glu)
* [Lionel Martin](https://github.com/lionel-martin)

### Contributors

* Cedric Cook (Fixed a typo)
* Yolan Romailler (Fixed a path)
* Yann Beaud (Fixed VCARDs)
* Laurent Gay (Migration to Python3/Django3)

## Development

This is a standard django project. Python requirements are stored in `truffe2/data/pip-reqs.txt`.

This projects requires ImageMagick which can be obtained using `brew install freetype imagemagick`

You will need access to tequila (EPFL internal network is enough) to login.

No initial database is provided. To begin, grant yourself admin rights in the database after a first login, and create at least one unit.

South is used for migrations. Be careful, some models are created dynamically!

You will need a `truffe2/app/settingsLocal.py` file with your local settings (database, etc.). A template is provided in `truffe2/app/settingsLocal.py.dist`. According to which database driver you choose, install the corresponding python package, e.g. `pip install mysql-python` for MySQL.

Deployment scripts using fabric are located in the `Deployment` folder.

### Example development environment setup

1. Create a virtual Python 3 environment: `virtualenv --python=/usr/bin/python3 venv`
2. Activate it: `. ./venv/bin/activate`
3. Install dependencies: `pip install -r ./truffe2/data/pip-reqs.txt`
4. `cp ./truffe2/app/settingsLocal.py{.dist,}`
5. Edit `./truffe2/app/settingsLocal.py` and set the database engine to `django.db.backends.sqlite3` and database name to `db.sqlite3`
6. To be apple to see the mails sent from the application, run a [maildump](https://pypi.python.org/pypi/maildump) instance on port 1025
7. Go inside the `truffe2` directory for the next steps: `cd truffe2`
8. On OSX, if you get `ImportError: MagickWand shared library not found.`, it's probably because Python was not installed using MacPorts, you have to export MAGICK_HOME path. You should try to set the path with `export MAGICK_HOME=/opt/local` and go back to point 8.
9. Create the database tables with `python manage.py migrate`
10. Run the development server with `python manage.py runserver`
11. Go to `http://localhost:8000/` and log in with Tequila
12. Give your user superuser rights with `echo "update users_truffeuser set is_superuser=1 where id=1;" | sqlite3 db.sqlite3`

Those actions are setting in a script for Linux : `tools/install_venv.sh`.  
2 Options for this script:
 - `./tools/install_venv.sh noclean` : don't remove virtual Python environment, just delete SQLite DB file and reload a new DB.  
 - `./tools/install_venv.sh "" demo` : add examples of data for testing in DB (5 users: admin, user1, user2, user3, user4 with username as password).  

A new script, `tools/run_tests.sh`, allows to launch tests with code coverage.  
