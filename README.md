# Onecloud test

Test Python, Angular, Django.

# Setup

1. Install and start virtualenv -> https://virtualenv.pypa.io/en/latest/installation.html
2. Clone this repository for the folder -> git clone https://github.com/lemon123456/Protractor.git
3. cd Protractor
4. Execute command -> pip install -r requirements.txt 
5. Run test -> python manage.py test

# Start Project

1. python manage.py runserver
2. Visit http://localhost:8000


# Config Protractor

1. Add *_conf.js file
2. Add *-spec.js file
3. Run test -> protractor test/*-spec.js
   (run 'webdriver-manager start' before 'protractor test/functional_multiple_conf.js')

