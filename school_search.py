import time
from itertools import groupby


class SchoolSearch:
    filename = 'sl051bai.csv'

    def search_schools(self, q):
        start_time = time.time()
        results = []

        with open(self.filename, newline='', encoding='cp1252') as file:
            search = q.upper()
            count = 0
            for row in file:
                row = row.split(',')
                # read the note below, please
                if search in row[3] or search in row[4] or search in row[5]:
                    if count > 2:
                        break
                    count += 1
                    results.append(f'{count}. {row[3]}')
                    results.append(f'{row[4]}, {row[5]}')

        search_time = time.time() - start_time
        print('Results for "%s" (search took: %ss)' % (q, search_time))
        for result in results:
            print(result)


school_search = SchoolSearch()
school_search.search_schools('elementary')
# school_search.search_schools('elementary school highland park')

'''
Unfortunately, I could only make an exact matching search. I tried, but couldn't find an efficient way to do.
Surely, I googled for solution, but what I found was too big for just to copy/paste, so I didn't do it. 
But in practice, I would copy/paste a solution I found and even may optimize it if possible.

It was first time working with CSV in Python. Never had to work with it before. I had a lot of pleasure
and got new experience. Thank you!
'''
