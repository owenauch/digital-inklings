#!/usr/bin/python3
import sys

with open(sys.argv[1], 'r') as fh:
    reader = fh.readlines()
    lines = []
    footnotes = []
    footnote_count = 1
    for line in reader:
        if ("[F]" in line):
            footnotes.append(line.split("[F]")[1])
        else:
            split_text = line.split("[f]")
            edited_line = ""
            # loop through all but last section
            for section in split_text[:-1]:
                edited_line += f'{section}<sup id="ref-{footnote_count}">[{footnote_count}](#{footnote_count})</sup>'
                footnote_count += 1
            edited_line += split_text[-1]
            lines.append(edited_line)
    
    if (footnote_count != len(footnotes) + 1):
        raise ValueError

with open(sys.argv[1], 'w') as fh:
    for line in lines:
        fh.write(f"{line}")

    fh.write("\n#### Footnotes\n")
    for idx, footnote in enumerate(footnotes):
        fh.write(f'\n<a name="{idx}">[{idx}](#ref-{idx})</a>.{footnote}\n')