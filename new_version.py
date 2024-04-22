import webbrowser
from tkinter import *
from tkinter import messagebox
from countryinfo import CountryInfo
import country_converter

import pycountry


class Country_Info:
    def __init__(self, master):
        self.master = master
        self.master.title("Country Information Finder")
        self.master.geometry("300x100")

        self.label = Label(self.master, text="Country name:")  # A label that show the text "Country name:"
        self.label.pack()

        self.entry_country_name = Entry(self.master, width=15)  # An entry box that allows the user to enter a country name
        self.entry_country_name.pack()

        self.search_button = Button(self.master, text="Search", command=self.show_country_info)  # A button that allows the user to see the country's information on click
        self.search_button.pack()


    def is_it_valid(self):
        """
        This function checks if the user entered a valid country name.
        """
        valid = False

        try:
            country = pycountry.countries.lookup(self.entry_country_name.get())
            valid = True
        except LookupError:
            messagebox.showerror("Country not found", "The country you entered is not found!")

        return valid

    def get_country_info(self):
        if self.is_it_valid():
            return CountryInfo(self.entry_country_name.get())
        else:
            return None

    def show_country_info(self):

        country_info = self.get_country_info()

        if country_info is not None:
            country_name = self.entry_country_name.get().capitalize()
            title_string = country_name

            if country_name[-1] == "s":
                title_string += "' information"  # In grammar when the final letter is a "s" then we say for example "Netherlands' capital".
            else:
                title_string += "'s information"

            country_root = Toplevel()
            country_root.title(title_string)
            country_root.geometry("550x440")

            aland = ""

            if len(country_name) == 2:
                aland = pycountry.countries.get(alpha_2=country_name)
            elif len(country_name) == 3:
                aland = pycountry.countries.get(alpha_3=country_name)
            elif len(country_name) > 3:
                aland = pycountry.countries.get(name=country_name)

            flag = aland.flag

            language_spoken = country_info.languages()  # or languages
            list_of_languages = []
            for language in language_spoken:
                iso_2 = pycountry.languages.get(alpha_2=language)
                standard_name = iso_2.name

                list_of_languages.append(standard_name)

            capital_city = country_info.capital()  # The capital of the country
            population = country_info.population()  # Approximately the population of the country
            currency = country_info.currencies()  # The currency or currencies of the country
            native_name = country_info.native_name()  # e.g Bulgaria -> България
            denonym = country_info.demonym()  # e.g Italy -> Italian
            area = country_info.area()  # The area of the country in qubic kilometers
            region = country_info.subregion()

            iso_2_borders = country_info.borders()
            standard_name_borders = ", ".join(country_converter.convert(names=iso_2_borders, to="name_short"))  #e.g fr -> France

            if not standard_name_borders:
                standard_name_borders = "No borders or have maritime borders."

            calling_codes = ", ".join([f"+{calling_code}" for calling_code in country_info.calling_codes()])
            time_zones = ", ".join(country_info.timezones())
            domain = ", ".join(country_info.tld())
            provinces = country_info.provinces() # Provinces of a country
            more_information_link = country_info.wiki()  # A link that leads to wikipedia

            # Widgets:

            name_label = Label(country_root, text=f"{country_name}:", font=("Arial", 20))
            name_label.pack()

            flag_label = Label(country_root, text=flag, font=("Arial", 70))
            flag_label.pack()

            language_label = Label(country_root, text=f"Language/s: {", ".join(list_of_languages)}")
            language_label.pack()

            capital_city_label = Label(country_root, text=f"Capital city: {capital_city}")
            capital_city_label.pack()

            population_label = Label(country_root, text=f"Population(approximately): {population:,}")
            population_label.pack()

            currency_label = Label(country_root, text=f"Currency: {", ".join(currency)}")
            currency_label.pack()

            native_name_label = Label(country_root, text=f"Native's name: {native_name}")
            native_name_label.pack()

            denonym_label = Label(country_root, text=f"Resident's name: {denonym}")
            denonym_label.pack()

            area_label = Label(country_root, text=f"Area: {area:,} km²")
            area_label.pack()

            region_label = Label(country_root, text=f"Region: {region}")
            region_label.pack()

            borders_label = Label(country_root, text=f"Borders: {standard_name_borders}")
            borders_label.pack()

            calling_code_label = Label(country_root, text=f"Calling code: {calling_codes}")
            calling_code_label.pack()

            time_zone_label = Label(country_root, text=f"Time zone/s: {time_zones}")
            time_zone_label.pack()

            domain_label = Label(country_root, text=f"Domain: {domain}")
            domain_label.pack()

            provinces_button = Button(country_root, text="Click here to check the provinces",
                                      command=lambda: self.create_provinces_window(provinces, country_name))
            provinces_button.pack()

            more_information_link_label = Label(country_root, padx=15,
                                                text=f"More information: {more_information_link}", cursor="hand1")

            more_information_link_label.pack()
            more_information_link_label.bind("<Button-1>", lambda e: webbrowser.open_new(more_information_link))

    def create_provinces_window(self, provinces, country_name):
        provinces_window = Toplevel()
        provinces_window.title("Provinces")

        provinces_label = Label(provinces_window, text=f"Provinces of {country_name}:", padx=30)
        provinces_label.pack()

        for province in provinces:
            province_label = Label(provinces_window, text=province)
            province_label.pack()


def main():
    root = Tk()
    country_info = Country_Info(root)
    root.mainloop()


if __name__ == "__main__":
    main()
