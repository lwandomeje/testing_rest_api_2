from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest
#from item_test import ItemModel


class StoreTest(UnitBaseTest):

    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         'the name of the store after creation does not equal the constructor argument.')
