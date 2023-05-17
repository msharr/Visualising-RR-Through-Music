# musicRR

An alternative representation of RR peak data in terms of musical notation.

## Prerequisite

Download Lilypond from https://lilypond.org/download.html and make sure that the default program for running `.ly` files is set to Lilypond.

## Running the program

Once the program has been installed, run `gui.py`.

Enter the parameters:

`Time` - Format is HH:mm (24 hour time)

`Date` - Format is dd/mm/yyyy

`Tuning Level` - Maximum percentage difference between the BPM of two bars before they are categorised differently. Value is between 0 - 1

`Exclusion Duration` - Excludes bars below value in seconds. Off by default as useful information may be excluded - use with caution.

`Min Tempo` & `Max Tempo` - Min Tempo < x < Max Tempo, heart rates (BPMs) below min tempo and above max tempo are excluded.

## Data format

Place data in a text file in the same format as below. Length is capped at 15000 due to a limitation with Lilypond.

```
656
727
688
688
648
773
695
625
672
687
633
688
711
726
586
672
680
711
695
672
687
```
