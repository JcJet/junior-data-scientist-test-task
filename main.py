def get_user_group(user_id):
    user_group = 0
    while user_id:
        user_group, user_id = user_group + user_id % 10, user_id // 10
    return user_group


def get_user_groups(n_customers=0, n_first_id=0):
    user_groups = {}
    cur_user = n_first_id
    while cur_user < n_customers:
        cur_user_group = get_user_group(cur_user)
        user_groups[cur_user_group] = user_groups.get(cur_user_group, 0) + 1
        cur_user += 1
    return user_groups


if __name__ == '__main__':
    # Первый вариант функции:
    user_groups_test = get_user_groups(11)
    print(user_groups_test)
    # Второй вариант функции:
    user_groups_test = get_user_groups(11, 5)
    print(user_groups_test)
