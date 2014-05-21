import sys

paths = ['..\..\common-scripts\\']

for path in paths:
    if not(path in sys.path):
        sys.path.append(path)
        
	