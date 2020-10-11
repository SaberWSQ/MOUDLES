"""
Program: file_read_write.py
Author: Shiqi Wang
Last date modified: 10/05/2020

The purpose of this program is to read and write a file.
"""

def write_to_file(content_tuple):
    """Add content tuple at the end of the file
    :param tuple content_tuple: content
    :return: None
    """
    with open("student_info.txt", 'a') as f:
        f.write(f"{content_tuple}\n")


def get_student_info(**kwargs):
    content = (kwargs['name'],)

    while True:
        score = input(f"{kwargs['name']}, please input your score (press 'q' or 'Q' to quit): ")
        if score.lower() == 'q':
            break

        try:
            score = float(score)
        except ValueError:
            raise ValueError("Input score is not a number")
        else:
            content += (score,)

    write_to_file(content)


def read_from_file():
    """Read content from student_info.txt
    and print the content line by line
    :return: None
    """
    with open("student_info.txt", 'r') as f:
        for line in f.readlines():
            print(line)


if __name__ == '__main__':
    get_student_info(name='student A')
    get_student_info(name='student B')
    get_student_info(name='student C')
    get_student_info(name='student D')

    read_from_file()
    input("Press any key to end")
