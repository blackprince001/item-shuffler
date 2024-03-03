from dataclasses import dataclass
from queue import Queue
from random import randint
from typing import List
from uuid import UUID, uuid4


# you can alter the content of the Item class to whatever object wrapping you intend to have.
@dataclass
class Item:
    slug: str
    content_type: str
    id: UUID


class ShuffleQueue:
    def __init__(self):
        self.__shuffle_queue = Queue(maxsize=0)

    def shuffle(self, shuffleableitems: List[Item]):
        N = len(shuffleableitems)

        for i, item in enumerate(shuffleableitems):
            # randomise the locations of the items placed into queue
            # this can take various forms depending on what shuffling algo you want
            rand_value_index_from_collection = randint(i, N - 1)

            self.__shuffle_queue.put(
                shuffleableitems[rand_value_index_from_collection].__dict__
            )
        return self.__shuffle_queue

    # implement iterators that can traverse into the queue and pop certain elements.
    # next(), current(), previous() methods.


def create_item_id() -> UUID:
    return uuid4()
