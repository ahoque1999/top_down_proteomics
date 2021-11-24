20140926_F_EV_Sisl-SAX-fr3_ETD6_ms2.msalign
```
Henry
4/11/21

from Dave: david.tabb@pasteur.fr
raw file converted to mzML using msConvert
mzML converted to ms2.msalign file using TopFD 1.4.9 
```

ETD-TopPIC.tsv
```
Henry
4/11/21

from Dave: david.tabb@pasteur.fr
ms2.msalign file converted to prsm (prteoform spectrum match) file in tsv format using TopPIC 1.4.13
prsm in tsv format converted to Proforma-formatted prsm table in tsv format using developing C# ProForma reformatter
```

extracted_ETD-TopPIC.tsv
```
python.exe .\extract_relevant_columns_from_TopPIC.py .\ETD-TopPIC.tsv
17/11/21
Python 3.8.3

we only need prsm from fraction 3, since we only have ms2 files for fr3
also we only need column 2, 3, 5 which are scan number, charge and annotation respectively
scan number will be used as master key to merge with ms2 file
```

annotated_20140926_F_EV_Sisl-SAX-fr3_ETD6_ms2_using_extracted_ETD-TopPIC.msp
```
python.exe .\annotate_ms2_using_toppic.py .\extracted_ETD-TopPIC.tsv .\20140926_F_EV_Sisl-SAX-fr3_ETD6_ms2.msalign 
17/11/21
Python 3.8.3

produces a file format similar to msp
remember to name it .msp so it is properly imported by spectrast
using annotations from the TopPIC file and peaks from ms2 file
uses scan number as master key for merging
```

