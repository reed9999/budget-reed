#going by this for a singleton idiom: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

from yaml import load, dump
import csv, re, datetime

class BudgetApp(object):

    class __BudgetApp:
        def __init__(self):
            pass

        def __str__(self):
            return repr(self)

        def load_config(self):
            #Why is it hardcoded? Fake it til we make it!
            self.config = {u"input-file" : "/home/philip/code/budget-reed/__/something.csv"}
            return self.config

        def read_data_from_input_file(self):
            self.rows = []
            with open(self.config[u"input-file"]) as f:
                self.rows = list(csv.DictReader(f))

        def output_data(self):
            with open("__temp-output-file.csv", 'w') as f:
                fieldnames = self.rows[0].keys()
                w = csv.DictWriter(f, fieldnames)
                w.writeheader()
                w.writerows(self.rows)

        def clean_up_data(self):
            # There are probably cute more-Pythonic ways to do this with map.
            # For now this is my attempt at a crude but working implementation.
            for row in self.rows:
                row['Date'] = self.parse_date(row['Date'])
                # unchanged row['Description']
                row['Amount'] = self.parse_gain_loss(row['Amount'])


        #If I wanted to lay the groundwork for something cute and polymorphic, I could have
        # references to each method for different formats, and then standardize the interface
        # so as to just iterate through a dict matching each field with its format.
        def parse_date(self, str):
            #import locale
            #locale.setlocale(locale.LC_ALL, 'en_US')    #unsupported. Weird! de_DE is the same.
            rv = datetime.datetime.strptime(str, "%m/%d/%Y")
            return rv

        def parse_gain_loss(self, str):
            import locale
            locale.setlocale(locale.LC_ALL, '')

            capture_digits_periods_commas = "([0-9\.,]*)"
            optional_quote = '"*'
            loss_pattern = "\(" + optional_quote + capture_digits_periods_commas + optional_quote + "\)"
            gain_pattern = "^" + optional_quote + capture_digits_periods_commas + optional_quote + "$"
            gain_result = re.search(gain_pattern, str)
            loss_result = re.search(loss_pattern, str)
            if loss_result:
                return -locale.atof(loss_result.group(1))
            elif gain_result:
                return locale.atof(gain_result.group(1))
            raise Exception("I couldn't match this with {} or {}".format((loss_pattern, gain_pattern)))

        def run_for_instance(self):
                self.load_config()
                self.read_data_from_input_file()
                self.clean_up_data()
                self.output_data()

        def set_rows(self, rows):
            self.rows = rows

    #I don't understand why we wouldn't want to double-underscore this.
    __instance = None

    def __init__(self):
        cls = self.__class__
        if not cls.__instance:
            cls.__instance = cls.__BudgetApp()
        else:
            pass


    def __getattr__(self, name):
        return getattr(self.__instance, name)


    @classmethod
    def run(cls) -> object:
        app = BudgetApp()
        app.run_for_instance()


