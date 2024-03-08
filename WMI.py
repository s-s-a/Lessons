import wmi

# Создаем объект WMI
c = wmi.WMI()

# Получаем информацию о системе
system_info = c.Win32_ComputerSystem()[0]

# Выводим полученные данные
print(f"Производитель: {system_info.Manufacturer}")
print(f"Модель: {system_info.Model}")
print(f"Имя компьютера: {system_info.Name}")
print(f"Количество процессоров: {system_info.NumberOfProcessors}")
print(f"Тип системы: {system_info.SystemType}")
print(f"Физическая память: {system_info.TotalPhysicalMemory}")
