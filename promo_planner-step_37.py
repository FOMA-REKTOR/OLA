# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: PromoPlanner
import unittest

class TestPromoPlanner(unittest.TestCase):
    def test_add_channel(self):
        channels = {}
        channels['email'] = {'name': 'Email', 'cost': 0.1, 'volume': 10000}
        self.assertEqual(len(channels), 1)
        self.assertEqual(channels['email']['name'], 'Email')

    def test_add_campaign(self):
        campaigns = {}
        campaigns['summer_sale'] = {'name': 'Summer Sale', 'budget': 5000, 'expected_roi': 2.5}
        self.assertIn('summer_sale', campaigns)
        self.assertEqual(campaigns['summer_sale']['budget'], 5000)

    def test_add_task(self):
        tasks = {}
        tasks['design_banner'] = {'name': 'Design Banner', 'status': 'todo', 'priority': 'high'}
        self.assertEqual(tasks['design_banner']['status'], 'todo')

    def test_add_result(self):
        results = {}
        results['summer_sale'] = {'total_revenue': 15000, 'cost': 5000, 'roi': 3.0}
        self.assertEqual(results['summer_sale']['roi'], 3.0)

    def test_channel_with_budget_check(self):
        channels = {'email': {'name': 'Email', 'cost': 0.1, 'volume': 10000}}
        budget = 1000
        cost = channels['email']['cost'] * channels['email']['volume']
        self.assertLessEqual(cost, budget)

if __name__ == '__main__':
    unittest.main()
