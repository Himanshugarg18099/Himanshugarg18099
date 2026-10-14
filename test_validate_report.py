import json
import pytest
from validate_report import validate_json_report

def test_validate_json_report_valid_list(tmp_path):
    # Create a temporary valid JSON list file
    test_file = tmp_path / "valid_report.json"
    data = [{"id": 1, "name": "Test1"}, {"id": 2, "name": "Test2"}]
    with open(test_file, 'w') as f:
        json.dump(data, f)

    assert validate_json_report(str(test_file)) is True

def test_validate_json_report_invalid_dict(tmp_path, capsys):
    # Create a temporary JSON dict file (not a list)
    test_file = tmp_path / "invalid_dict_report.json"
    data = {"id": 1, "name": "Test1"}
    with open(test_file, 'w') as f:
        json.dump(data, f)

    assert validate_json_report(str(test_file)) is False
    captured = capsys.readouterr()
    assert "Error: JSON must be a list (array)." in captured.out

def test_validate_json_report_invalid_json(tmp_path, capsys):
    # Create a file with invalid JSON
    test_file = tmp_path / "invalid_json_report.json"
    with open(test_file, 'w') as f:
        f.write("{ invalid json [")

    assert validate_json_report(str(test_file)) is False
    captured = capsys.readouterr()
    assert "Error: Invalid JSON format." in captured.out

def test_validate_json_report_file_not_found(capsys):
    # Test with a file that doesn't exist
    assert validate_json_report("non_existent_file.json") is False
    captured = capsys.readouterr()
    assert "Error: File not found." in captured.out
