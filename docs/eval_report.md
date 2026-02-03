# Final Evaluation Report (Restored Models)

## Summary Table

| Model Version | Rank / Alpha | Avg Judge Score | Status |
| :--- | :--- | :--- | :--- |
| **v13-bis (Baseline)** | 16 / 32 | **3.6 / 5.0** | ✅ **RECOMMENDED** |
| **v14-bis (HighRank)** | 64 / 128 | **2.45 / 5.0** | ❌ **REJECTED** |
| **v16 (AlphaScaling)** | 16 / 16 | 2.51 / 5.0 | ⚠️ STABLE BUT COLD |

---

## Detailed Findings: v14-bis (High-Rank)
The High-Rank model (Rank 64) achieved the lowest validation loss (0.65) but suffered from **catastrophic unlearning of input grounding**.

### 🚨 Critical Clinical Risks
1. **Systemic Hallucinations**: Fabricated specific client ages (e.g., "Olet 40-vuotias mies") in 20% of samples without any age data in the input.
2. **False Quantifications**: Robotic insistence on numbers ("100% varma", "120 desibelin melu").
3. **Pseudo-Clinical Terminology**: Invented terms like "iltakammo" (night dread) and "2. tason ahdistus" (level 2 anxiety) which do not exist in Finnish clinical practice.
4. **Context Drift**: In Sample 36, the model drifted from a discussion about dieting to "the best moment of the week."

---

## Detailed Findings: v13-bis (Baseline)
The baseline model remains the most reliable for clinical use.

### ✅ Strengths
- **Safe Grounding**: Never fabricated client demographics.
- **Natural Language**: Higher score in "Lämmin yleiskieli" (warm general language).
- **Consistent Structure**: Follows therapeutic boundaries well.

### ⚠️ Areas for Improvement
- **Brevity**: Sometimes too concise.
- **Labeling**: Occasional tendency to label emotions (e.g., "This is an imagined threat") rather than explore them.

---

## Final Recommendation
Revert to the **v13 (Rank 16)** architecture. The next training iteration should focus on **increasing dataset diversity** and **psychoeducational depth** rather than increasing model rank.