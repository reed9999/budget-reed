#going by this for a singleton idiom: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

from yaml import load, dump


class BudgetApp(object):

    class __BudgetApp:
        def __init__(self):
            pass

        def __str__(self):
            return repr(self)
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
    def load_config(self):
        return {u"input-file" : "__/something.csv"}


    @classmethod
    def run(cls) -> object:
        app = BudgetApp()
        config = app.load_config()
        print (str.format("Hello {}" , config[u"input-file"]))


