import unittest

def mark_attendance(student_id, status):
    if student_id and status in ["Present", "Absent"]:
        return True
    return False

class AttendanceTest(unittest.TestCase):
    def test_mark_present(self):
        self.assertTrue(mark_attendance("STU101", "Present"))

    def test_mark_absent(self):
        self.assertTrue(mark_attendance("STU102", "Absent"))

    def test_empty_student_id(self):
        self.assertFalse(mark_attendance("", "Present"))

    def test_invalid_status(self):
        self.assertFalse(mark_attendance("STU103", "Late"))

if __name__ == "__main__":
    unittest.main()