from HuffmanCoding import HuffmanCoding

path = input("Enter the path to the file: ")

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)
