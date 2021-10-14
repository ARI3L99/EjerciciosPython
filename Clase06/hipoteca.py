monto = 500000.0
tasaFija = 0.05
pagado = 0.0
mensual = 2684.11
meses = 0
comienzo_pago_extra = 61
fin_pago_extra = 108
pago_extra = 1000

while monto > 0:
    meses += 1
    if meses >= comienzo_pago_extra and meses <= fin_pago_extra:
        monto = monto * (1+tasaFija/12) - mensual - pago_extra
        pagado += mensual + pago_extra

    else:
        if monto < mensual:
            mensual = 0
            pagado+= monto
            monto = 0

        monto = monto * (1+tasaFija/12) - mensual
        pagado += mensual
    print(f'Mes {meses} Total pagado ${pagado:0.2f} Total a pagar ${monto:0.2f}')

print(f'Total pagado ${pagado:0.2f} en {meses} meses')
