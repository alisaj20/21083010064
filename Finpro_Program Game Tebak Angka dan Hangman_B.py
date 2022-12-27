import random
import string

def home():
    while(True):
        pilih = int(input("Pilih game yang ingin kamu mainkan : \n1. Tebak Angka \n2. Hangman \nJawab = "))
        if(pilih == 1):
            gametebakangka()
        elif(pilih == 2):
            gamehangman()
        else:
            exit()
            break
def exit():
    print("Terimakasih Telah Bermain")

def gametebakangka():
    while(True):
        print("=" * 41)
        print("|  Selamat datang di Game Tebak Angka!  |")
        print("=" * 41)
        level = input("Masukkan level [mudah/sedang/sulit] : ")
        while( level != "mudah" and level != "sedang" and level != "sulit" ) :
            level = input("\nMaaf, inputan anda salah. Silahkan coba lagi.\nMasukkan level [mudah / sedang / sulit] : ")

        if level == "mudah" :
            batas_percobaan = 5
            bilrandom = random.randint(1,10)
        elif level == "sedang" :
            batas_percobaan = 6
            bilrandom = random.randint(1,20)
        elif level == "sulit" :
            batas_percobaan = 7
            bilrandom = random.randint(1,30)

        print("Level", level, "dengan batas percobaan sebanyak", batas_percobaan, "kali")    
        
        print("-" * 47)
        print("|  Kami sudah memilih angka, Ayo coba tebak!  |")
        print("-" * 47)

        #Looping tebak angka
        while(batas_percobaan >= 0):
            if batas_percobaan == 0:
                print("Angka yang benar adalah ", bilrandom)
                print("Yaah sayang sekali gagal, batas percobaanmu sudah habis :(")
                break
            else:
                print("Batas percobaanmu : ", batas_percobaan)
                jawaban = int(input("\nMasukkan Angka : "))
                if jawaban == bilrandom:
                    print("Yeaayy Berhasil, tebakanmu benar!")
                    break
                elif jawaban > bilrandom:
                    print("Angkanya dibawah dari", jawaban)
                    batas_percobaan -= 1
                elif jawaban < bilrandom:
                    print("Angkanya diatas dari", jawaban)
                    batas_percobaan -= 1    
        
        # Mengkonfirmasi ulang
        ulang = input("\nIngin coba lagi? : ")
        while( ulang != "yes" and ulang != "no"):
            ulang = input("\nMaaf, inputan anda salah. Silahkan coba lagi.\nIngin coba lagi? : ")

        if ulang == "yes":
            print("\nSiap, Mulai!\n")
        elif ulang == "no":
            print("\nGame Berakhir, Terimakasih sudah bermain :).\n")
            break
            home()

    

def gamehangman():
    while(True):
        print("=" * 39)
        print("|  Selamat datang di Game Hangman!    |")
        print("|  CLUENYA : menebak kata zodiak      |")
        print("=" * 39)
        from words import word_list

        def get_word():
            word = random.choice(word_list)
            return word.upper()
        
        def play(word):
            word_completion = "_" * len(word)
            tebakan = False
            tebak_huruf = []
            tebak_kata = []
            kesempatan = 6
            print("-" * 26)
            print("|  Kesempatanmu ada", kesempatan, "   |")
            print("|  Siap, Mulai!          |")
            print("-" * 26)
            print(display_hangman(kesempatan))
            print(word_completion)
            print("\n")
            while not tebakan and kesempatan > 0:
                tebak = input("Masukkan huruf : ").upper()
                if len(tebak) == 1 and tebak.isalpha():
                    if tebak in tebak_huruf:
                        print("Kamu sudah menebak huruf ini", tebak)
                    elif tebak not in word:
                        print("Huruf", tebak, "tidak ada di alphabet")
                        kesempatan -= 1
                        tebak_huruf.append(tebak)
                    else:
                        print("Tebakan Benar!")
                        tebak_huruf.append(tebak)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == tebak]
                        for index in indices:
                            word_as_list[index] = tebak
                            word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            tebakan = True
                elif len(tebak) == len(word) and tebak.isalpha():
                    if tebak in tebak_kata:
                        print("Kamu sudah menebak huruf ini", tebak)
                    elif tebak != word:
                        print(tebak, "Tidak ada di alphabet")
                        kesempatan -=1
                        tebak_kata.append(tebak)
                    else:
                        tebakan = True
                        word_completion = word
                
                else:
                    print("Tebakan salah. Silahkan coba lagi")
                print(display_hangman(kesempatan))
                print(word_completion)
                print("\n")

            if tebakan:
                print("Selamat! kamu berhasil menebak katanya, Kamu Menang!")
            else:
                print("Yaah sayang sekali, kesempatanmu habis, game sudah berakhir :(. Katanya adalah", word)

        def display_hangman(kesempatan):
            stages = [  # final state: head, torso, both arms, and both legs
                        """
                            --------
                            |      |
                            |      O
                            |     \\|/
                            |      |
                            |     / \\
                            -
                        """,
                        # head, torso, both arms, and one leg
                        """
                            --------
                            |      |
                            |      O
                            |     \\|/
                            |      |
                            |     / 
                        -
                        """,
                        # head, torso, and both arms
                        """
                            --------
                            |      |
                            |      O
                            |     \\|/
                            |      |
                            |      
                            -
                        """,
                        # head, torso, and one arm
                        """
                            --------
                            |      |
                            |      O
                            |     \\|
                            |      |
                            |     
                            -
                        """,
                        # head and torso
                        """
                            --------
                            |      |
                            |      O
                            |      |
                            |      |
                            |     
                            -
                        """,
                        # head
                        """
                            --------
                            |      |
                            |      O
                            |    
                            |      
                            |     
                            -
                        """,
                        # initial empty state
                        """
                            --------
                            |      |
                            |      
                            |    
                            |      
                            |     
                            -
                        """
            ]
            return stages[kesempatan]
        
        def main():
            word = get_word()
            play(word)
            while input("\nIngin coba lagi? : ").upper() == "Y":
                print("\nSiap, Mulai!\n")
                word = get_word()
                play(word)
            
            print("\nGame Berakhir, Terimakasih sudah bermain :).\n")
            home()
        
        if __name__ == "__main__":
            main()
            break
home()