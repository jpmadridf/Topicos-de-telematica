from mrjob.job import MRJob
from mrjob.job import MRStep
import numpy as np



class P3(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(reducer=self.reducer2),
        ]

    def mapper1(self, _, line):
        company,price,date = line.split(',')
        yield date, float(price)

    def reducer1(self, date, values):
        l = list(values)
        suma = sum(l)
        avg = suma/len(l)
        yield None,(date,avg)

    def reducer2(self, date, values):
        l = list(values)
        ordenados = sorted(l, key=lambda avg : avg[1])
        yield "date and average price:" , ordenados[0]


if __name__ == '__main__':
    P3.run()