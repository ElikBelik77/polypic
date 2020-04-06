class AppSettings:
    """
    Class for holding the settings of the application.
    """
    def __init__(self):
        self.settings = {}

    def set(self, settings):
        for key, value in settings.items():
            self.settings[key] = value
        return self

    def get(self, key):
        return self.settings[key]

    def __getitem__(self, item):
        return self.settings[item]


def get_settings():
    return __app_settings

# Initialize the app settings as a singleton.
__app_settings = None
if __app_settings is None:
    __app_settings = AppSettings()
