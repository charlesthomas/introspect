#!/usr/bin/env python
from datetime import datetime
from os import makedirs, path
from time import sleep

from window_title import get_window_title

NOW_TO_THE_HOUR = '%Y-%m-%d-%H'
EPOCH = '%s'

def logger(run_forever=True, stdout=False):
    write_path = setup_write_dir()
    run = True
    while run:
        now = datetime.now()
        file_end = now.strftime(NOW_TO_THE_HOUR)
        epoch = now.strftime(EPOCH)
        output = "%s: %s" % (epoch, get_window_title())

        if stdout:
            print output
        else:
            with open('%s_%s.log' % (write_path, file_end), 'a') as log_file:
                log_file.write(output + '\n')

        run = run_forever
        if run:
            sleep(1)

def main():
    logger(stdout=True)

def setup_write_dir():
    partial = path.join(path.expanduser('~'), '.introspect')
    if not path.isdir(partial):
        makedirs(partial)
    return path.join(partial, 'introspect')

if __name__ == '__main__':
    main()
