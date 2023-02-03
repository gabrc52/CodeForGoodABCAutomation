"""
Data equivalences

The keys are the old one (the one to replace)
And the values are the new ones (the ones to replace WITH)

If a key corresponds to multiple values, it means that they 
should be summed

If a key isn't found, then drop it

(because the collapsed version wasn't found in the older dataset
so only the full version could be downloaded)
"""

equivalences = {
    # Race to race (collapsed)
    f'SE_A04001_00{x}': f'SE_B04001_00{x}'
    for x in range(1, 10)
} | {
    # Households by income to collapsed version

    # Households
    'SE_A14001_001': 'SE_B14001_001',

    # Households: [0, $25K)
    'SE_A14001_002': 'SE_B14001_002',
    'SE_A14001_003': 'SE_B14001_002',
    'SE_A14001_004': 'SE_B14001_002',
    'SE_A14001_005': 'SE_B14001_002',

    # Households: [$25K, $50K)
    'SE_A14001_006': 'SE_B14001_003',
    'SE_A14001_007': 'SE_B14001_003',
    'SE_A14001_008': 'SE_B14001_003',
    'SE_A14001_009': 'SE_B14001_003',
    'SE_A14001_010': 'SE_B14001_003',

    # Households: [$50K, $75K)
    'SE_A14001_011': 'SE_B14001_004',
    'SE_A14001_012': 'SE_B14001_004',

    # Households: [$75K, $100K)
    'SE_A14001_013': 'SE_B14001_005',

    # Households: 3 figure salary
    'SE_A14001_014': 'SE_B14001_006',
    'SE_A14001_015': 'SE_B14001_006',
    'SE_A14001_016': 'SE_B14001_006',
    'SE_A14001_017': 'SE_B14001_006',
}
