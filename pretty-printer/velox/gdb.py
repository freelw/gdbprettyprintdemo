import os
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
import sys
sys.path.insert(0, current_directory)
import vector_printer
