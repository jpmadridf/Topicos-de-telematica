from mrjob.job import MRJob
from mrjob.job import MRStep

class P6(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer2),
        ]

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, int(rating)

    def reducer(self, movie, values):
        l = list(values)
        cant = len(l)
        avg = sum(l)/cant
        yield None,(movie,avg)
    
    def reducer2(self, date, values):
        l = list(values)
        ordenados = sorted(l, key=lambda avg : avg[1], reverse=True)
        yield "date and average rating:" , ordenados[0]

if __name__ == '__main__':
    P6.run()