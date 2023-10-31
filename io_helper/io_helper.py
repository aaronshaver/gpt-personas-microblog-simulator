def read_file(path):
    with open(path, 'r') as f:
        return ''.join(f.readlines())