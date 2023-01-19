#!/usr/bin/env python3
"""
Paginates according to given indices
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Paginates according to given indices
    indices are 1-based
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
