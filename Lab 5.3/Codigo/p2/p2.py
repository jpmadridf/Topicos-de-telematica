from mrjob.job import MRJob


class P2(MRJob):

    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, float(price)

    def reducer(self, company, values):
        l = list(values)
        price = l[0]
        stable = 1
        for i in l:
            if i < price:
                stable = 0
            price = i
        if stable==1:
            yield 'Stable company', company


if __name__ == '__main__':
    P2.run()