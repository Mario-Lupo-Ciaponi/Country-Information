from countryinfo import CountryInfo


def getting_country_information(country_name):
    """
      This function returns the information of a country.
    """

    return CountryInfo(country_name)


def showing_country_information(country_information, country_name):
    """
      This function prints the information about the given country.
    """
    print(f"\nInformation about {country_name}:\n")

    print(f"Language/s: {", ".join(country_information.languages())}")
    print(f"Capital city: {"".join(country_information.capital())}")
    print(f"Population: {country_information.population()}")
    print(f"Currency/ies: {"".join(country_information.currencies())}")
    print(f"Native's name: {country_information.native_name()}")
    print(f"Resident's name: {country_information.demonym()}")
    print(f"Area: {country_information.area()} km²")
    print(f"Provinces: {", ".join(country_information.provinces())}")
    print(f"Region: {country_information.subregion()}")
    print(f"Borders: {", ".join(country_information.borders())}")
    print(f"Calling code: +{", ".join(country_information.calling_codes())}")
    print(f"Time zone: {", ".join(country_information.timezones())}")
    print(f"Domain: {", ".join(country_information.tld())}")
    print(f"More information: {country_information.wiki()}\n")


def main():
    """
     This is the main function in which you give the name of the country.
    """
    country_name = input("Type the name of the country that you want to see the information: ")
    while True:
        country_information = getting_country_information(country_name)
        showing_country_information(country_information, country_name)

        country_name = input("If you want to see the information of another country type its name."
                                    "If you want to quit type 'Exit'. ")

        if country_name == "Exit":
            break


main()
