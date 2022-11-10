from mrjob.job import MRJob


class P4(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield movie, int(rating)

    def reducer(self, movie, values):
        l = list(values)
        cant = len(l)
        avg = sum(l)/cant
        yield movie,(cant,avg)

if __name__ == '__main__':
    P4.run()