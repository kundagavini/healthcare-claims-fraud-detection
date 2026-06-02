# Risk Model Methodology

## Overview

This project implements a **composite risk stratification model** modeled after
approaches used in Medicare Advantage care management programs. The score draws
on four evidence-based domains used in commercial and CMS risk tools.

---

## Domain 1 — Clinical Complexity (0–40 pts)

| Signal | Points | Rationale |
|--------|--------|-----------|
| Each chronic condition | 6 pts each (max 40) | Multimorbidity is the strongest predictor of high utilization |
| High-acuity diagnosis (CHF, AFib, CKD) | +10 pts | These conditions have high readmission and cost rates |
| Age 65–74 | +2 pts | Age-related risk multiplier |
| Age 75+ | +5 pts | Frailty and polypharmacy risk |

**Clinical basis**: Charlson Comorbidity Index (CCI), HCC risk adjustment model

---

## Domain 2 — Utilization Intensity (0–30 pts)

| Flag | Points | Threshold |
|------|--------|-----------|
| High ED use | 10 pts | ≥3 ED visits in measurement year |
| High inpatient use | 12 pts | ≥2 inpatient stays in measurement year |
| High total cost | 5 pts | ≥$20,000 total claims cost YTD |
| No PCP visit | 5 pts | ≥365 days since last primary care visit |

**Clinical basis**: LACE Index, HOSPITAL Score for readmission risk

---

## Domain 3 — Social Risk / SDOH (0–15 pts)

| Signal | Points | Rationale |
|--------|--------|-----------|
| Dual-eligible (Medicare + Medicaid) | 8 pts | Strongest social risk proxy in claims data |
| Non-English preferred language | 4 pts | Health literacy and care coordination barrier |
| Enrollment gap | 3 pts | Indicates coverage instability |

**Clinical basis**: CMS Accountable Health Communities model, AHRQ SDOH framework

---

## Domain 4 — Care Gap Burden (0–15 pts)

| Signal | Points |
|--------|--------|
| Each open HEDIS measure | 3 pts (max 5 gaps = 15 pts) |

Care gaps measured:
- HbA1c Testing (diabetes)
- Breast Cancer Screening
- Colorectal Cancer Screening
- Annual Wellness Visit
- Controlling High Blood Pressure
- Statin Use (diabetes/CVD)
- Medication Adherence
- Diabetic Eye Exam

---

## Risk Tier Thresholds

| Tier | Score | Population % | Interpretation |
|------|-------|-------------|----------------|
| High | ≥50 | ~24% | Active care management needed |
| Medium | 25–49 | ~49% | Monitoring and coordination |
| Low | <25 | ~27% | Preventive focus |

Thresholds are calibrated to identify the top 20–25% of members by cost and
utilization risk — consistent with industry benchmarks for care management
program capacity.

---

## Limitations (for real-world use)

1. **No predictive validation** — the model uses rule-based scoring, not a
   trained ML model. Real deployment should be validated against 12-month
   prospective outcomes.
2. **Synthetic data** — prevalence rates are approximated from national
   estimates, not a real member population.
3. **Claims-only** — does not incorporate EHR, lab, or patient-reported data.
4. **Static thresholds** — cut points should be recalibrated annually.

---

## References

- Charlson ME et al. *A new method of classifying prognostic comorbidity.* J Chronic Dis. 1987.
- van Walraven C et al. *Derivation and validation of an index to predict early death or unplanned readmission after hospital discharge.* CMAJ. 2010. (LACE Index)
- CMS HCC Risk Adjustment Model: https://www.cms.gov/medicare/health-plans/medicareadvtgspecratestats/risk-adjustors
- AHRQ SDOH Framework: https://www.ahrq.gov/sdoh/index.html
