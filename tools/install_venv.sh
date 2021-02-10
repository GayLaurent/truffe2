#!/bin/bash
# Script to install virtual environment for truffe2 for developpement
# --- DO NOT USE IN PRODUCTION MODE ---

set -e
set +x

project_dir="$(dirname $(dirname $(readlink -f "$0")))"

if [ "$1" != "noclean" ]
then
	rm -rf "$project_dir/venv"
	python3 -m virtualenv --python python3.7 "$project_dir/venv"

	. "$project_dir/venv/bin/activate"
	pip install -U pip
	pip install -r "$project_dir/truffe2/data/pip-reqs.txt"
else
	. "$project_dir/venv/bin/activate"
fi

rm -rf "$project_dir/truffe2/db.sqlite3"
cp "$project_dir/tools/settingsLocal.py.test" "$project_dir/truffe2/app/settingsLocal.py"

(
	cd "$project_dir/truffe2"
	python -Wd manage.py migrate
	if [ "$2" == "demo" ]
	then
		echo 'from main.test_data import setup_testing_all_data; setup_testing_all_data()' | python -Wd manage.py shell
	fi
)