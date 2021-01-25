import unittest
from unittest.mock import patch

import sqlalchemy

from start import get_app


class RoutesTest(unittest.TestCase):
	def setUp(self) -> None:
		self.app = get_app()

	def test_default_rendering(self):
		with self.app.test_client() as c:
			with c.get("/") as rv:
				self.assertTrue(rv)

	def test_render_login_on_noauth(self):
		with self.app.test_client() as c:
			with c.get("/login") as login_page:
				l_page_content = login_page.data
			with c.get('/request') as request_page:
				r_page_contet = request_page.data

		self.assertEqual(l_page_content, r_page_contet)

	@patch('infrastructure.database_manager.dblink.DBConn')
	def test_api_request_without_auth(self, mock_sql):
		with self.app.test_client() as c:
			with c.get("/api/request") as api_req:
				self.assertTrue(True)
				self.assertTrue(mock_sql.called)


if __name__ == '__main__':
	unittest.main()
