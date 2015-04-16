class LazyPagedSequence(object):
    """
    LazyPagedSequence provides a read-only list-like interface to paged data structures of known length.

    This class is intended to be used with paged resources in which pages may be expensive to return.
    Individual pages are cached, allowing for retrieval of individual items from a given page without repeated calls to the page function.

    Because the length of the sequence is fixed and is known before any pages are fetched, this class is suitable for use with Django's Paginator class without inducing undue overhead.

    An example
    """

    def __init__(self, page_func, page_size, length):
        """
        :param function page_func: Function to be used to reify individual pages in the LazyPagedSequence's cache.
            page_func will be called with the following two functions:
                * page, an integer representing the page to produce (with the first page assumed to be 0).
                * page_size, an integer representing the size of the page to fetch; this will always be the same number.
        :param integer page_size: The size of the pages.
        :param integer length: The total length of all items in this sequence.
            This must be known ahead of time.
        """
        self.page_func = page_func
        self.page_size = page_size
        self._length = length
        self.__cache = {}

    def __len__(self):
        return self._length

    def __page(self, index):
        """
        Determine the page number on which a given index will be located, using self.page_size. Assumes page count begins with 1.
        """
        return index / self.page_size + 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            step = 1 if index.step is None else index.step
            return [self.__getitem__(i) for i in xrange(index.start, index.stop, step)]

        if index > self._length:
            raise IndexError("LazyPagedSequence index out of range")

        page_number = self.__page(index)
        if page_number not in self.__cache:
            self.__cache[page_number] = self.page_func(page_number, self.page_size)
        return self.__cache[page_number][index % self.page_size]
