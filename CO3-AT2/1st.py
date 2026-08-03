import numpy as np
exercise = np.array([10,15,20,25,30,35,40,45,50,55])
bmi = np.array([32,31,30,29,28,27,26,25,24,23])
bp = np.array([150,148,145,142,138,134,130,126,122,118])
print("Mean Blood Pressure:", np.mean(bp))
print("Standard Deviation:", np.std(bp, ddof=1))
print("Covariance (Exercise, BP):", np.cov(exercise, bp)[0,1])
print("Covariance (BMI, BP):", np.cov(bmi, bp)[0,1])
corr_ex = np.corrcoef(exercise, bp)[0,1]
corr_bmi = np.corrcoef(bmi, bp)[0,1]
print("Correlation (Exercise, BP):", corr_ex)
print("Correlation (BMI, BP):", corr_bmi)
if abs(corr_ex) > abs(corr_bmi):
    print("Exercise is more strongly associated with Blood Pressure.")
else:
    print("BMI is more strongly associated with Blood Pressure.")
print("\nHealthcare Interventions:")
print("- Encourage regular exercise")
print("- Promote healthy diet")
print("- Weight management")
print("- Regular BP checkups")