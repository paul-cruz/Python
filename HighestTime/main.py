def highest_time(time):
    time_list = list(time)
    if time_list[0] == '1' or time_list[0] == '0':
        if time_list[1] == '?':
            time_list[1] = '9'
    elif time_list[0] == '2':
        if time_list[1] == '?':
            time_list[1] = '3'
    else:
        if time_list[1] == '?':
            time_list[0] = '2'
            time_list[1] = '3'
        elif int(time_list[1]) <= 3:
            time_list[0] = '2'
        else:
            time_list[0] = '1'
    if time_list[3] == '?':
        time_list[3] = '5'
    if time_list[4] == '?':
        time_list[4] = '9'
    return ''.join(time_list)
    

if __name__ == "__main__":
    t = input()
    print(highest_time(t))
