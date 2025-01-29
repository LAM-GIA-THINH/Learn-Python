### **1. Câu điều kiện `if`:**
- **Cú pháp:** `if <điều kiện>: <mã thực thi>`
- **Ví dụ:**
  ```python
  is_raining = True
  if is_raining:
      print("Mang ô")  # In ra "Mang ô" vì điều kiện is_raining là True
  ```

---

### **2. Câu lệnh `else`:**
- **Cú pháp:** `else: <mã thực thi>`
- **Ví dụ:**
  ```python
  is_raining = False
  if is_raining:
      print("Mang ô")
  else:
      print("Ô tùy chọn")  # In ra "Ô tùy chọn" vì điều kiện is_raining là False
  ```

---

### **3. Toán tử logic:**
- **Toán tử `or`:**
  - **Ví dụ:**
    ```python
    is_raining = True
    is_cold = False
    if is_raining or is_cold:
        print("Mang ô hoặc áo khoác")  # In ra vì is_raining là True
    ```

- **Toán tử `and`:**
  - **Ví dụ:**
    ```python
    is_raining = True
    is_cold = True
    if is_raining and is_cold:
        print("Mang ô và áo khoác")  # In ra vì cả hai điều kiện đều True
    ```

- **Toán tử `not`:**
  - **Ví dụ:**
    ```python
    is_cold = False
    if not is_cold:
        print("Không cần mang áo khoác")  # In ra vì is_cold là False, not đảo ngược thành True
    ```

---

### **4. Câu lệnh `elif`:**
- **Cú pháp:** `elif <điều kiện>: <mã thực thi>`
- **Ví dụ:**
  ```python
  is_raining = False
  is_cold = True
  if is_raining and not is_cold:
      print("Mang ô")
  elif not is_raining and is_cold:
      print("Mang áo khoác")  # In ra "Mang áo khoác" vì điều kiện này đúng
  else:
      print("Không cần mang gì")
  ```

---

### **5. Ví dụ thực tế về câu điều kiện:**
- **Website đăng nhập:**
  ```python
  is_logged_in = False
  if is_logged_in:
      print("Chào mừng bạn quay lại!")
  else:
      print("Vui lòng đăng nhập để tiếp tục")  # In ra vì is_logged_in là False
  ```

- **Máy thanh toán thẻ tín dụng:**
  ```python
  amount = 60
  if amount <= 50:
      print("Giao dịch được chấp nhận")
  else:
      print("Vui lòng nhập mã PIN")  # In ra vì amount > 50
  ```

---

### **6. Ví dụ với số:**
- **Ví dụ:**
  ```python
  balance = 100
  withdrawal_amount = 75
  if withdrawal_amount <= balance:
      print("Giao dịch thành công")  # In ra vì withdrawal_amount <= balance
  else:
      print("Số dư không đủ")
  ```

---

### **Tổng kết:**
Các ví dụ trên minh họa cách sử dụng câu điều kiện `if`, `else`, `elif` và các toán tử logic (`or`, `and`, `not`) trong các tình huống cụ thể. Những khái niệm này giúp chương trình đưa ra quyết định dựa trên các điều kiện khác nhau, từ đơn giản đến phức tạp.