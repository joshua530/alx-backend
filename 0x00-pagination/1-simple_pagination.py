#!/usr/bin/env python3
"""
Paginates according to given indices
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """fetches a page from a given dataset"""
        dataset = self.dataset()
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        begin, end = index_range(page, page_size)
        if begin > len(dataset) or end > len(dataset):
            return []
        return [dataset[begin: end]]


def index_range(page: int, page_size: int) -> tuple:
    """
    Paginates according to given indices
    indices are 1-based
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
