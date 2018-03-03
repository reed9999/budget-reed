from unittest import TestCase
from BudgetApp import BudgetApp
import csv, re, os


class TestBudgetApp(TestCase):
    output_fn = "__temp-output-file.csv"
    runTest = ['test_load_config', 'test_output_data']  #This does not appear to be the right way to do this.

    def setUp(self):
        self.app = BudgetApp()
        os.chdir(os.path.expanduser("~/code/budget-reed"))


    def test_load_config(self):
        config = self.app.load_config()
        self.assertIsNotNone(self.app.config, 'Should have loaded a config [and returned a value].')
        self.assertIsNotNone(config, 'Should have [loaded a config and] returned a value.')
        example_key = u'input-filename'
        self.assertIsNotNone(config[example_key], 'Loaded config should include {}'.format(example_key))

    def test_read_data_from_input_file(self):
        self.app.read_data_from_input_file()
        self.assertIsNotNone(self.app.rows)
        self.assertGreater(len(self.app.rows), 0, 'Should have read in some rows from the input file.')

    def test_output_data(self):
        list_of_dicts = [
            {'Date': '08/13/1978', 'Name': 'HANDY CLEANERS', 'Amount': '(700.54)'},
            {'Date': '08/13/1982', 'Name': 'DANDY CLEANERS', 'Amount': '(815.54)'},
            {'Date': '08/13/2004', 'Name': 'CANDY CLEANERS', 'Amount': '(912.54)'},
            {'Date': '08/13/2015', 'Name': 'VANDY HOME SERVICES', 'Amount': '(1.17)'},
            {'Date': '08/13/2018', 'Name': 'HANDY CLEANERS', 'Amount': '(5.00)'},
                         ]
        # self.app.__instance.rows = list_of_dicts
        self.app.set_rows(list_of_dicts)
        self.app.output_data()
        fn = self.__class__.output_fn

        with open(fn, 'r') as output_file:
            self.assertIsNotNone(output_file, "The output file is not present and that is a problem. File name: {0}".format(fn))
            lines=output_file.readlines()
            self.assertGreater(len(lines), 4, "The output file should have many lines but only has {0}.".format(len(lines)))

    def test_clean_up_data(self):
        list_of_dicts = [{'Date': '07/29/1973', 'Name': 'HANDY CLEANERS', 'Amount': '(700.54)'}]
        # self.app.__instance.rows = list_of_dicts
        self.app.set_rows(list_of_dicts)
        self.app.clean_up_data()
        self.assertIsNotNone(self.app.rows)
        self.assertEqual( -700.54, self.app.rows[0]['Amount'], "Amount should match")

    def test_parse_date(self):
        import datetime
        result = self.app.parse_date("12/06/2017")
        self.assertEqual(datetime.datetime(year=2017, month=12, day=6, hour=0, minute=0), result,
                         "Parsing method parse_date doesn't work")

    def test_parse_gain_loss(self):
        result = self.app.parse_gain_loss("(1234.45)")
        self.assertEqual(-1234.45, result, "Parsing method parse_gain_loss doesn't work. ")
        result = self.app.parse_gain_loss('"999,888.75"')
        self.assertEqual(999888.75, result, "Parsing method parse_gain_loss doesn't work for gains with quotes. ")

    def test_output_positive_entries_make_sense(self):
        self.app.run()
        fn = self.__class__.output_fn
        rows = []
        with open(fn, 'r') as output_file:
            self.assertIsNotNone(output_file,
                                 "The output file is not present and that is a problem. File name: {0}".format(fn))
            rows = list(csv.DictReader(output_file))
        positives = [row for row in rows if float(row['Amount']) > 0.0]

        vendor_who_gave_refund = 'ALASKA'
        patterns = ['PAYMENT RECEIVED', vendor_who_gave_refund]
        match_any_regex = "|".join(patterns)

        problem_positives = [row for row in positives if not re.search(match_any_regex, row['Description'])]
        self.assertLess(len(problem_positives), 1, "My regex is probably broken but... "
                                                        "There shouldn't be any surprising positive entries.")


    def test_alternative_input_files(self):
        self.skipTest("Right now input file name is hardcoded!")

