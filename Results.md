# Results of T5 model for OOD sorting task
Default number of epochs is 20 unless otherwise specified

| Sort | Strategy | Model | Digits | Rep | P/F | Train | Val | Test | Sep | Inpol Loss | Inpol Acc | Expol Loss | Expol Acc | Batch | Comments | Number of Epochs |
|------|----------|-------|--------|-----|-----|-------|-----|------|-----|------------|-----------|------------|-----------|-------|----------|------------------|
| Asc | Only Finetuning | T5 Base | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 1.4748e-05 | 100 | 0.0074 | 81.7 | 16 |
| Asc | Only Finetuning | T5 Base | 4 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0001 | 99.8 | 0.0652 | 77.6 | 8 |
| Asc | Only Finetuning | T5 Base | 4 | e-based | F | 10K | 1K | 1K | `' '` | 0.00019 | 99.4 | 0.0174 | 64.2 | 8 |
| Asc | Only Finetuning| T5 Base | 4 | Decimal | F | 10K | 1K  | 1K  | `'\|'` |  0.044 | 90.6 | 0.736 | 23.4 | 8 |
| Asc | Only Finetuning | T5 Base | 4 | Decimal | F | 10K| 1K  | 1K  | `'@'` |  0.0461 | 90.6 | 0.7928 | 25 | 8 | | 20 
| Asc | Only Finetuning | T5 Base | 2 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0001 | 99.8 | 1.304 | 0.0 | 16 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0003 | 99.8 | 1.3245 | 0.1 | 16 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 1K | 100 | 100 | `' '` | 0.0174 | 93.0 | 2.3167 | 0.0 | 4 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 1K | 100 | 100 | `','` | 0.0128 | 91.0 | 1.5032 | 0.0 | 4 |
| Asc | Only Finetuning | T5 Base | 2 | Decimal | F | 10K | 1K  | 1K  | `'\|'` |  0.00030 | 100 | 13.683 | 0.0 | 8 |
| Asc | Only Finetuning | T5 Base | 2 | Decimal | F | 10K| 1K  | 1K  | `'@'` |  0.00201 | 99.3 | 14.21 | 0.0| 8 | | 20
| Asc | Only Finetuning | T5 Small | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0005 | 98.5 | 0.1737 | 38.9 | 16 |
| Asc | Only Finetuning | T5 Small | 4 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0007 | 98.5 | 0.2338 | 23.9 | 16 |
| Asc | Only Finetuning | T5 Small | 4 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0686 | 82.6 | 0.899 | 14.9 | 8 |
| Asc | Only Finetuning | T5 Small | 4 | Decimal | F | 10K| 1K  | 1K  | `'@'` |   0.0605 | 86 | 1.246 | 10.9 | 8| |30 
| Asc | Only Finetuning | T5 Small | 2 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0081 | 91.3 | 1.0282 | 0.0 | 16 |
| Asc | Only Finetuning | T5 Small | 2 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0017 | 97.4 | 1.2284 | 0.0 | 16 |
| Asc | Only Finetuning | T5 Small | 2 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0098 | 96.2 | 11.79 | 0.0 | 8 |
| Asc | Only Finetuning | T5 Small | 2 | Decimal | F | 10K| 1K  | 1K  | `'@'` |   0.0055 | 98.2 | 11.09 | 0.0 | 8 | | 30
| Asc | Only Finetuning | T5 Base | 4 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0002 | 99.7 | 0.0131 | 80.6 | 16 || 20
| Asc | Only Finetuning | T5 Small | 4 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0006 | 99.0 | 0.2292 | 2.7 | 16 || 20
| Asc | Only Finetuning | T5 Small | 2 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0267 | 86.7 | 1.3058 | 0.1 | 16 || 20
| Asc | Only Finetuning | T5 Base | 2 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0036 | 97.9 | 1.3130 | 0.2 | 16 || 20
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.0272 | 87.3 | 1.4896 | 13.0 | 4 | Span Length is random
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0382 | 91.6 | 1.0411 | 17.2 | 8 | Span Length is random
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0429 | 90.9 | 1.0272 | 17.3 | 8 | Span Length = 3
| Asc | Span Masking | T5 Base | 4 | e-based | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0001 | 99.9 | 0.0581 | 38.0 | 8 | Span Length is random
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.0093 | 97.8 | 15.1265 | 0.0 | 4 | Span Length is random
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0001 | 100.0 | 11.8078 | 0.0 | 8 | Span Length = 3
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K | 10K</br>1K | `'\|'` | 0.0271 | 92.2 | 2.2388 | 6.4 | 16 | Span Length is random
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 70K</br>10K | 7K</br>1K | 7K</br>1K | `'\|'` | 0.0393 | 88.5 | 1.8637 | 5.6 | 16 | Span Length = 3
| Asc | Span Masking | T5 Small | 2 | Decimal | P</br>F | 60K</br>10K | 6K</br>1K | 6K</br>1K | `'\|'` | 1.7335e-5 | 100.0 | 15.0776 | 0.0 | 16 | Span Length = 4
| Asc | Span Masking | T5 Small | 2 | Decimal | P</br>F | 70K</br>10K | 7K</br>1K | 7K</br>1K | `'\|'` | 0.0006 | 99.9 | 10.4126 | 0.0 | 16 | Span Length = 3
| Asc | Yes/No Classification | T5 Base | 4 | e-based | P</br>F | 10K</br>10K | 1K</br>1K  | 1K</br>1K  | `'\|'` | 9.3154e-05 | 99.8 | 0.5500 | 29.5 | 16 |
| Asc | Yes/No Classification | T5 Base | 4 | Decimal | P</br>F | 10k</br>10k | 1k</br>1K | 1k</br>1K | `' '` | 0.0453 | 88.6 | 0.9451 | 16.0 | 16 |
| Asc | Yes/No Classification | T5 Base | 2 | e-based | P</br>F | 10K</br>10K  | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0001 | 99.9 | 1.6233 | 0.0 | 16 |
| Asc | Yes/No Classification | T5 Base | 2 | Decimal | P</br>F | 10K</br>1K | 1K</br>1K | 1K</br>1K | `' '` | 0.0362 | 88.7 | 8.8804 | 0.0 | 16 |
| Asc | Yes/No Classification | T5 Small | 4 | e-based | P</br>F | 100k</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0008 | 97.9 | 0.2105 | 39.5 | 16 |
| Asc | Yes/No Classification | T5 Small | 2 | e-based | P</br>F | 100k</br>10k | 1k</br>1K | 1k</br>1K | `'\|'` | 0.0014 | 98.8 | 2.0120 | 0.0 | 16 |
| Asc | Number Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.000315 | 99.9 | 13.284 | 0.0 | 4 | Numbers Masked = 3
| Asc | Number Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0385 | 91.7 | 1.045 | 17.2 | 8 | Numbers Masked = 3
| Asc | Number Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0027 | 99 | 12.488 | 0.0 | 8 | Numbers Masked = 3
| Asc | Number Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K | 10K</br>1K | `'\|'` | 0.0379 | 90.8 | 2.07 | 6.5 | 8 | Numbers Masked = 3
| Asc | Digit Masking | T5 Small | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.1029 | 99.3 | 10.0114 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.0284 | 87 | 0.6169 | 23.8 | 16 | Number of Digits Masked = 1 | 30
| Asc | Digit Masking | T5 Small | 2 | Decimal | P</br>F | 1778</br>177 | 178</br>17 | 178</br>17 | `' '` | 1.9313 | 0 | 1.7503 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 1778</br>177 | 178</br>17 | 178</br>17 | `' '` | 0.7809 | 0 | 1.0602 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 2 | Decimal | P</br>F | 3162</br>316 | 316</br>31 | 316</br>31 | `' '` | 0.5321 | 6 | 2.2294 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 3162</br>316 | 316</br>31 | 316</br>31 | `' '` | 1.5405 | 0 | 1.6196 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 5623</br>562 | 562</br>56 | 562</br>56 | `' '` | 0.4567 | 3.5 | 0.6335 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 2 | Decimal | P</br>F | 1000</br>1000 | 100</br>100 | 100</br>100 | `' '` | 0.239 | 42 | 3.8713 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 1000</br>1000 | 100</br>100 | 100</br>100 | `' '` | 0.3691 | 9 | 0.7751 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 10000</br>10000 | 1000</br>1000 | 1000</br>1000 | `' '` | 0.453 | 73.1 | 1.539 | 5.9 | 16 | Number of Digits Masked = 1 | 20
| Asc | Digit Masking | T5 Small | 2 | Decimal | P</br>F | 10000</br>10000 | 1000</br>1000 | 1000</br>1000 | `' '` | 0.1397 | 75.5 | 10.464 | 0 | 16 | Number of Digits Masked = 1 | 20
| Asc | Native Language Digits Representation | T5 Small | 4 | Decimal | F | 10000 | 1000 | 1000 | `' '` | - | - | - | - | 16 | As the model wasn't returning any output, we stopped executing native language number prediction | 20
| Asc | Digit Masking | T5 Base | 2 | Decimal | P</br>F | 10000</br>10000 | 1000</br>1000 | 1000</br>1000 | `' '` | 0.019 | 92.8 | 10.412 | 0 | 16 | Number of Digits Masked = 1 | 20
| Desc | Only Finetuning | T5 Base | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0002 | 99.4 | 0.0259 | 59.5 | 16 |
| Desc | Only Finetuning | T5 Base | 2 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0015 | 98.2 | 1.7185 | 0.0 | 16 |
| Desc | Only Finetuning | T5 Small | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0028 | 91.8 | 0.0373 | 57.7 | 16 |
| Desc | Only Finetuning | T5 Small | 2 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0041 | 95.7 | 1.3578 | 0.0 | 16 |
| Desc | Yes/No Classification | T5 Base | 4 | e-based | P</br>F | 10k</br>10k | 1k</br>1k | 1k</br>1k | `'\|'` | 3.7685e-05 | 99.9 | 0.2506 | 18.0 | 16 |
| Desc | Yes/No Classification | T5 Base | 4 | Decimal | P</br>F | 10k</br>10k | 1k</br>1k | 1k</br>1k | `'\|'` | 0.0485 | 88.0 | 0.9197 | 17.5 | 16 |
| Desc | Yes/No Classification | T5 Base | 2 | e-based | P</br>F | 10k</br>10k | 1k</br>1k | 1k</br>1k | `'\|'` | 0.0011 | 97.9 | 2.4068 | 0.0 | 16 |
| Desc | Yes/No Classification | T5 Small | 4 | e-based | P</br>F | 100k</br>10k | 1k</br>1k | 1k</br>1k | `'\|'` | 0.0011 | 97.2 | 0.2622 | 14.0 | 16 |
| Desc | Yes/No Classification | T5 Small | 2 | e-based | P</br>F | 100k</br>10k | 1k</br>1k | 1k</br>1k | `'\|'` | 0.0029 | 97.8 | 2.5975 | 0.0 | 16 |
| Desc | Digit Masking | T5 Large | 4 | Decimal | P</br>F | 30000</br>30000 | 1000</br>1000 | 1000</br>1000 | `' '` | - | - | - | - | 8 | Memory Error | 10
| Desc | Digit Masking | T5 Small | 4 | Decimal | P</br>F | 10000</br>10000 | 1000</br>1000 | 1000</br>1000 | `' '` | 0.101 | 78 | 10.236 | 0 | 16 | Number of Digits Masked = 1 | 20
| Desc | Digit Masking | T5 Large | 2 | Decimal | P</br>F | 30000</br>30000 | 1000</br>1000 | 1000</br>1000 | `' '` | 0.0807 | 87 | 15.682 | 0 | 8 | Number of Digits Masked = 1 | 10
| Desc | Only Finetuning | T5 Base | 4 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0506 | 89.3 | 1.1345 | 15.4 | 8 | | 20
| Desc | Only Finetuning | T5 Small | 4 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |   0.073 | 81.9 | 1.46 | 9 | 16 | | 30
| Desc | Only Finetuning | T5 Base | 2 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0116 | 95 | 9.21 | 0.0| 8 | | 20
| Desc | Only Finetuning | T5 Small | 2 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |   0.01603 | 95.2 | 9.720 | 0.0 | 16 | |30 
| Desc | Number Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 10K</br>1K  | 10K</br>1K  | `'\|'` |  0.038 | 90.5| 0.910 | 18.9 | 16 |Random number of masks| 20
| Desc | Number Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 10K</br>1K  | 10K</br>1K  | `'\|'` |  7.301 | 100 | 12.806 | 0.0 | 16 | Random number of masks|20
| Desc | Number Masking | T5 Small | 2 | Decimal | P</br>F | 10K</br>10K | 10K</br>1K  | 10K</br>1K  | `'\|'` |  0.000400 | 100 | 9.804 | 0.0 | 16 |Random number of masks|30
| Desc | Number Masking | T5 Small | 4 | Decimal | P</br>F | 10K</br>10K | 10K</br>1K  | 10K</br>1K  | `'\|'` |  0.0573 | 85.8 | 1.442 | 9.4 | 16 |Random number of masks|30
| Desc | Only Finetuning | T5 Large | 4 | ebased | F | 10K| 1K  | 1K  | `'\|'` |  0.0003 | 99.5 | 0.0784 | 42.9 | 4 | | 21 
| Desc | Only Finetuning | T5 Base | 4 | ebased | F | 10K| 1K  | 1K  | `'\|'` |  3.3377e-05 | 99.9 | 0.0846 | 59.8 | 16 | | 20 
| Desc | Only Finetuning | T5 Base | 4 | Decimal | F | 10K| 1K  | 1K  | `'@'` |  0.0497 | 88.1 | 0.9080 | 18.3 | 8 | | 20 
| Desc | Only Finetuning | T5 Base | 2 | Decimal | F | 10K| 1K  | 1K  | `'@'` |  0.00751 | 96.9 | 13.00 | 0.0| 8 | | 20 
| Desc | Only Finetuning | T5 Base | 2 | ebased | F | 10K| 1K  | 1K  | `'\|'` |  0.0002 | 99.8 | 2.0215 | 0.1 | 16 | | 20 
| Desc | Only Finetuning | T5 Small | 4 | ebased | F | 10K| 1K  | 1K  | `'\|'` |  0.0014 | 95.2 | 0.1873 | 45.9| 16 | | 20 
| Desc | Only Finetuning | T5 Small | 4 | Decimal | F | 10K| 1K  | 1K  | `'@'` |  0.06179 | 84.3 | 1.6083 | 10.1 | 8 | | 30 
| Desc | Only Finetuning | T5 Small | 2 | Decimal | F | 10K| 1K  | 1K  | `'@'` |   0.02563 | 93.6 | 10.853 | 0.0 | 8| | 30
| Desc | Only Finetuning | T5 Small | 2 | ebased | F | 10K| 1K  | 1K  | `'\|'` |  0.0070 | 93.1 | 1.4392 | 0.2 | 16 | | 20 
| Desc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 30K</br>10K | 3K</br>1K | 3K</br>1K | `'\|'` | 0.0446 | 91.4 | 1.1801 | 13.4 | 8 | Span Length = 3
| Desc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 30K</br>10K | 3K</br>1K | 3K</br>1K | `'\|'` | 5.5793e-05 | 100.0 | 12.4272 | 0.0 | 16 | Span Length = 3
| Desc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K | 10K</br>1K | `'\|'` | 0.0451 | 85.8 | 2.0066 | 5.8 | 16 | Span Length is random
| Desc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 60K</br>10K | 6K</br>1K | 6K</br>1K | `'\|'` | 0.0532 | 85.1 | 1.4518 | 7.1 | 16 | Span Length = 4
| Desc | Span Masking | T5 Small | 2 | Decimal | P</br>F | 70K</br>10K | 7K</br>1K | 7K</br>1K | `'\|'` | 6.3913e-05 | 100.0 | 10.8221 | 0.0 | 16 | Span Length = 3
| Desc | Only Finetuning | T5 Base | 4 | 10-based | F | 10k | 1k | 1k | `'\|'` | 2.4705e-05 | 100 | 0.0537 | 42.7 | 16 ||20
| Desc | Only Finetuning | T5 Small | 4 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0007 | 99.2 | 0.1582 | 4.3 | 16 ||20
| Desc | Only Finetuning | T5 Base | 2 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0021 | 99.1 | 1.5341 | 0.5 | 16 ||20
| Desc | Only Finetuning | T5 Small | 2 | 10-based | F | 10k | 1k | 1k | `'\|'` | 0.0126 | 94.7 | 2.8978 | 0.0 | 16 ||20

## Span Masking

Take a continuous span of numbers and rearrange them in sorted order keeping the remaining numbers same. This helps the model to sort the numbers.</br>
`Original: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|<extra_id_0>|<extra_id_1>|<extra_id_2>|15|33|47|69`</br>
`label: 43|63|91`</br>
The length of span is mentioned in the comments column. It is 3 for above example.
???

## Yes/No Classification

Classify whether the given list of numbers in the input sentence are correctly sorted into mentioned order.</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 12|15|33|43|47|60|63|69|91`</br>
`label: Yes`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`label: No`</br>

## E-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 e 1 0 e 0|1 e 1 2 e 0|9 e 1 1 e 0`</br>
`label: 1 e 1 2 e 0|4 e 1 3 e 0|9 e 1 1 e 0`
???
## 10e-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 10e1 0 10e0|1 10e1 2 10e0|9 10e1 1 10e0`</br>
`label: 1 10e1 2 10e0|4 10e1 3 10e0|9 10e1 1 10e0`

## 10-based Representation

`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 10 0 1|1 10 2 1|9 10 1 1`</br>
`label: 1 10 2 1|4 10 3 1|9 10 1 1`
???
## Number Masking

`Numbers: 60|12|91`</br>
`Input: The sorted ascending order of 6555|6173|423|108 is 108|<extra_id_0>|<extra_id_1>|<extra_id_2>`</br>
`label: <extra_id_0> 423 <extra_id_1> 6173 <extra_id_2> 6555 <extra_id_3> `
`
???
## Digit Masking

`Numbers: 12 7 33`</br>
`Input: The sorted ascending order of 12 7 33 is 7 <mask_1>2 <mask_2>3`</br>
`label: 1 3`

### Native Language Digit Representation

`Numbers: ?????? ??? ??????` </br>
`Input: Sort in ascending order: ?????? ??? ??????`</br>
`label: ??? ?????? ??????`
???
