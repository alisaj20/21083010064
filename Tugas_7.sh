#!/bin/bash

panjang() {
	echo "Masukkan Panjang : "
	read panjang
}
lebar() {
	echo "Masukkan Lebar : "
	read lebar
}

luas() {
	let luas=panjang*lebar
	echo "Luas Persegi : $luas"
}

panjang
lebar
luas
