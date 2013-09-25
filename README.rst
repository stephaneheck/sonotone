## Create i18n Files
cd <project_path>/sontone
export PATH=/usr/local/Cellar/gettext/0.18.3.1/bin:$PATH
python ../manage.py makemessages -l en

## setup DB
python manage.py syncdb
python manage.py sql pol

## How to install

    virtualenv env
    source env/bin/activate
    add2virtualenv .
    pip install -r requirements-dev.txt
    gem install bootstrap-sass
    gem install bundle
    bundle install
    make run
