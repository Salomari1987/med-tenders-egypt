# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from textblob.classifiers import NaiveBayesClassifier
from django.db import IntegrityError

class ScrapTendersPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except IntegrityError:
            pass
        return item


class ClassifyTendersPipeline(object):
    def process_item(self, item, spider):
        item['classification'] = classify(item['Description'])
        return item
train = [
    ("Supply And Erection Of 60 Human Simulators For The Faculty Of Dental Medicine", "Medical Equipment"),
    ("Supply Of Medical Requisites For The Medical Treatment Dept", "Medical Equipment"),
    ("Supply Of Requirements Of The Employees Hospital In Nagee Hamadi Of Medicines & Medical Requisites.", "Pharmaceutical"),
    ("Supply Of Medical Instruments & Requisites.", "Medical Equipment"),
    ("Supply Of An Instrument To Digitally Develop X Ray Photos With Related Accessories", "Laboratory Product"),
    ("Supply Of A Radio Active Material Fia - Fdg For The Pec - Ct Preston Diagnostic X Ray Instrument.", "Laboratory Product"),
    ("Supply Of Requisites For The Interactive Brain X Ray Unit.", "Medical Disposable and Consumable"),
    ("Supply Of X-ray Image Treatment Devices", "Medical Equipment"),
    ("Supply Of Chemicals For The Laboratories Dept", "Laboratory Product"),
    ("Supply Of Medicines And Medical Requisites For The Company~s Hospital For One Year", "Pharmaceutical"),
    ("Supply Of (a) Requisites Of The X Ray Division, (b) Requisites For The Endoscopes Unit, (c) Chemicals And Requisites Of The Blood Bank, (d) Chemicals For The Instrument To Automatically Analyze Blood", "Medical Disposable and Consumable"),
    ("Supply Of Surgical Tools For The Dental Medicine Clinic", "Medical Equipment"),
    ("Pact Brushes Sterile Blood Remover And Detergent Enzyme And Rust Remover And A Chemical Indicator For Sterilization", "Medical Disposable and Consumable"),
    ("Purchase Of Scientific Equipment For The Project Development Unit Of Microbiology Lab Laboratory Abu Rish Hospital Enlightening For Children", "Laboratory Product"),
    ("Buy Clothes Workers And Patients Required For The Directorate Of Health And Its Units", "Medical Disposable and Consumable"),
    ("The Supply Of Ready-made Meals In Hospital", "Nutrition and Cosmetic"),
    ("Public Tender For The Supply Of Tablets And Capsules Drugs", "Pharmaceutical"),
    ("Develop And Raise The Efficiency Of A Number (11) Health Eastern Region Unit", "Other"),
    ("Complete The Development Of Health Center For Reproductive Bareicheh Egypt Ismailia", "Other"),
    ("Provide Information Services Field To Make Sure The Data Provided Dealers With The Health Fund", "Other"),
    ("Medical Supplies", "Medical Disposable and Consumable"),
    ("Supply of food and beverages and meals for hospital workers", "Nutrition and Cosmetic"),
    ("Construction Of Three Medical Centers In Northern Sinai", "Other"),
    ("Supply of Drugs and Vaccines", "Pharmaceutical"),
    ("Supply of medical supplies and materials", "Medical Disposable and Consumable")
]
def classify(desc):
    cl = NaiveBayesClassifier(train)
    classification = cl.classify(desc)
    print classification
    return classification
