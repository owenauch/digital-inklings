import sys

with open(sys.argv[1], 'r') as fh:
    reader = fh.readlines()
    lines = []
    footnote_count = 0
    footnotes = {}
    for line in reader:
        text = line.split('{FOOTNOTE: ')
        if len(text) > 1:
            footnote_count += 1
            footnote = text[1].split('}')
            footnote_text = footnote[0]
            footnotes[footnote_count] = footnote_text
            final_line = f"{text[0]}<sup>[{footnote_count}](#{footnote_count})</sup>{footnote[1]}"
            lines.append(final_line)
        else:
            lines.append(line)

with open(sys.argv[1], 'w') as fh:

    for line in lines:
        fh.write(f"{line}")

    fh.write("\n#### Footnotes\n")
    for key, value in footnotes.items():
        fh.write(f'\n<a name="{key}">{key}</a>. {value}\n')