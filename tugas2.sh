echo "----------------TUGAS 2----------------"
echo "masukkan nilai a : "
read a
echo "masukkan nilai b : "
read b

echo "perbandingan nilai a dengan nilai b adalah..."

if [ $a -eq $b ]
 then
  echo "nilai a sama dengan nilai b"
elif [ $a -gt $b ]
 then
  echo "nilai a lebih besar dari nilai  b"
elif [ $a -lt $b ]
 then
  echo "nilai a lebih kecil dari nilai b"
else
  echo "Tidak ada kondisi yang memenuhi"
fi


jumlah=`expr $a + $b`
kurang=`expr $a - $b`
kali=`expr $a \* $b`
bagi=`expr $a / $b`
mod=$(($a % $b))

echo "hasil penjumlahan a + b = $jumlah"
echo "hasil pengurangan a - b = $kurang"
echo "hasil perkalian a * b = $kali"
echo "hasil pembagian a / b = $bagi"
echo "hasil sisa pembagian a \\ b = $mod"

printf "gimana mudah bukan? \n"
printf "mudah banget ? \n"
printf "mudah sekali ? \n"

read jawab

case "$jawab" in
	"mudah banget")
		echo "kereen, teruslah belajar sistem operasi"
		;;
	"mudah sekali")
		echo "baguss, ayo perdalam sistem operasi"
		;;
	*)
		echo "tidak apa-apa, tetap semangaatt!!"
		;;
esac
