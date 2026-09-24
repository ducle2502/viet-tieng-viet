# viet-tieng-viet

Skill biên tập tiếng Việt tự nhiên cho văn bản công việc.

## Cấu trúc

- `SKILL.md`: hướng dẫn và điều kiện kích hoạt.
- `references/checklist.md`: kiểm tra trước khi bàn giao.
- `references/translationese-patterns.md`: mẫu dịch thô thường gặp.
- `references/examples.md`: ví dụ trước và sau.
- `scripts/lint_vi.py`: dò một số dấu hiệu bề mặt.
- `evals/evals.json`: ba tình huống đánh giá chất lượng.
- `evals/trigger-evals.json`: bộ câu hỏi kiểm tra kích hoạt.
- `evals/test_lint_vi.py`: kiểm thử cho script.

## Kiểm tra nhanh

```bash
python scripts/lint_vi.py <tep.md>
python -m pytest evals/test_lint_vi.py
```

Script chỉ dò các mẫu bề mặt. Kết quả không chứng minh văn bản do AI tạo và không thay thế việc đọc, sửa của con người.
