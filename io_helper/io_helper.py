import re


def file_to_string(path):
    with open(path, 'r') as f:
        return ''.join(f.readlines())


def minify_string(s):
    s = s.replace('  ', ' ')
    s = s.replace('\n\n', '\n')
    return s


# save tokens (and money) by compressing the system and user prompt text;
# removes string sequences that mostly serve human readers
def minify_string(s):
    s = re.sub(r' +', ' ', s)
    s = re.sub(r'\n+', '\n', s)
    s = re.sub(r'; ', ';', s)
    s = re.sub(r', ', ',', s)
    s = re.sub(r': ', ':', s)
    return s
