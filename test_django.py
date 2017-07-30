from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		print('setup...')
		self.browser = webdriver.Firefox()
	def tearDown(self):
		print('teardown..')
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		print('test can start a list ...')
		self.browser.get('http://localhost:8000')
		#title是否包含To-do
		self.assertIn('To-do', self.browser.title)
		self.fail('Finish the test')


print(__name__)

if __name__ == '__main__':
	unittest.main(warnings='ignore')

# 2017.7.30


