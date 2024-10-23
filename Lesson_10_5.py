from multiprocessing import Pool
from datetime import datetime
def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while True:
            all_data.append(file.readline())
            if not file.readline():
                break

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.now()
    print(end - start)


    start = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)