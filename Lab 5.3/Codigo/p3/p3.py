from mrjob.job import MRJob
from mrjob.job import MRStep


class P3(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(reducer=self.reducer2),
        ]

    def mapper1(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date,1 

    def reducer1(self, date, values):
        l = list(values)
        suma = sum(l)
        yield None,(date,suma)
    
    def reducer2(self,date, values):
        l = list(values)
        ordenados = sorted(l, key=lambda max : max[1])
        yield "Date:" , ordenados[0]

if __name__ == '__main__':
    P3.run()