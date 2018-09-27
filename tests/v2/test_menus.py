"""
This module facilitates testing
"""
import unittest
import os
import sys
import json

from tests.v2.base_setup import BaseTests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class MenuTests(BaseTests):
    """
    This class contains tests for menu
    """

    def test_get_all_menu(self):
        """
        This method tests if an admin successfully gets all menu
        """
        response = self.client().get('api/v2/menus')
        self.assertEqual(response.status_code, 200)

    def test_get_a_particular_menu(self):
        """
        This method tests if an admin successfully gets a particular menu
        """
        response = self.client().get('api/v2/menus/1')
        self.assertEqual(response.status_code, 200)

    def test_admin_create_menu(self):
        """
        This method tests a successful creation of menu
        """
        data = {
            "menu_item": "Ugali & Mboga",
            "price": 50
        }
        response = self.client().post('/api/v2/menus', data=data)
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu has been successfully posted')

    # def test_admin_successfully_updates_menu(self):
    #     data = {
    #         "menu_item": "Ugali & Chiken",
    #         "price": 50
    #     }
    #     response = self.client().post('/api/v2/menus', data=data)
    #     self.assertEqual(response.status_code, 201)
    #     newdata = {
    #         "menu_item": "Ugali & Chiken",
    #         "price": 30
    #     }
    #     res = self.client().put('/api/v2/menus/1', data=newdata)
    #     self.assertEqual(res.status_code, 200)
    #     result = json.loads(res.data.decode('utf-8'))
    #     self.assertEqual(result["price"], 30)

    def test_admin_delete_a_particular_menu(self):
        """
        This method tests successful deletion of a particular menu
        """
        data = {
            "menu_item": "Ugali & Beef",
            "price": 50
        }
        res = self.client().post('/api/v2/menus', data=data)
        self.assertEqual(res.status_code, 201)
        response = self.client().delete('/api/v2/menus/1')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result.get('message'), 'menu item has been deleted')

if __name__ == '__main__':
    unittest.main()