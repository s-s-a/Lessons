# ������ ������ � ZIP-����� � ������� Python
# ������ ������ � ZIP-������ � ���� �� ����� ������� �������� ��������� ������ ������
# � ���������� �� ��� �������� ��� ��������. ���������� ������ zipfile � Python ���������
# �������� � ZIP-�������� ��� ��������� �������������� ���������.

# ��� ������ ����������� ������ zipfile � ����� Path �� pathlib:

import zipfile
from pathlib import Path

# �������� ������� create_zip(), ������� ����� ��������� ZIP-����� � ���������� �������.
# � ������� ����� �������������� ��� ���������, � ������:
# folder_path � ���� � �����, ������� ����� ��������������
# archive_name � ��� ������������ ZIP-������.
import zipfile
from pathlib import Path


def zip_folder(folder_path: str, archive_name: str) -> None:
	# ������ ��, ������ ����� ��������� �������� �� ������������� �����:
	folder = Path(folder_path)

	# ���������, ���������� �� ��������� �����
	if not folder.is_dir():
		print(f"����� '{folder_path}' �� �������.")
		return

	# ����� ������������� ����������� ���������� � �������/�������� ZIP-����� � ������ ������.
	# ������ ���������� �������� �� ���� ������ � ���������� � ������� �� � �������� �����:

	# ��������� ��� ������ ZIP-����� � ������ ������
	with zipfile.ZipFile(archive_name, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
		# ���������� ������� ��� ����� � ����� ������ �������� ����������
		for file_path in folder.rglob("*"):
			if file_path.is_file():
			# ��������� ���� � �����, �������� ��������� ����������
			archive.write(file_path, arcname=file_path.relative_to(folder))
			print(f"�������� ����: {file_path}")

	print(f"����� '{archive_name}' ������� ������.")


# �������� �������� ����� �����:
if __name__ == "__main__":
	# ������ �������������
	# ������������ ������ ���� � �����
	folder_path = input("������� ���� � ����� ��� ������: ").strip()

	# ������������� ��������� ��� ������ �� ����� �����
	archive_name = Path(folder_path).name + ".zip"

	# �������� ������� ���������
	zip_folder(folder_path, archive_name)
