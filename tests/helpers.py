from os import path


def get_html_from_file(named):
    file_path = path.abspath(path.join('data', named + '.html'))
    with open(file_path, 'r') as f:
        return f.read()
