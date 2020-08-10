def validate_float(val, name=''):
    try:
        return True, float(val)
    except Exception:
        print(f"Значение параметра {name} должно быть числом")
        return False
