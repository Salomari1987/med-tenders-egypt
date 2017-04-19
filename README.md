# Tenders Classifier App

## Description
This is an application that crawls http://www.medicaltenders.com/ website for medical tenders in Egypt, classifies the data and stores it in an sqlite database for simplicity, with a UI to display the results

## Technologies used
* Python Scrapy Spider
* Python NLTK Nayev Bayes classifier
* Python 2.7
* Django 1.10
* JavaScript
* jQuery
* CSS and bootstrap
* Django HTML templates
* Sqlite3

## How to run
### First time only
1. Clone repository
1. Create virtual environment `mkvirtualenv tenders`
1. Install requirements `pip install -r requirements.txt`
1. Migrate Database `python manage.py makemigrations && python manage.py migrate`
  * **Note: you must be in .../tenders/django directory `cd`**
### Anytime
* Run the crawler first: `scrapy crawl tender`
  * **Note: you must be in .../tenders/scrap_tenders/scrap_tenders directory `cd`**
* Run the server: `python manage.py runserver 0.0.0.0:8000`
  * **Note: you must be in .../tenders/django directory `cd`**

After running the server, you can browse the app on your browser at localhost:8000

## Test classifier
* Run classifier tests by running `python ./test_classifier.py` from inside scrap_tenders/scrap_tenders/classifier and see results on terminal

```
The F-MEASURE (2*recall/(recall+precision) accuracy of the Nayev Bayes classifier for:

      Medical Equipment: 83.3333333333%

      Pharmaceutical: 80.0%

      Laboratory Product: 100.0%

      Medical Disposable and Consumable: 85.7142857143%

      Nutrition and Cosmetic:100.0%

      Other: 105.0 %

      and, Overall 92.3412698413%
```
