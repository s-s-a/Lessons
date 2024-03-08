import ctypes


lib1 = ctypes.CDLL("handlers/lib1.so")
lib2 = ctypes.CDLL("handlers/lib2.so")
lib3 = ctypes.CDLL("handlers/lib3.so")


string = ctypes.create_string_buffer(b"zprogerit")
lib1.open_website(string)
lib2.start_thread()
lib3.start_thread2()