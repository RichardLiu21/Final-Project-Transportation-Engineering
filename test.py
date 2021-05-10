# Alternative test

alt1 = Alternative('alt1', 5, 180000, 10000, 0)

alt2 = Alternative('alt2', 5, 180000, 10000, 0, {'lighting': 2000, 'roofing': 3000})

print(alt1)

print(alt2)

# Result of Alternative test
# Alternative: alt1 
# Service Life: 5 years
# Initial Cost: $180,000.00
# Annual Maintenance Cost: $10,000.00
# Salvage Value: $0.00

# Alternative: alt2
# Service Life: 5 years
# Initial Cost: $180,000.00
# Annual Maintenance Cost: $10,000.00
# Salvage Value: $0.00
# roofing: $3,000.00
# lighting: $2,000.00

# Economics Analysis Test

econ = Economic_Analysis([alt1, alt2], 0.10)

print(econ)

# Result of Economics Analysis Test
# Alternatives Analyzed:2
# 1: alt1
# 2: alt2

# Factors Test

print('SPPWF: ', econ.SPPWF(10))
print('SPCAF: ', econ.SPCAF(10))
print('CRF: ', econ.CRF(10))
print('USPWF: ', econ.USPWF(10))
print('USCAF: ', econ.USCAF(10))
print('USSFF: ', econ.USSFF(10))

# Result of Factors Test

# ('SPPWF: ', 0.3855432894295314)
# ('SPCAF: ', 2.5937424601000023)
# ('CRF: ', 0.16274539488251152)
# ('USPWF: ', 6.144567105704685)
# ('USCAF: ', 15.937424601000023)
# ('USSFF: ', 0.06274539488251152)

# Present Worth Test

print(econ.present_worth(alt1))

# Result of Present Worth Test

# 217907.867694

# Present Worth Method Test

alt3 = Alternative('alt3', 10, 10000, 2000, 2500)

alt4 = Alternative('alt4', 10, 12000, 1600, 3000)

econ2 = Economic_Analysis([alt3, alt4], 0.10)

print(econ2.present_worth_method())

# Result of Present Worth Method Test

# Best Alternative: alt4
# Cost: $20,674.68

# Annual Cost Test

print(econ2.annual_cost(alt4))

# Result of Annual Cost Test

# 3364.70855394

# Annual Cost Method Test

alt5 = Alternative('alt5', 15, 75000, 3000, 45000, {'wetland rehab': 7500, 'roadway lighting': 1500})

alt6 = Alternative('alt6', 15, 125000, 2000, 25000, {'wetland rehab': 2500, 'roadway lighting': 2500})

econ3 =Economic_Analysis([alt5, alt6], 0.10)

print(econ3.annual_cost_method())

# Result of Annual Cost Method Test

# Best Alternative: alt5
# Cost: $20,444.21

# Benefit-Cost Test

alt7 = Alternative('alt7', 5, 180000, 10000, 0)

alt8 = Alternative('alt8', 30, 1550000, 0, 0)

econ4 = Economic_Analysis([alt7, alt8], 0.10)

print(econ4.benefit_cost_method({'alt7': 3630600, 'alt8': 1790100}))

# Result of Benefit-Cost Test

# BC Ratio: 17.21
# Best Alternative: alt8


