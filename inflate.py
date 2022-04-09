import struct
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="input_file",
                  help="Binary name or file path including binary name", metavar="example.com")
parser.add_option("-s", "--size", dest='inflate_size',
                  help="Size in MB to inflate binary by", metavar="10", type=int)
(options, args) = parser.parse_args()


def transform(file, size):
    print("[!]\tInflating %s by %s MB" % (file, size))
    blank_bytes = struct.pack('B', 0)
    transformer = open(file, 'ab')
    transformer.write(blank_bytes * 1024 * 1024 * size)
    transformer.close()
    print("[!]\tOperation Complete...\n")


if not options.input_file or not options.inflate_size:
    print("[ERROR] - Enter an input file and an inflation size in MB.\n\n"
        "$ python -f c:\\tools\\mimikatz.exe -s 100\n"
        "$ python -f mimikatz.exe -s 250\n\n")
else:
    transform(options.input_file, options.inflate_size)

