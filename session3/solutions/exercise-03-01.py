# with open("les_miserables.txt", "r", encoding="utf-8") as file:
#     it = iter(file)
#     print(next(it))
#     print(next(it))
#     print(next(it))
#
# print("Next part")
# TEXT_FILE = "les_miserables.txt"
#
# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     # Provide here your solution
#     it = iter(file)
#     print(next(it))
#
# print("Next part finding values")
# TEXT_FILE = "les_miserables.txt"
# target = "Jean Valjean"
# found = None
#
# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     counter = 0
#     for line in file:
#         counter += 1
#         # Provide here your solution
#         if target in line:
#             print(f"Found '{target}' at line {counter}")
#             found = line
#             break
#
# print(found)
#
# print("Next part counter")
#
# TEXT_FILE = "les_miserables.txt"
# count = 0
#
# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     for line in file:
#
#         # Provide here your solution
#         count += 1
#
# print(count)

# print("Part 9")
# TEXT_FILE = "les_miserables.txt"
# total_length = 0
# count = 0
#
# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     for line in file:
#         # Provide here your solution
#         total_length += len(line)
#         count += 1
#
# average = total_length / count
# print(average)

# print("Part 10")
# TEXT_FILE = "les_miserables.txt"
#
# with open(TEXT_FILE, "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# print(lines[100])

# print("Part 11")
# def non_empty_lines(path):
#     with open(path, "r", encoding="utf-8") as file:
#         for line in file:
#             line = line.strip()
#             if line != "":
#                 yield line
#
# for line in non_empty_lines("les_miserables.txt"):
#     print(line)
#     break

print("Part 12")
TEXT_FILE = "les_miserables.txt"
target = "Jean"

def non_empty_lines(path, non_empty=True):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "" and non_empty:
                yield line
            elif not non_empty:
                print("Sending non empty line")
                yield line

count = 0

# Use non_empty_lines(TEXT_FILE) to count
# how many non-empty lines contain target
for line in non_empty_lines("les_miserables.txt", True):
    if line == "":
        print("Empty line")
    count += 1

print(count)