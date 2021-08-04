#!/usr/bin/env python
import numpy as np
import socket

key = np.array([[3, 3], [2, 5]])

def send(byte_message):
	
	bytes = ''.join(map(str, byte_message))
	s= socket.socket()
	port = 5005
	s.bind(('', port))
	s.listen(5)
	while True:
		c, addr = s.accept()
		c.send(bytes)
		c.close()

def encrypt_char(red_cip):
	enc_data = []
	for row in red_cip:
		for item in row:
			data = chr(item)
			enc_data.append(data)
	return enc_data;
		
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

def main():

	message = raw_input("Enter the message you want to send: ")
	message = message.lower()#Network
	#print(message)
	msg_string = message.replace(" ", "")
	if len(msg_string) != 4:
		print("Message length more than 4, Try again")
		exit();
	else:

		number_msg = []
		for i in msg_string:
        		number_msg.append(ord(i)-97)

		rem = len(number_msg)%2
		#print(rem)
		if(rem == 0):
        		row1, row2  = matrix_row(number_msg)
			data_msg = np.array([row1, row2])
			#print(data_msg)
			cipher = matrix_calc(data_msg, key)
			cipher = np.array(cipher)
			red_cip = cipher % 26 + 97
			send_data = encrypt_char(red_cip)
			send(send_data)
		else:
        		number_msg.append(25)#z
        		row1, row2 = matrix_row(number_msg)
			n_array = np.array([row1, row2])
                	print(n_array)
                	det = np.linalg.det(n_array)
                	print(int(det))

if __name__ == '__main__':
  main()
 
