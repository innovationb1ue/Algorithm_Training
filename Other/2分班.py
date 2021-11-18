"""排队分班，每个小朋友可以知道前面的人是否一个班"""

def solve(in_str):
    class1 = []
    class2 = [int(in_str.split(" ")[-1].split("/")[0])]
    class_list = [class1, class2]
    cur_class_index = 1
    y_flag = False
    for pair in in_str.split(" ")[::-1]:
        idx, ans = pair.split("/")
        idx = int(idx)
        if idx == 1:
            class_list[cur_class_index].append(idx)
            break
        if y_flag:
            class_list[cur_class_index].append(idx)
        if ans == 'N':
            cur_class_index -= 1
            if cur_class_index < 0:
                raise ValueError
        elif ans == 'Y':
            y_flag = True
    class1 = sorted(class1)
    class2 = sorted(class2)
    return class1, class2


if __name__ == '__main__':
    in_str = '1/N 2/Y 3/N 4/Y 5/Y 6/Y 7/Y'
    c1, c2 = solve(in_str)
    print(c1, c2)
