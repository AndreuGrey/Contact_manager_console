# Проверяет команду выбора в меню
def command_input_test(input_user: int | str) -> tuple[bool, str]:
    """
    Info: 
        Проверяет ввода пользователя в центральном меню.

    Args:
        input_user: Введённое пользователем значение (число или строка).

    Returns:
        Кортеж (True, "") в случае успеха,
        либо (False, "сообщение об ошибке") при неудаче.
    """
    if isinstance(input_user, str):  # Проверка строки
        if input_user.isdigit():
            input_user = int(input_user)
        else:
            return False, f"Ввод не должен содержать буквы или быть пустым. Ввод: {input_user}"

    if isinstance(input_user, int):  # Проверка числа
        if 1 <= input_user <= 5:
            return True, ""
        else:
            return False, f"Значение должно быть от 1 до 5. Ввод: {input_user}"

    return False, f"Неподдерживаемый тип данных: {type(input_user)}"
