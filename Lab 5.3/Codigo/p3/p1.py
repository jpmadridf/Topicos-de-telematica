from mrjob.job import MRJob


class P1(MRJob):

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield user, int(rating)

    def reducer(self, user, values):
        l = list(values)
        cant = len(l)
        avg = sum(l)/cant
        yield user,(cant,avg)

if __name__ == '__main__':
    P1.run()