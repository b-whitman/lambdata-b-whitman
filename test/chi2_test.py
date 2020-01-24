import unittest

from app.team import Team

class TestTeams(unittest.TestCase):

    def test_full_name(self):
        team = Team("New York", "Giants", [])
        self.assertEqual(team.full_name, "New York Giants")


if __name__ == '__main__':
    unittest.main()