#! /usr/bin/env python
from SQLFactExtractor import * 

extractor = SQLFactExtractor(sys.stdin, False)
print(json.dumps(extractor.extract_file()))
