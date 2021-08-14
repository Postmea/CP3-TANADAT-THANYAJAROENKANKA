manu = ['ผัดไทย',"ข้าวผัด","ไข่ดาว"]
print(manu)
manu.append("เป็ดย่าง")  #.append คือการเพิ่มข้อมูลใน list
print(manu)
manu.remove("ข้าวผัด")  #.remove คือการลบข้อมูลใน list
print(manu)
manu[1] = "ข้าวผัดกุ้ง"  #[1] คือระบุตำแหน่งตัวที่ 2 และทำการแก้ไข
print(manu)
del manu[0]  #del ....[0] คือระบุตำแหน่งตัวที่ 1 และทำการลบ
print(manu)