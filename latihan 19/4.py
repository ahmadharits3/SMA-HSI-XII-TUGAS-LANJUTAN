import re
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
print(re.findall(r'\w+g', kalimat))
# Output: ['Kucing', 'anjing', 'burung']
