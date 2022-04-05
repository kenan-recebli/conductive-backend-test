import csv
from itertools import groupby


class CountSchools:
    filename = 'sl051bai.csv'

    def print_counts(self):
        print('Total Schools: ' + self.count_total())

        print('Schools by State:')
        self.count_by_state()

        print('Schools by Metro-centric locale:')
        self.count_by_metro_centric()

        self.count_cities()

    def count_total(self):
        with open(self.filename, newline='', encoding='cp1252') as file:
            return str(sum(1 for row in file) - 1)  # noqa

    def count_by_state(self):
        with open(self.filename, newline='', encoding='cp1252') as file:
            self.iterate(5, file, 'LSTATE05')

    def count_by_metro_centric(self):
        with open(self.filename, newline='', encoding='cp1252') as file:
            self.iterate(8, file, 'MLOCALE')

    def count_cities(self):
        with open(self.filename, newline='', encoding='cp1252') as file:
            counts = []

            def key(x):
                return x[4]

            data = sorted(csv.reader(file), key=key)
            for key, group in groupby(data, key=key):
                if not key == 'LCITY05':
                    counts.append(sum(1 for row in group))  # noqa
            max_count = max(counts)
            print('City with most schools: %s (%s schools)' % (data[counts.index(max_count)][4], str(max_count)))
            print('Unique cities with at least one school: ' + str(len(counts)))

    @staticmethod
    def iterate(index, file, header):
        def key(x):
            return x[index]

        for key, group in groupby(sorted(csv.reader(file), key=key), key=key):
            if not key == header:
                print(key + ': ' + str(sum(1 for row in group)))  # noqa


count_schools = CountSchools()
count_schools.print_counts()
