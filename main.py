import sys


if len(sys.argv) < 2:
    print("No brainfuck sources provided!")
    exit()

try: 
    f = open(sys.argv[1])
except FileNotFoundError:
    print("Path provided contains no sources!")
    exit()
src = f.read()
f.close()


lines = src.split("\n")
src = src.replace("\n", "")

memory_cells = [0]
current_cell = 0
loop_stack = []
program_counter = -1  # i don't like this much
while program_counter < len(src) - 1:
    program_counter += 1
    c = src[program_counter]

    if c == "<":
        current_cell -= 1

        if current_cell < 0:
            # print(f"Memory cell out of bounds at l.{i}:{j}")
            exit()

        continue
    

    if c == ">":
        current_cell += 1

        if current_cell > len(memory_cells) - 1:
            memory_cells.append(0)

        continue
    

    if c == "+":
        memory_cells[current_cell] += 1

        continue


    if c == "-":
        memory_cells[current_cell] -= 1

        if memory_cells[current_cell] < 0:
            # print(f"Memory cell {current_cell} became negative at l.{i}:{j}")
            exit()

        continue


    if c == ".":
        print(chr(memory_cells[current_cell]), end='')

    
    if c == ",":
        while True:
            read = input()

            if len(read) > 1 or len(read) == 0:
                print("Input not a single char!")
                continue

            memory_cells[current_cell] = ord(read)
            break

        continue


    if c == "[":
        if memory_cells[current_cell] == 0:
            depth = 1
            while True:
                if depth == 0:
                    break
                    
                program_counter += 1

                if src[program_counter] == "[":
                    depth += 1

                if src[program_counter] == "]":
                    depth -= 1

            continue

        loop_stack.append(program_counter)
        continue

    
    if c == "]":
        program_counter = loop_stack.pop() - 1
        continue
