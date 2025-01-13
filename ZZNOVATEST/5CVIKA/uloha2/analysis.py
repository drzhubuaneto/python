from collections import Counter

from src.defaults import DEFAULT_DIASTOLIC, DEFAULT_SYSTOLIC, DEFAULT_TEMPERATURE


def calculate_stats(values):
    return {
        "max": max(values),
        "min": min(values),
        "mean": sum(values) / len(values) if values else 0
    }

def analyze_temperatures(patients):
    temperatures = [p["teplota"] for p in patients]
    return calculate_stats(temperatures)

def analyze_blood_pressure(patients):
    systolic = [p["tlak"]["systolicky"] for p in patients]
    diastolic = [p["tlak"]["diastolicky"] for p in patients]

    return {
        "systolic": {
            **calculate_stats(systolic),
            "offset_from_default": {
                "max": max(systolic) - DEFAULT_SYSTOLIC,
                "min": min(systolic) - DEFAULT_SYSTOLIC
            }
        },
        "diastolic": {
            **calculate_stats(diastolic),
            "offset_from_default": {
                "max": max(diastolic) - DEFAULT_DIASTOLIC,
                "min": min(diastolic) - DEFAULT_DIASTOLIC
            }
        }
    }

def categorize_by_gender(patients):
    gender_counts = Counter(p["pohlavi"] for p in patients)
    return {"Muž": gender_counts.get("Muž", 0), "Žena": gender_counts.get("Žena", 0)}

def unique_diagnoses(patients):
    diagnoses = Counter(p["diagnoza"] for p in patients)
    return dict(diagnoses)
