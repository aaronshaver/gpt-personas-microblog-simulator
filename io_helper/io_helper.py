def file_to_string(path):
    with open(path, 'r') as f:
        return ''.join(f.readlines())