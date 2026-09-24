#!/usr/bin/env python3
import re, sys
from pathlib import Path
PATTERNS = {
 "gạch ngang dài": r"[—–]",
 "câu nối dễ rỗng": r"\b(song song với đó|cùng thời điểm|đáng chú ý là)\b",
 "danh từ hóa": r"\b(việc thực hiện|kết quả thực hiện|mức độ sẵn sàng|tình trạng mua sắm)\b",
 "bị động mơ hồ": r"\b(cần được thực hiện|được ghi nhận là|được xác định là)\b",
 "khung đối xứng": r"\b(không chỉ.+mà còn|không những.+mà còn)\b",
}
def main(path):
 text=Path(path).read_text(encoding="utf-8"); found=0
 for label,pat in PATTERNS.items():
  for m in re.finditer(pat,text,flags=re.I|re.S):
   line=text.count("\n",0,m.start())+1
   print(f"{path}:{line}: {label}: {re.sub(r'\s+',' ',m.group(0))[:120]}"); found+=1
 print("Không phát hiện mẫu bề mặt trong danh sách kiểm tra." if not found else f"Tổng số dấu hiệu cần đọc lại: {found}")
 return 1 if found else 0
if __name__=="__main__":
 if len(sys.argv)!=2: print("Cách dùng: python lint_vi.py <tep.md>"); raise SystemExit(2)
 raise SystemExit(main(sys.argv[1]))
