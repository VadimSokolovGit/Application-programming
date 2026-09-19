def status(signal: float) -> str:

    #датчик
    PVmin = 0
    PVmax = 75
    MinSign = 4
    MaxSign = 20

    sign_low = 3.9
    sign_high = 20.1

    if type(signal) not in [int, float]:
        raise TypeError("Signal must be int or float")

    if signal == 0:
        return "Датчик отключен"
    elif signal < sign_low:
        return "Датчик неисправен"
    elif signal > sign_high:
        return "Датчик неисправен"


    PV = (signal - MinSign) * (PVmax - PVmin) / (MaxSign - MinSign) + PVmin


    #корова
    if PV < 34.9:
        cow = "требуется внимание"
    elif PV < 37.4:
        cow = "корова замерзла, требуется обогрев"
    elif PV <= 39.0:
        cow = "с коровой все ок"
    elif PV <= 39.5:
        cow = "корова перегрелась, требуется охлаждение"
    elif PV > 39.6:
        cow = "срочно вызывайте ветеринара, коровка заболела"

    return f"Получен сигнал датчика {signal}mA, датчик исправен, температура {PV} градусов, {cow}"
