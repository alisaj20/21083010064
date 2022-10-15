#!/bin/bash

echo "Input nilai : "
read ipk

i=1;
jumlah=0;
ipk_mhs=0;

while [ $i -le $ipk ]
do
	echo "nilai ke $i : "; 
	i=$((i+1))
	read x
	jumlah=$((jumlah+x))
	ipk_mhs=$((jumlah/ipk))
done

echo "Nilai IPS mahasiswa = " $jumlah / $ipk
echo "Nilai IPK mahasiswa = " $((jumlah/ipk))
