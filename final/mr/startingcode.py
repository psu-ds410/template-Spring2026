from mrjob.job import MRJob
from mrjob.step import MRStep

class Final(MRJob):
    def mapper_one(self, _, line):
        parts = line.split("\t")
        if len(parts) == 5 and not parts[0].startswith("InvoiceNo"): # orders
            (orderid, itemid, quantity, date, cid) = parts
            yield (cid.strip(), orderid), (int(quantity), 1)
        else:
            pass


    def combiner_one(self, key, valuelist): # key is a string, value is a list of [int, int] elements
        # fill this in


    def reducer_one(self, key, valuelist):
        # fill this in


    def mapper_two(self, key, value): # key is a string, value is [int, int]
        yield key, value

    def combiner_two(self, key, valuelist): # key is a string, value is a list of [int, int] elements
        first = 0
        second = 0
        for (f, s) in valuelist:
            first = first + f
            second = second + s
        yield key, (first, second)

    def reducer_two(self, key, valuelist): # key is a string, value is a list of [int, int] elements
        first = 0
        second = 0
        for (f, s) in valuelist:
            first = first + f
            second = second + s
        yield key, (first, second)
 

    def steps(self):
        return [
            MRStep(mapper=self.mapper_one, reducer=self.reducer_one, combiner=self.combiner_one),
            MRStep(mapper=self.mapper_two, reducer=self.reducer_two, combiner=self.combiner_two)
        ]


if __name__ == '__main__':
    Final.run()   

