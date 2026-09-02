from __future__ import annotations

import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path

from scripts.validate_skills import collect_skill_files, main, validate_skill


def write_skill(root: Path, directory: str, frontmatter: str, body: str = "# Instructions\n") -> Path:
    skill_dir = root / directory
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(f"---\n{frontmatter}---\n\n{body}", encoding="utf-8")
    return skill_file


class ValidateSkillTests(unittest.TestCase):
    def test_accepts_minimal_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = write_skill(
                Path(temp_dir),
                "example-skill",
                "name: example-skill\ndescription: Use when an example task needs focused guidance.\n",
            )

            self.assertEqual(validate_skill(path), [])

    def test_rejects_missing_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "broken-skill" / "SKILL.md"
            path.parent.mkdir()
            path.write_text("# No frontmatter\n", encoding="utf-8")

            errors = validate_skill(path)

            self.assertTrue(any("frontmatter" in error for error in errors))

    def test_rejects_invalid_name_and_directory_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = write_skill(
                Path(temp_dir),
                "expected-name",
                "name: Invalid_Name\ndescription: Use when validating a malformed skill.\n",
            )

            errors = validate_skill(path)

            self.assertTrue(any("name" in error for error in errors))
            self.assertTrue(any("directory" in error for error in errors))

    def test_rejects_missing_or_oversized_description(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            missing = write_skill(root, "missing-description", "name: missing-description\n")
            oversized = write_skill(
                root,
                "oversized-description",
                f"name: oversized-description\ndescription: {'x' * 1025}\n",
            )

            self.assertTrue(any("description" in error for error in validate_skill(missing)))
            self.assertTrue(any("1024" in error for error in validate_skill(oversized)))

    def test_collects_only_skill_files_one_directory_below_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            expected = write_skill(
                root,
                "one-skill",
                "name: one-skill\ndescription: Use when collecting valid skill files.\n",
            )
            nested = root / "too" / "deep"
            nested.mkdir(parents=True)
            (nested / "SKILL.md").write_text("ignored", encoding="utf-8")

            self.assertEqual(collect_skill_files([root]), [expected])

    def test_cli_fails_when_a_requested_path_does_not_exist(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_skill(
                root,
                "one-skill",
                "name: one-skill\ndescription: Use when checking requested validation paths.\n",
            )
            missing = root / "missing"
            stderr = StringIO()

            with redirect_stderr(stderr):
                status = main([str(root), str(missing)])

            self.assertEqual(status, 1)
            self.assertIn("does not exist", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
