import sys


class MainInteractiveMenu:
    template_main_menu = """
    Select 1 for Load data
    Select 2 for Find and display asset
    Select 3 for Find and display trade details
    Select 4 for Find and display potential trade paths
    Select 5 for Set asset filter
    Select 6 for Asset overview
    Select 7 for Trade overview
    Select 8 for Save data (serialized)
    Select 9 for Exit
    """

    template_load_data_sub_menu="""
    Select 1 for Asset data
    Select 2 for Trade data
    Select 3 for Serialized data
    """

    template_asset_filter_menu="""
    Select 1 for include asset
    Select 2 for exclude asset
    """

    def __call__(self):
        return self.menu_handle()

    def is_valid(self, value, min_value, max_value):
        # Check for None
        if value is None:
            return False
        # Check for numeric value
        try:
            float(value)
        except Exception as ex:
            print("Error. You have entered non-numeric option. Please enter valid option")
            return False

        # Check for integer value
        if int(float(value))!=float(value):
            print("Error. You have entered option with decimal value. Please enter valid option")
            return False
        
        # Check if value exist in range
        if not (min_value <= int(float(value)) <= max_value):
            print("Error. You have selected option that is not given")
            return False
        
        return True

    def menu_handle(self):
        opt1, opt2 = None, None
        self.show(self.template_main_menu)
        # is_continue=True

        while not self.is_valid(opt1, 1, 9):
            opt1=input("Choose a input: ")
        # Option 1 and Option 6 have sub options
        # needs to be handled differently
        try:
            opt1=int(float(opt1))
        except Exception as ex:
            print("Error. Cannot cast option to integer..")
            sys.exit(1)
        
        # Internal sub menu control
        if opt1==1:
            self.clearLS()
            self.show(self.template_load_data_sub_menu)
            while not self.is_valid(opt2, 1, 3):
                opt2=input("Choose a input: ")
        elif opt1==5:
            self.clearLS()
            self.show(self.template_asset_filter_menu)
            while not self.is_valid(opt2, 1, 2):
                opt2=input("Choose a input: ")
        # Internal submenu ends
        try:
            if opt2:
                opt2=int(float(opt2))
        except Exception as ex:
            print("Warning. Cannot cast option to integer..")

        self.clearLS()

        return (opt1, opt2)

    def clearLS(self):
        import os
        _=os.system('cls' if os.name=='nt' else 'clear')
        # print('\n'*100)

    def show(self, m_template):
        print(m_template)