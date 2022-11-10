from mrjob.job import MRJob
from mrjob.job import MRStep

class P7(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer2),
        ]

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield movie, int(rating)

    def reducer(self, movie, values):
        l = list(values)
        cant = len(l)
        avg = sum(l)/cant
        yield None,(movie,avg)
    
    def reducer2(self, date, values):
        l = list(values)
        Max = sorted(l, key=lambda avg : avg[1], reverse=True)
        Min = sorted(l, key=lambda avg : avg[1])
        yield [("movie with max rating:" , Max[0])],[("movie with min rating:" , Min[0])]

if __name__ == '__main__':
    P7.run()