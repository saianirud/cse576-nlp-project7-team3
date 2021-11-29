| Sort | Strategy | Model | Digits | Rep | P/F | Train | Val | Test | Sep | Inpol Loss | Inpol Acc | Expol Loss | Expol Acc | Batch | Comments |
|------|----------|-------|--------|-----|-----|-------|-----|------|-----|------------|-----------|------------|-----------|-------|---------|
| Asc | Only Finetuning | T5 Base | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 1.4748e-05 | 100 | 0.0074 | 81.7 | 16 |
| Asc | Only Finetuning | T5 Base | 4 | e-based | F | 10K | 1K | 1K | `'\|'` | 7.9491e-05 | 99.8 | 0.1284 | 79.0 | 8 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 10K | 1K | 1K | `' '` | 0.0011 | 98.5 | 2.6851 | 0.0 | 4 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 1K | 100 | 100 | `' '` | 0.0174 | 93.0 | 2.3167 | 0.0 | 4 |
| Asc | Only Finetuning | T5 Base | 2 | e-based | F | 1K | 100 | 100 | `','` | 0.0128 | 91.0 | 1.5032 | 0.0 | 4 |
| Asc | Only Finetuning | T5 Small | 4 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0007 | 98.5 | 0.2338 | 23.9 | 16 |
| Asc | Only Finetuning | T5 Small | 4 | 10e-based | F | 10k | 1k | 1k | `'\|'` | 0.0005 | 98.5 | 0.1737 | 38.9 | 16 |
| Asc | Only Finetuning | T5 Small | 2 | e-based | F | 10K | 1K | 1K | `'\|'` | 0.0017 | 97.4 | 1.2284 | 0.0 | 16 |
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.0272 | 87.3 | 1.4896 | 13.0 | 4 | Span Length is random
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0382 | 91.6 | 1.0411 | 17.2 | 8 | Span Length is random
| Asc | Span Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0429 | 90.9 | 1.0272 | 17.3 | 8 | Span Length = 3
| Asc | Span Masking | T5 Base | 4 | e-based | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0001 | 99.9 | 0.0581 | 38.0 | 8 | Span Length is random
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `' '` | 0.0093 | 97.8 | 15.1265 | 0.0 | 4 | Span Length is random
| Asc | Span Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K | 1K</br>1K | `'\|'` | 0.0001 | 100.0 | 11.8078 | 0.0 | 8 | Span Length = 3
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K | 10K</br>1K | `'\|'` | 0.0271 | 92.2 | 2.2388 | 6.4 | 16 | Span Length is random
| Asc | Span Masking | T5 Small | 4 | Decimal | P</br>F | 70K</br>10K | 7K</br>1K | 7K</br>1K | `'\|'` | 0.0393 | 88.5 | 1.8637 | 5.6 | 16 | Span Length = 3
| Asc | Yes/No Classification | T5 Base | 4 | e-based | P</br>F | 10K</br>10K | 1K</br>1K  | 1K</br>1K  | `'\|'` | 99.8 | 9.3154e-05 | 0.5500 | 29.5 | 16 |
| Asc | Yes/No Classification | T5 Base | 2 | e-based | P</br>F | 10K</br>10K  | 1K</br>1K | 1K</br>1K | `'\|'` | 99.9 | 0.0001 | 1.6233 | 0.0 | 16 |
| Asc | Yes/No Classification | T5 Base | 2 | Decimal | P</br>F | 1K</br>1K | 1K</br>1K | 1K</br>1K | `' '` | 0.0362 | 88.7 | 8.8804 | 0.0 | 16 |
| Asc | Yes/No Classification | T5 Small | 4 | e-based | P</br>F | 100k</br>10K | 1K</br>1K  | 1K</br>1K  | `'\|'` | 0.0008 | 97.9 | 0.2105 | 39.5 | 16 |
| Asc | Number Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K  | 1K</br>1K  | `' '` |  0.000315 | 99.9 | 13.284 | 0.0 | 4 | Numbers Masked = 3
| Asc | Only Finetuning| T5 Base | 4 | Decimal | F | 10K | 1K  | 1K  | `'\|'` |  0.044 | 90.6 | 0.736 | 23.4 | 8 |
| Asc | Number Masking | T5 Base | 4 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K  | 1K</br>1K  | `'\|'` |  0.0385 | 91.7 | 1.045 | 17.2 | 8 | Numbers Masked = 3
| Asc | Only Finetuning | T5 Base | 2 | Decimal | F | 10K | 1K  | 1K  | `'\|'` |  0.00030 | 100 | 13.683 | 0.0 | 8 |
| Asc | Number Masking | T5 Base | 2 | Decimal | P</br>F | 10K</br>10K | 1K</br>1K  | 1K</br>1K  | `'\|'` |  0.0027 | 99 | 12.488 | 0.0 | 8 | Numbers Masked = 3
| Asc | Only Finetuning | T5 Small | 4 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0686 | 82.6 | 0.899 | 14.9 | 8 |
| Asc | Number Masking | T5 Small | 4 | Decimal | P</br>F | 100K</br>10K | 10K</br>1K  | 10K</br>1K  | `'\|'` |  0.0379 | 90.8 | 2.07 | 6.5 | 8 | Numbers Masked = 3
| Asc | Only Finetuning | T5 Small | 2 | Decimal | F | 10K| 1K  | 1K  | `'\|'` |  0.0098 | 96.2 | 11.79 | 0.0 | 8 |



## Span Masking
Take a continuous span of numbers and rearrange them in sorted order keeping the remaining numbers same. This helps the model to sort the numbers.</br>
`Original: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|43|63|91|15|33|47|69`</br>
`Input: The sorted ascending order of 60|12|91|43|63|15|33|47|69 is 60|12|<extra_id_0>|<extra_id_1>|<extra_id_2>|15|33|47|69`</br>
`label: 43|63|91`</br>
The length of span is mentioned in the comments column. It is 3 for above example.

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

## 10e-based Representation
`Numbers: 60|12|91`</br>
`Input: Sort in ascending order: 6 10e1 0 10e0|1 10e1 2 10e0|9 10e1 1 10e0`</br>
`label: 1 10e1 2 10e0|4 10e1 3 10e0|9 10e1 1 10e0`

## Number Masking 
`Numbers: 60|12|91`</br>
`Input: The sorted ascending order of 6555|6173|423|108 is 108|<extra_id_0>|<extra_id_1>|<extra_id_2>`</br>
`label: 423|6173|6555`






