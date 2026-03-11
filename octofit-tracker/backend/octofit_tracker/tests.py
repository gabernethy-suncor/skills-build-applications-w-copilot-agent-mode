from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')
    def test_user_creation(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'Clark Kent')
    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2026-03-11')
        self.assertEqual(str(activity), 'Tony Stark - Running')
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='All')
        self.assertEqual(str(workout), 'Pushups')
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Peter Parker', email='peter@marvel.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Peter Parker - 100')
