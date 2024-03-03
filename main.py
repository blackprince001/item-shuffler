import time

from src.shuffler import Item, ShuffleQueue, create_item_id

if __name__ == "__main__":
    start_time = time.time()

    shuffle_queue = ShuffleQueue()

    collection = [
        Item(x, y, id=create_item_id()) for x, y in zip("ABCDEFGH", "ZYXWSRTU")
    ]

    # show how the original collection is grouped
    print(collection)

    # shuffle the items into the queue and pop them out for logging
    final_queue = shuffle_queue.shuffle(collection)
    N = final_queue.qsize()

    for _ in range(N):
        print(final_queue.get())

    end_time = time.time()

    print(f"Execution time was {end_time - start_time} seconds.")
