1. **Kế thừa**: Khi một lớp (class) có thể **nhận các thuộc tính và phương thức từ một lớp khác**.  
   - **Ví dụ**:  
     ```python
     class Xe:
         def lai(self):
             print("Xe đang được lái")

     class XeTheThao(Xe):
         pass

     xe_the_thao = XeTheThao()
     xe_the_thao.lai()  # Output: Xe đang được lái
     ```

2. **Lớp con (subclass) có thể mở rộng hoặc sửa đổi các phương thức của lớp cha (superclass)**:  
   - **Ví dụ**:  
     ```python
     class Nguoi:
         def gioi_thieu(self):
             print("Tôi là một người bình thường")

     class BacSi(Nguoi):
         def gioi_thieu(self):
             super().gioi_thieu()
             print("Tôi cũng là một bác sĩ")

     bac_si = BacSi()
     bac_si.gioi_thieu()
     # Output:
     # Tôi là một người bình thường
     # Tôi cũng là một bác sĩ
     ```

3. **Ghi đè phương thức (method overriding)**: Lớp con có thể định nghĩa lại các phương thức đã có trong lớp cha.  
   - **Ví dụ**:  
     ```python
     class Nguoi:
         def di_chuyen(self):
             print("Người đang di chuyển với tốc độ trung bình")

     class ChienBinh(Nguoi):
         def di_chuyen(self):
             print("Chiến binh đang di chuyển nhanh hơn")

     chien_binh = ChienBinh()
     chien_binh.di_chuyen()  # Output: Chiến binh đang di chuyển nhanh hơn
     ```

4. **Kế thừa đa (multiple inheritance)**: Một lớp có thể kế thừa từ nhiều lớp khác nhau.  
   - **Ví dụ**:  
     ```python
     class BacSi:
         def chua_benh(self):
             print("Bác sĩ đang chữa bệnh")

     class ChienBinh:
         def tan_cong(self):
             print("Chiến binh đang tấn công")

     class PhuThuy(BacSi, ChienBinh):
         def niem_phep(self):
             print("Phù thủy đang niệm phép")

     phu_thuy = PhuThuy()
     phu_thuy.chua_benh()  # Output: Bác sĩ đang chữa bệnh
     phu_thuy.tan_cong()   # Output: Chiến binh đang tấn công
     phu_thuy.niem_phep()  # Output: Phù thủy đang niệm phép
     ```

5. **Thứ tự kế thừa trong trường hợp xung đột (method resolution order - MRO)**: Khi một lớp kế thừa từ nhiều lớp và các phương thức trùng tên, Python sẽ sử dụng phương thức của lớp được liệt kê đầu tiên trong danh sách kế thừa.  
   - **Ví dụ**:  
     ```python
     class BacSi:
         def di_chuyen(self):
             print("Bác sĩ di chuyển cẩn thận")

     class ChienBinh:
         def di_chuyen(self):
             print("Chiến binh di chuyển nhanh")

     class PhuThuy(BacSi, ChienBinh):
         pass

     phu_thuy = PhuThuy()
     phu_thuy.di_chuyen()  # Output: Bác sĩ di chuyển cẩn thận
     ```

6. **Ví dụ trong game (kế thừa trong hệ thống nhân vật):**  
   - **Nguoi**:  
     ```python
     class Nguoi:
         def di_chuyen(self):
             print("Người đang di chuyển")
         
         def nghi_ngoi(self):
             print("Người đang nghỉ ngơi")
     ```
   - **BacSi**:  
     ```python
     class BacSi(Nguoi):
         def chua_benh(self):
             print("Bác sĩ đang chữa bệnh")
     ```
   - **ChienBinh**:  
     ```python
     class ChienBinh(Nguoi):
         def gay_sat_thuong(self):
             print("Chiến binh đang gây sát thương")
         
         def di_chuyen(self):
             print("Chiến binh di chuyển nhanh hơn")
     ```
   - **PhuThuy**:  
     ```python
     class PhuThuy(BacSi, ChienBinh):
         def niem_phep(self):
             print("Phù thủy đang niệm phép để trở nên vô hình")
         
         def chua_benh(self):
             print("Phù thủy chữa bệnh mạnh hơn")
    character1=PhuThuy()
    character1.di_chuyen()
     ```

**Tóm lại:** Kế thừa là công cụ mạnh mẽ giúp tái sử dụng code, xây dựng hệ thống phân cấp lớp một cách dễ dàng, và giúp chương trình dễ mở rộng, bảo trì hơn.