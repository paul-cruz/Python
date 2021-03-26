def most_requested(rooms):
    number_of_requests = {}
    for room in rooms:
        if room[0] == '+':
            if room in number_of_requests.keys():
                number_of_requests[room] += 1
            else:
                number_of_requests[room] = 1
    return max(number_of_requests, key=number_of_requests.get)[1:]


def solution(A):
    reservations = {}
    for reserv in A:
        if reserv in reservations.keys():
            reservations[reserv] += 1
        else:
            reservations[reserv] = 1
    max_number_of_reservations = max(reservations.values())

    list_of_rooms = []
    for room in reservations:
        if reservations[room] == max_number_of_reservations:
            list_of_rooms.append(room[1:])

    list_of_rooms.sort()

    return list_of_rooms[0]


if __name__ == "__main__":
    rooms = input().split(',')

    print(most_requested(rooms))
    print(solution(rooms))
