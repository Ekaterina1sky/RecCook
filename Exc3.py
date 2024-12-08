import os.path
import os

def acounting(file:str) -> int:
    return
    # return sum(1 for _ in open('1.txt', 'rt', encoding='utf-8'))
#
def rewriting(Tekst_write: str, base_path, Exc):
    files = []
    for i in list(os.listdir(os.path.join(base_path, Exc))):
        files.append([acounting(os.path.join(base_path, Exc, i)), os.path.join(base_path, Exc, i), i])
        # print(i)

    for file_from_list in sorted(files):
        opening_files = open(Tekst_write, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        # print(file_from_list)
        # print(Tekst_write)
        # print(files)
        with open(file_from_list[1], 'r', encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()
    # print(sorted(files))
    print(file_from_list)

Exc = os.path.abspath('\\Users\\618\\Desktop\\Rec\\NewFolder')
Tekst_write = os.path.abspath('\\Users\\618\\Desktop\\Rec\\1.txt')
base_path = os.getcwd()
rewriting(Tekst_write, base_path, Exc)





