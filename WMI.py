import wmi

# ������� ������ WMI
c = wmi.WMI()

# �������� ���������� � �������
system_info = c.Win32_ComputerSystem()[0]

# ������� ���������� ������
print(f"�������������: {system_info.Manufacturer}")
print(f"������: {system_info.Model}")
print(f"��� ����������: {system_info.Name}")
print(f"���������� �����������: {system_info.NumberOfProcessors}")
print(f"��� �������: {system_info.SystemType}")
print(f"���������� ������: {system_info.TotalPhysicalMemory}")
