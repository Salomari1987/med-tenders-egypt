# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from textblob.classifiers import NaiveBayesClassifier

class ScrapTendersPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item


class ClassifyTendersPipeline(object):
    def process_item(self, item, spider):
        item['classification'] = classify(item['Category'] + ';' + item['Description'])
        return item


train = [
    ("Healthcare Equipment and Services; Supply And Erection Of 60 Human Simulators For The Faculty Of Dental Medicine", "Medical Equipment"),
    ("Healthcare Equipment and Services; Supply Of Medical Requisites For The Medical Treatment Dept", "Medical Equipment"),
    ("Pharmaceuticals , Healthcare Equipment and Services; Supply Of Requirements Of The Employees Hospital In Nagee Hamadi Of Medicines & Medical Requisites.", "Pharmaceutical"),
    ("Healthcare Equipment and Services; Supply Of Medical Instruments & Requisites.", "Medical Equipment"),
    ("Healthcare Equipment and Services; Supply Of An Instrument To Digitally Develop X Ray Photos With Related Accessories", "Laboratory Product"),
    ("Pharmaceuticals , Healthcare Equipment and Services; Supply Of A Radio Active Material Fia - Fdg For The Pec - Ct Preston Diagnostic X Ray Instrument.", "Laboratory Product"),
    ("Healthcare Equipment and Services; Supply Of Requisites For The Interactive Brain X Ray Unit.", "Medical Disposable and Consumable"),
    ("Healthcare Equipment and Services; Supply Of X-ray Image Treatment Devices", "Medical Equipment"),
    ("Pharmaceuticals; Supply Of Chemicals For The Laboratories Dept", "Laboratory Product"),
    ("Pharmaceuticals; Supply Of Medicines And Medical Requisites For The Company~s Hospital For One Year", "Pharmaceutical"),
    ("Chemicals , Healthcare Equipment and Services; Supply Of (a) Requisites Of The X Ray Division, (b) Requisites For The Endoscopes Unit, (c) Chemicals And Requisites Of The Blood Bank, (d) Chemicals For The Instrument To Automatically Analyze Blood", "Medical Disposable and Consumable"),
    ("Healthcare Equipment and Services; Supply Of Surgical Tools For The Dental Medicine Clinic", "Medical Equipment"),
    ("Healthcare Equipment and Services , Healthcare and Medicine; Pact Brushes Sterile Blood Remover And Detergent Enzyme And Rust Remover And A Chemical Indicator For Sterilization", "Medical Disposable and Consumable"),
    ("Healthcare Equipment and Services , Laboratory Equipment and Services; Purchase Of Scientific Equipment For The Project Development Unit Of Microbiology Lab Laboratory Abu Rish Hospital Enlightening For Children", "Laboratory Product"),
    ("Textile, Apparel and Footwear , Healthcare Equipment and Services; Buy Clothes Workers And Patients Required For The Directorate Of Health And Its Units", "Medical Disposable and Consumable"),
    ("Agriculture, Food and Beverages , Healthcare Equipment and Services; The Supply Of Ready-made Meals In Hospital", "Nutrition and Cosmetic"),
    ("Healthcare and Medicine; Public Tender For The Supply Of Tablets And Capsules Drugs", "Pharmaceutical")
]
def classify(desc):
    cl = NaiveBayesClassifier(train)
    classification = cl.classify(desc)
    print classification
    return classification
