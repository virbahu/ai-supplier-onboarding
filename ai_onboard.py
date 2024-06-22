import numpy as np
WEIGHTS = {'financial_check': 0.25, 'quality_cert': 0.2, 'capacity_check': 0.15, 'compliance': 0.15, 'references': 0.1, 'sustainability': 0.15}
TARGETS = {'financial_check': 80, 'quality_cert': 100, 'capacity_check': 90, 'compliance': 100, 'references': 80, 'sustainability': 70}
def score_onboarding_score(entity_data):
    scores = {{}}
    for metric, actual in entity_data.items():
        if metric not in TARGETS: continue
        target = TARGETS[metric]
        if metric in set():
            scores[metric] = round(min(100, max(0, (target/max(actual, 0.01))*100)), 1)
        else:
            scores[metric] = round(min(100, max(0, (actual/target)*100)), 1)
    weighted = sum(scores.get(k, 0)*w for k, w in WEIGHTS.items())
    grade = "A+" if weighted >= 95 else "A" if weighted >= 85 else "B" if weighted >= 75 else "C" if weighted >= 60 else "D"
    return {{"scores": scores, "weighted": round(weighted, 1), "grade": grade}}
if __name__=="__main__":
    data = {'financial_check': 75, 'quality_cert': 100, 'capacity_check': 85, 'compliance': 95, 'references': 70, 'sustainability': 65}
    r = score_onboarding_score(data)
    print(f"Grade: {{r['grade']}} ({{r['weighted']}})")
    for k,v in r["scores"].items(): print(f"  {{k}}: {{v}}")
