def my_power_function_1(x, func_params={"prefactor": 1.0, "power": 2, "x_shift": 0.0, "y_shift": 0.0}):
    """
    A * (x - x0)^n + y0
    """
    A = func_params["prefactor"]
    n = func_params["power"]
    x0 = func_params["x_shift"]
    y0 = func_params["y_shift"]

    return A * (x - x0)**n + y0

