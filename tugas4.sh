#!/bin/bash
echo "input angka : "
read angka

echo "Hasilnya adalah "
until [ ! $angka -gt 0 ]
do
	echo $angka
	angka=$((angka-2))
done
