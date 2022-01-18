from itertools import takewhile, repeat
from math import prod

with open('input/16.txt') as f:
    hex_string = f.read().strip()

binary_string = ''.join(format(int(c, 16), "04b") for c in hex_string)
pntr = 0

def read(n:int) -> str:
    global binary_string, pntr
    pntr += n
    return binary_string[pntr-n:pntr]

def read_int(n:int) -> int:
    return int(read(n), 2)

def consume_literal() -> int: 
    read_next_group = True
    res = ""
    while read_next_group:
        read_next_group = int(read(1))
        res += read(4)
    return int(res, 2)

def read_packet1():
    packet_version = read_int(3)
    packet_type = read_int(3)
    if packet_type == 4:
        consume_literal()
        return packet_version
    else:
        length_type = read(1)
        if length_type == '0':
            total_length = read_int(15)
            end = pntr + total_length
            return packet_version + sum(read_packet1() for _ in takewhile(lambda _: pntr < end, repeat(None)))
        else:
            sub_packet_count = read_int(11)
            return packet_version + sum(read_packet1() for _ in range(sub_packet_count))

print('Part 1:', read_packet1())

def read_packet2():
    packet_version = read_int(3)
    packet_type = read_int(3)
    if packet_type == 4:
        return consume_literal()
    else:
        f = {
            0: sum,
            1: prod,
            2: min,
            3: max,
            5: lambda itr: next(itr) > next(itr),
            6: lambda itr: next(itr) < next(itr),
            7: lambda itr: next(itr) == next(itr)
        }[packet_type]
        length_type = read(1)
        if length_type == '0':
            total_length = read_int(15)
            end = pntr + total_length
            return f(read_packet2() for _ in takewhile(lambda _: pntr < end, repeat(None)))
        else:
            sub_packet_count = read_int(11)
            return f(read_packet2() for _ in range(sub_packet_count))
        
pntr = 0
print('Part 2:', read_packet2())