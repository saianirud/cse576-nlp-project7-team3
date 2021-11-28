| Sort | Strategy | Model | Digits | Rep | P/F | Train | Val | Test | Batch | Sep | Inpol Loss | Inpol Acc | Expol Loss | Expol Acc | Comments |
|------|----------|-------|--------|-----|-----|-------|-----|------|-------|-----|------------|-----------|------------|-----------|---------|
| Asc | E-based | T5 Base | 4 | e-based | F | 10K | 1K | 1K | 8 | `'\|'` | 7.9491e-05 | 99.8 | 0.1284 | 79.0 |
| Asc | E-based | T5 Base | 2 | e-based | F | 10K | 1K | 1K | 4 | `' '` | 0.0011 | 98.5 | 2.6851 | 0.0 |
| Asc | E-based | T5 Base | 2 | e-based | F | 1K | 100 | 100 | 4 | `' '` | 0.0174 | 93.0 | 2.3167 | 0.0 |
| Asc | E-based | T5 Base | 2 | e-based | F | 1K | 100 | 100 | 4 | `','` | 0.0128 | 91.0 | 1.5032 | 0.0 |
| Asc | E-based | T5 Small | 4 | e-based | F | 10K | 1K | 1K | 16 | `'\|'` | 0.0007 | 98.5 | 0.2338 | 23.9 |
| Asc | E-based | T5 Small | 2 | e-based | F | 10K | 1K | 1K | 16 | `'\|'` | 0.0017 | 97.4 | 1.2284 | 0.0 |
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 4 | `' '` | 0.0272 | 87.3 | 1.4896 | 13.0 | Span Length is random for each sample
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 8 | `'\|'` | 0.0382 | 91.6 | 1.0411 | 17.2 | Span Length is random for each sample
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 8 | `'\|'` | 0.0429 | 90.9 | 1.0272 | 17.3 | Span Length = 3
| Asc | Span Masking | T5 Base | 4 | e-based | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 8 | `'\|'` | 0.0001 | 99.9 | 0.0581 | 38.0 | Span Length is random for each sample
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 4 | `' '` | 0.0093 | 97.8 | 15.1265 | 0.0 | Span Length is random for each sample
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | 8 | `'\|'` | 0.0001 | 100.0 | 11.8078 | 0.0 | Span Length = 3
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K | 10K</br>1K | 16 | `'\|'` | 0.0271 | 92.2 | 2.2388 | 6.4 | Span Length is random for each sample
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 70K</br>10K | 7K</br>1K | 7K</br>1K | 16 | `'\|'` | 0.0393 | 88.5 | 1.8637 | 5.6 | Span Length = 3

</br></br>
## Span Masking
Take a continuous span of numbers and rearrange them in sorted order keeping the remaining numbers same. This helps the model to sort the numbers.</br>
`Original: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|<extra_id_0>|<extra_id_1>|<extra_id_2>|15|33|47|69`</br>
`label: 43|63|91`</br>
The length of span is mentioned in the comments column. It is 3 for above example.

</br></br>
## E-based Representation
`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 e 1 0 e 0|1 e 1 2 e 0|9 e 1 1 e 0`</br>
`label: 1 e 1 2 e 0|4 e 1 3 e 0|9 e 1 1 e 0`