print("----Status Kelulusan Ujian Mahasiswa----")
nama= (input("Nama :"))
mtk= float(input("Nilai Matematika : "))
bhsindo= float(input("Nilai Bhs Indonesia : "))
ipa= float(input("Nilai IPA : "))
if (mtk<0) or (bhsindo<0) or (ipa<0) or (mtk>100) or (bhsindo>100) or (ipa>100):
    print("Maaf input ada yang tidak valid")
elif (mtk>70) and (bhsindo>60) and (ipa>60):
     print("Status Kelulusan : ", nama, "Dinyatakan LULUS")
else:
    print("Status Kelulusan : ", nama, "Dinyatakan TIDAK LULUS")
    print("Sebab")
    if (mtk<70):
        print("-Nilai Matematika Kurang dari 70")
    if (bhsindo<60):
        print("-Nilai Bhs Indonesia Kurang dari 60")
    if (ipa<60):
        print("-Nilai IPA Kurang dari 60")