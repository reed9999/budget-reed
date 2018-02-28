from unittest import TestCase
from BudgetApp import BudgetApp


class TestBudgetApp(TestCase):
    def setUp(self):
        self._app = BudgetApp()

    def test_load_config(self):
        config = self._app.load_config()
        self.assertIsNotNone(self._app.config, 'Should have loaded a config [and returned a value].')
        self.assertIsNotNone(config, 'Should have [loaded a config and] returned a value.')
        self.assertIsNotNone(config['input-file'], 'Loaded config should include input-file')

    def test_read_data_from_input_file(self):
        self._app.read_data_from_input_file()
        self.assertIsNotNone(self._app.rows)
        self.assertGreater(len(self._app.rows), 0, 'Should have read in some rows from the input file.')

    def test_output_data(self):
        list_of_dicts = [{'hello' : 1, 'goodbye' : 2}]
        # self._app.__instance.rows = list_of_dicts
        self._app.set_rows(list_of_dicts)
        self._app.output_data()
        fn = "__temp-output-file.csv"
        with open(fn, 'r') as f:
            if f is None:
                raise Exception("The input file is not present and that is a problem. File name: {0}".format(fn))

    def test_clean_up_data(self):
        self.skipTest('NYI')

    def test_parse_date(self):
        self.skipTest('NYI')

    def test_parse_gain_loss(self):
        self.skipTest('NYI')
