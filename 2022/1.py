with open('store/input_1.txt', 'r') as f:
    res = [sum(map(int, i.split('\n'))) for i in f.read().strip().split('\n\n')]
    print('task_1:', max(res))
    res.sort()
    print('task_2:', sum(res[-3:]))
