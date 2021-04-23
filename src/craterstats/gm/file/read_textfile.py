#  Copyright (c) 2021, Greg Michael
#  Licensed under BSD 3-Clause License. See LICENSE.txt for details.

from . import file_exists

def read_textfile(filename,n_lines=-1,ignore_blank=False,ignore_hash=False,strip=None,as_string=False):
    '''

    :param filename: full filepath
    :param n_lines: number of lines to read (all, if omitted)
    :param ignore_blank: ignore blank lines
    :param ignore_hash: ignore # lines
    :param strip: remove trailing comments after strip symbol (e.g. ';')
    :param as_string: concatenate into single string, jioned with '\n'
    :return: file contents as list of strings or single string
    '''

    if not file_exists(filename) :
        return None

    with open(filename, 'r', encoding='utf-8-sig') as file: # encoding='utf-8-sig' removes BOM if present
        if n_lines !=-1:
            s=[]
            for i in range(n_lines): s.append(file.readline().strip())
        else:
            s=file.read().splitlines()

    if ignore_blank:
        s = [e for e in s if e != '']

    if ignore_hash:
        s = [e for e in s if not e.lstrip().startswith('#')]

    if strip is not None:
        c = re.compile(r'(("[^"]*?")|(\'[^\']*?\')|[^;\'"]*)*') # avoid splitting within quoted string
        s = [c.match(s)[0] for e in s]

    if as_string:
        s='\n'.join(s)

    return s



