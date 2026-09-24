from pathlib import Path
import subprocess, tempfile
SCRIPT=Path(__file__).resolve().parents[1]/"scripts"/"lint_vi.py"

def run(text):
    with tempfile.NamedTemporaryFile("w",suffix=".md",encoding="utf-8",delete=False) as f:
        f.write(text); p=f.name
    return subprocess.run(["python",str(SCRIPT),p],capture_output=True,text=True)

def test_clean_text_passes():
    r=run("Ban Dự án phải nộp biên bản trước ngày 30/09/2026.")
    assert r.returncode==0

def test_translationese_is_flagged():
    r=run("Song song với đó, việc thực hiện rà soát cần được thực hiện.")
    assert r.returncode==1
    assert "dấu hiệu" in r.stdout.lower()
