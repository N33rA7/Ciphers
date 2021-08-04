#!/usr/bin/env python
import numpy as np
import socket

private_key = np.array([[15, 17], [20, 9]])

def decrypt_char(red_cip):
        dec_data = []
        for row in red_cip:
                for item in row:
                        data = chr(item)
                        dec_data.append(data)
        print(''.join(dec_data))

def matrix_calc(matrix1, matrix2):

        res = [[0 for x in range(2)] for y in range(2)]
        # explicit for loops
        for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                        for k in range(len(matrix2)):
                                res[i][j] += matrix1[i][k] * matrix2[k][j]

        return res;


def matrix_row(number_msg):

        row1 = number_msg[:len(number_msg)/2]
        row2 = number_msg[len(number_msg)/2:]
        return row1, row2;

def receiver():
	open_socket = socket.socket()
	port = 5005
	open_socket.connect(('127.0.0.1', port))
	cipher_data = open_socket.recv(1024)
	return cipher_data;
	open_socket.close()

def main():

	cipher_data = receiver()
	#print(cipher_data)
	data = []
	for byte in cipher_data:
		d= ord(byte)
		data.append(d)
	#print(data)
	row1, row2  = matrix_row(data)
        data_msg = np.array([row1, row2])
        data_msg = data_msg - 97
#	print(data_msg)
	cipher = matrix_calc(data_msg, private_key)
	cipher = np.array(cipher)
	red_cip = cipher % 26 + 97
	#print(red_cip)
	decrypt_char(red_cip)

if __name__ == '__main__':
  main()
