def ask_password(login: str, password: str, success: callable, failure: callable):
    count_v, count_c, pos_c = 0, 0, 0
    for pos, symbol in enumerate(password.lower()):
        if symbol in "aeiouy":
            count_v += 1
        elif symbol in login.lower():
            count_c, pos_c = 0 if pos_c > pos else count_c + 1, pos
    if count_v < 3 and count_c < 3:
        failure(login, "Everything is wrong")
    elif count_v < 3:
        failure(login, "Wrong number of vowels")
    elif count_c < 3:
        failure(login, "WRONG CONSONANTS")
    else:
        success(login)


ask_password("anastasia", "nsyatos",
             lambda login: print(f"Привет, {login} !"),
             lambda login, message: print(f"Кто-то пытался притвориться пользователем {login},но в пароле допустил ошибку:{message}"))

ask_password("eugene", "aanig",
             lambda login: print(f"Привет, {login} !"),
             lambda login, message: print(f"Кто-то пытался притвориться пользователем {login},но в пароле допустил ошибку:{message}"))

ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))