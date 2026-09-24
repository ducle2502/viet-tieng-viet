---
name: viet-tieng-viet
description: Viết mới hoặc biên tập văn bản công việc bằng tiếng Việt tự nhiên, loại bỏ lối dịch từng chữ từ tiếng Anh, câu hành chính máy móc và dấu hiệu văn phong AI nhưng không làm đổi sự kiện, số liệu, nguồn hoặc mức độ chắc chắn. Luôn dùng skill này khi người dùng yêu cầu viết lại cho tự nhiên, bỏ mùi AI, bỏ dịch thô Anh-Việt, Việt hóa báo cáo, chỉnh văn phong quản trị, hoặc biên tập báo cáo kiểm toán, tờ trình, biên bản, email và kiến nghị bằng tiếng Việt, kể cả khi người dùng không gọi tên skill.
---

# Viết tiếng Việt

## Mục tiêu

Viết như người Việt đang giải quyết một việc cụ thể. Không giữ khung tư duy và trật tự câu tiếng Anh rồi thay bằng từ Việt. Giữ nguyên sự kiện, số liệu, nguồn, tên riêng và mức độ chắc chắn.

## Bắt đầu từ trạng thái hiện tại

Trước khi sửa, xác định văn bản đang ở trường hợp nào:

1. Bản dịch từ tiếng Anh cần viết lại hoàn toàn.
2. Bản tiếng Việt có câu dịch thô hoặc câu máy móc.
3. Bản nháp cần viết mới theo giọng văn của một nhóm người đọc cụ thể.
4. Văn bản nhạy cảm về trách nhiệm, pháp lý, tuân thủ hoặc thiệt hại.

Nếu người dùng đã cung cấp đủ văn bản và mục đích, bắt đầu ngay. Chỉ hỏi thêm khi thiếu thông tin có thể làm đổi ý nghĩa hoặc người chịu trách nhiệm.

## Quy trình

1. Xác định người đọc, mục đích và quyết định mà văn bản cần hỗ trợ.
2. Tách nội dung thành sự việc đã biết, điểm chưa rõ, ảnh hưởng có thể xảy ra và việc phải làm.
3. Viết lại từ ý, không sửa từng từ trên khung câu cũ.
4. Mở mỗi đoạn bằng kết luận chính hoặc sự việc quan trọng nhất.
5. Nêu rõ ai làm, làm gì, khi nào và cần có hồ sơ gì.
6. Soát lại số liệu, ngày, tên, mã hồ sơ, nguồn và mức độ chắc chắn.
7. Đọc `references/checklist.md` trước khi bàn giao. Khi cần dò nhanh các mẫu bề mặt, chạy `python scripts/lint_vi.py <tep>`.
8. Lưu kết quả vào tệp mới nếu người dùng yêu cầu sửa tệp. Không ghi đè bản gốc.

## Cách viết

- Ưu tiên câu chủ động và động từ cụ thể.
- Đặt chủ thể gần đầu câu khi trách nhiệm là thông tin quan trọng.
- Viết quan hệ thực tế: “chưa phê duyệt hạ tầng thì chưa thể khai trương”.
- Mỗi câu tập trung vào một ý chính.
- Mỗi đoạn phải giúp người đọc trả lời ít nhất một câu hỏi: có việc gì, căn cứ nào, ảnh hưởng gì, ai phải xử lý.
- Dùng thuật ngữ tiếng Việt trước. Thêm thuật ngữ tiếng Anh và chữ viết tắt ở lần đầu nếu cần.
- Giữ thuật ngữ nội bộ đã có cách dùng thống nhất. Không tự Việt hóa nếu có thể làm sai nghĩa.
- Thay câu mơ hồ bằng câu có người và việc, chẳng hạn “KTNB chưa nhận được biên bản” thay cho “hồ sơ hiện có chưa cho thấy”.

## Những lỗi cần tránh

Các lỗi dưới đây làm văn bản giống bản dịch hoặc đầu ra máy. Tránh chúng khi không có lý do nghiệp vụ rõ ràng:

- Giữ nguyên trật tự câu tiếng Anh rồi thay bằng từ Việt.
- Giấu chủ thể bằng “cần được”, “được thực hiện”, “đã được ghi nhận” khi có thể nêu đơn vị.
- Lạm dụng danh từ hóa như “việc thực hiện”, “kết quả thực hiện”, “mức độ sẵn sàng”, “tình trạng”.
- Dùng câu nối rỗng như “song song với đó”, “cùng thời điểm”, “đáng chú ý là”.
- Tạo bộ ba hoặc bộ bốn chỉ để câu cân đối.
- Dùng ẩn dụ, khẩu hiệu, câu kết hoa mỹ hoặc lối “không chỉ... mà còn...”.
- Lặp cùng một khuôn cho mọi đoạn.
- Dùng gạch ngang dài.

Đọc `references/translationese-patterns.md` khi văn bản có nhiều dấu hiệu dịch Anh-Việt hoặc khi cần giải thích vì sao một câu chưa tự nhiên.

## Giữ nguyên bằng chứng và mức độ kết luận

- Không thêm số liệu, nguyên nhân, trách nhiệm hoặc hậu quả không có trong nguồn.
- Không biến dấu hiệu thành vi phạm, nghi vấn thành kết luận hoặc khả năng thành sự việc chắc chắn.
- Không bỏ điều kiện, ngoại lệ hoặc giới hạn phạm vi chỉ để câu ngắn hơn.
- Khi hai nguồn khác nhau, giữ cả hai và nêu rõ điểm chưa thống nhất.
- Khi chưa kiểm tra độc lập, dùng cách viết thể hiện đúng giới hạn đó.

## Báo cáo kiểm toán và quản trị

Mỗi vấn đề nên có đủ năm thành phần, nhưng không cần lặp năm tiêu đề máy móc:

1. Kết luận chính.
2. Sự việc và số liệu chứng minh.
3. Phần chưa kiểm tra được hoặc hồ sơ còn thiếu.
4. Ảnh hưởng cụ thể nếu không xử lý.
5. Kiến nghị ghi rõ đơn vị, việc phải làm, thời hạn và hồ sơ phải nộp.

Ưu tiên kết luận và quyết định cần đưa ra. Không bắt đầu bằng một danh sách dài chỉ để chứng minh đã đọc hết tài liệu.

## Điểm người dùng cần duyệt

Đánh dấu rõ để người dùng duyệt trước khi coi là bản cuối nếu việc viết lại làm thay đổi hoặc có thể bị hiểu là thay đổi:

- Chủ thể chịu trách nhiệm.
- Mức độ rủi ro hoặc mức độ chắc chắn.
- Thời hạn hoặc điều kiện đóng kiến nghị.
- Nội dung pháp lý, tuân thủ, thiệt hại hoặc cáo buộc.
- Thuật ngữ nội bộ chưa có cách dùng thống nhất.

Không tự phê duyệt thay người dùng. Có thể đề xuất cách viết, nhưng phải tách đề xuất khỏi quyết định đã được phê duyệt.

## Đầu ra

- Giữ định dạng người dùng yêu cầu.
- Nếu người dùng yêu cầu tệp, tạo tệp mới với tên phân biệt rõ bản đã biên tập.
- Sau bản viết lại, nêu ngắn gọn các thay đổi chính theo nhóm: cấu trúc, độ tự nhiên, mức độ chắc chắn và thuật ngữ.
- Không tuyên bố văn bản “không còn dấu hiệu AI” theo nghĩa tuyệt đối. Chỉ nêu các mẫu đã kiểm tra và giới hạn của phép kiểm tra.
