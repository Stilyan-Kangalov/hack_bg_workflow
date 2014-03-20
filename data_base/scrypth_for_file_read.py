import sys
import glob
import errno

def scripth():
    path = 'home/hack_bg_workflow/data_base'
    files = glob.glob(path)
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        print(name)
        print(name)
def main():
    scripth()
if __name__ == '__main__':
    main()
    # try:
    #     with open(name) as f: # No need to specify 'r': this is the default.
    #         sys.stdout.write(f.read())
    # except IOError as exc:
    #     if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
    #         raise # Propagate other kinds of IOError.
