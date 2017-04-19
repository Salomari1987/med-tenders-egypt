#!/usr/bin/env python

from classifier import classify

test_cases = [
    {"text":"Supply And Erection Of 60 Human Simulators For The Faculty Of Dental Medicine", "label": "Medical Equipment"},
    {"text":"Supply Of Medical Requisites For The Medical Treatment Dept", "label": "Medical Equipment"},
    {"text":"Supply Of Requirements Of The Employees Hospital In Nagee Hamadi Of Medicines & Medical Requisites.", "label": "Pharmaceutical"},
    {"text":"Supply Of Medical Instruments & Requisites.", "label": "Medical Equipment"},
    {"text":"Supply Of An Instrument To Digitally Develop X Ray Photos With Related Accessories", "label": "Laboratory Product"},
    {"text":"Supply Of A Radio Active Material Fia - Fdg For The Pec - Ct Preston Diagnostic X Ray Instrument.", "label": "Laboratory Product"},
    {"text":"Supply Of Requisites For The Interactive Brain X Ray Unit.", "label": "Medical Disposable and Consumable"},
    {"text":"Supply Of X-ray Image Treatment Devices", "label": "Medical Equipment"},
    {"text":"Supply Of Chemicals For The Laboratories Dept", "label": "Laboratory Product"},
    {"text":"Supply Of Medicines And Medical Requisites For The Company~s Hospital For One Year", "label": "Pharmaceutical"},
    {"text":"Supply Of (a) Requisites Of The X Ray Division, (b) Requisites For The Endoscopes Unit, (c) Chemicals And Requisites Of The Blood Bank, (d) Chemicals For The Instrument To Automatically Analyze Blood", "label": "Medical Disposable and Consumable"},
    {"text":"Supply Of Surgical Tools For The Dental Medicine Clinic", "label": "Medical Equipment"},
    {"text":"Pact Brushes Sterile Blood Remover And Detergent Enzyme And Rust Remover And A Chemical Indicator For Sterilization", "label": "Medical Disposable and Consumable"},
    {"text":"Purchase Of Scientific Equipment For The Project Development Unit Of Microbiology Lab Laboratory Abu Rish Hospital Enlightening For Children", "label": "Laboratory Product"},
    {"text":"Buy Clothes Workers And Patients Required For The Directorate Of Health And Its Units", "label": "Medical Disposable and Consumable"},
    {"text":"The Supply Of Ready-made Meals In Hospital", "label": "Nutrition and Cosmetic"},
    {"text":"Public Tender For The Supply Of Tablets And Capsules Drugs", "label": "Pharmaceutical"},
    {"text":"Develop And Raise The Efficiency Of A Number (11) Health Eastern Region Unit", "label": "Other"},
    {"text":"Complete The Development Of Health Center For Reproductive Bareicheh Egypt Ismailia", "label": "Other"},
    {"text":"Provide Information Services Field To Make Sure The Data Provided Dealers With The Health Fund", "label": "Other"},
    {"text":"Medical Supplies", "label": "Medical Disposable and Consumable"},
    {"text":"Supply of food and beverages and meals for hospital workers", "label": "Nutrition and Cosmetic"},
    {"text":"Construction Of Three Medical Centers In Northern Sinai", "label": "Other"},
    {"text":"Supply of Drugs and Vaccines", "label": "Pharmaceutical"},
    {"text":"Supply of medical supplies and materials", "label": "Medical Disposable and Consumable"}
]


def test_classifier(label):
    results = {
        "FP": 0,
        "TP": 0,
        "FN": 0,
        "TN": 0
    }
    for i, e in enumerate(test_cases):
        result = classify(e["text"])
        if result == e["label"] and e["label"] == label:
            results["TP"] += 1
        elif result != e["label"] and e["label"] == label:
            results["FP"] += 1
        elif result != e["label"] and e["label"] != label:
            results["FN"] += 1
        elif result == e["label"] and e["label"] != label:
            results["TN"] += 1
    return results

def test_classifier_other(label):
    results = {
        "FP": 0,
        "TP": 0,
        "FN": 0,
        "TN": 0
    }
    for i, e in enumerate(test_cases):
        result = classify(e["text"])
        if result == e["label"] and e["label"] != label:
            results["TP"] += 1
        elif result != e["label"] and e["label"] != label:
            results["FP"] += 1
        elif result != e["label"] and e["label"] == label:
            results["FN"] += 1
        elif result == e["label"] and e["label"] == label:
            results["TN"] += 1
    return results

def calculate_accuracy(results):
    recall = float(results["TP"])/(results["TP"] + results["FN"])
    precision = float(results["TP"])/(results["TP"] + results["FP"])

    return float((2 * recall)/(recall + precision))

def main():

    ME = calculate_accuracy(test_classifier("Medical Equipment")) * 100
    PH = calculate_accuracy(test_classifier("Pharmaceutical")) * 100
    LP = calculate_accuracy(test_classifier("Laboratory Product")) * 100
    MDAC = calculate_accuracy(test_classifier("Medical Disposable and Consumable")) * 100
    NC = calculate_accuracy(test_classifier("Nutrition and Cosmetic")) * 100
    Other = calculate_accuracy(test_classifier_other("Other")) * 100
    Overall = (ME + PH + LP + MDAC + NC + Other) / 6

    accuracy = \
        """The F-MEASURE (2*recall/(recall+precision) accuracy of the Nayev Bayes classifier for:\n
        Medical Equipment: {ME}% \n
        Pharmaceutical: {PH}%\n
        Laboratory Product: {LP}%\n
        Medical Disposable and Consumable: {MDAC}%\n
        Nutrition and Cosmetic:{NC}%\n
        Other: {Other} %
        and, Overall {Overall}%""".format(ME = ME, PH = PH, LP = LP, MDAC=MDAC, NC = NC, Other = Other, Overall = Overall)
    print accuracy
    return accuracy

main()
