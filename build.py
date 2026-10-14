"""Merge data/categories/*.json into data/questions.json and embed it in index.html."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SECTIONS = [
    ("development", "LLM Application Development"),
    ("prompt", "Prompt Engineering"),
    ("rag", "RAG"),
    ("finetuning", "LLM Fine-tuning"),
    ("production", "Production Practices and AI Security"),
    ("agents", "AI Agent and Applications"),
]

questions = []
for sid, _ in SECTIONS:
    qs = json.loads((ROOT / f"data/categories/{sid}.json").read_text())["questions"]
    for q in qs:
        ids = {o["id"] for o in q["options"]}
        assert q["section"] == sid and set(q["correct"]) <= ids, q["id"]
        assert (len(q["correct"]) == 1) == (q["type"] == "single"), q["id"]
    questions += qs
assert len({q["id"] for q in questions}) == len(questions), "duplicate ids"

bank = {
    "version": 2,
    "title": "LLM Engineer Professional — Practice set 02",
    "sourceRoot": "aliyun_acp_learning/LLM_ACP_EN/p2_Build LLM Q&A System",
    "sections": [{"id": i, "title": t} for i, t in SECTIONS],
    "questions": questions,
}
text = json.dumps(bank, ensure_ascii=False, indent=2)
(ROOT / "data/questions.json").write_text(text + "\n")

html = (ROOT / "index.html").read_text()
html = re.sub(
    r'(<script id="question-bank" type="application/json">).*?(</script>)',
    lambda m: m[1] + text.replace("</", "<\\/") + m[2],
    html, count=1, flags=re.S,
)
html = re.sub(r"\d+ PRACTICE\s+QUESTIONS", f"{len(questions)} PRACTICE QUESTIONS", html)
(ROOT / "index.html").write_text(html)
print(f"{len(questions)} questions embedded")
