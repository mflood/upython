


import sys

class SimpleWriter(object):
    
    def __init__(self, output_file):
        self.output_file = output_file

    def write(self, data):
        with open(self.output_file, "a") as out_handle:
            out_handle.write(data)

    def __repr__(self): 
        return "SimpleWriter %s" % self.output_file

class DummyWriter(object):

    def write(self, data):
        print data

    def __repr__(self):
        return "DummyWriter"

def main():
    input_args = sys.argv;
    if len(input_args) != 3:
        print "Usage: python main.py <inputfile> <outputfile>"
        sys.exit(-1)

    input_file = input_args[1]
    output_file = input_args[2]
    
    print "Input file: %s  Output file: %s" % (input_file, output_file)

    my_writer = SimpleWriter(output_file)

    #my_writer = DummyWriter()

    with open(input_file, "r") as in_handle:
        for line in in_handle:
            my_writer.write(line)
    print my_writer

main()
