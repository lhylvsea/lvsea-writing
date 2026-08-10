import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_writing import scan_text  # noqa: E402


class CheckWritingTests(unittest.TestCase):
    def test_high_confidence_residue_fails(self):
        result = scan_text("好的，下面是修改后的版本。很好的问题。\n\n这不是A而是B，这不是C而是D。")
        self.assertGreaterEqual(len(result.failures), 3)

    def test_context_terms_are_warnings_not_hard_failures(self):
        result = scan_text("这个流程形成了闭环，底层逻辑是先记录、再验证。")
        self.assertFalse(result.failures)
        self.assertGreaterEqual(len(result.warnings), 1)

    def test_code_and_urls_are_masked(self):
        result = scan_text("代码 `print('好的，下面是')` 和网址 https://example.com/oaicite。这里写事实。")
        self.assertFalse(result.failures)

    def test_clean_professional_text_can_pass(self):
        text = (
            "本周二号线停机 18 分钟，原因是冷却水泵保护动作。维修人员先确认电气回路，"
            "随后更换接触器并复测。生产损失已经按当班记录登记，产品质量未发现异常。"
            "下一步由设备组在周五前完成同型号泵的点检，生产组负责复核备用件数量。"
        )
        result = scan_text(text, scenario="professional")
        self.assertFalse(result.failures)


if __name__ == "__main__":
    unittest.main()
