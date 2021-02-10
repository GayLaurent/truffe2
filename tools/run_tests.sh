#!/bin/bash

set +e
set +x

project_dir=$(dirname $(dirname $(readlink -f "$0")))

rm -rf $project_dir/htmlcov
. $project_dir/venv/bin/activate

cd $project_dir/truffe2
python -m pip install -U coverage >/dev/null
python -m coverage erase
python -Wd -m coverage run --branch --source=. manage.py test
# python -m coverage report
python -m coverage html -d $project_dir/htmlcov

deactivate
