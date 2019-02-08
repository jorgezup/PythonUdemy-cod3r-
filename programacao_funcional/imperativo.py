from calendar import mdays, month_name


# Listar todos os meses do ano com 31 dias
print('Meses com 31 dias: ')
# for k, mes in enumerate(month_name):
#     if mdays[k] == 31:
#         print(f'- {mes}')

for mes1 in range(1, 13):
    if mdays[mes1] == 31:
        print(month_name[mes1])
