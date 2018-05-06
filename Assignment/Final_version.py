import csv
import re
from urllib2 import Request, urlopen

import xlsxwriter

from UKMetConfig import UKMetConfig


class WeatherDataParser(object):

    def __init__(self):
        pass

    def run(self):
        print("Running Parser")
        output_data = self.download_and_parse_for_urls()
        if not output_data:
            print("No data to create CSV/EXCEL")
            return
        self.csv_write(output_data)
        self.xlsx_write(output_data)

    def download_and_parse_for_urls(self):
        combined_data = []
        main_url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/'
        # print UKMetConfig.to_download_urls()
        for url_list_elm in UKMetConfig.to_download_urls():
            url = main_url + url_list_elm
            # print url
            print("Working on %s" % url)
            file = self.download_data_from_url(url)
            parse_data = self.parse_data_from_file(file)
            region, weather_param = self.determine_weather_param(url)
            data = self.write_in_given_format(parse_data, region, weather_param)
            if not data:
                continue
            combined_data.append(data)

        return combined_data

    def download_and_parse_for_url(self, url):
        print("Downloading and parsing data for %s" % url)
        try:
            file = self.download_data_from_url(url)
            parse_data = self.parse_data_from_file(file)
            print("Successfully done")
            return parse_data
        except Exception as ex:
            print("Error %s" % ex)

    def download_data_from_url(self, url):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        file = urlopen(req)

        print('Successfully downloaded data from url: {}'.format(url))
        return file

    def parse_data_from_file(self, file):
        data = []
        for lines in file.readlines()[7:117:1]:
            lines = lines.replace('---', 'N/A')
            lines = re.sub(r'\s{7}', '    N/A', lines)
            line_element = [x.strip() for x in lines.split()]

            if len(line_element) != 18:
                line_element.extend(['N/A'] * 4)
            data.append(line_element)

        print('Parsed file for url')
        return data

    def determine_weather_param(self, url):
        url_list = url.split('/')
        region = url_list[-1].strip('.txt')
        weather_param = url_list[-3]
        weather_param = UKMetConfig.param_name_map()[weather_param]

        print('The weather parameters of {} region is {}'.format(region, weather_param))
        return region, weather_param

    def write_in_given_format(self, data, region, weather_param):
        # region, weather_param = self.determine_weather_param(url)
        parse_data = []
        # user descriptive variable names
        var = 0
        var1 = -1
        for list_line in data:
            for count_line_ele, line_ele in enumerate(list_line):
                if count_line_ele == 0:
                    var1 += 1
                    continue
                if var >= 17:
                    line_parse_data = [region, weather_param, data[var1][0], data[0][count_line_ele], line_ele]
                    parse_data.append(line_parse_data)
                    # print line_parse_data
                var += 1
        print('The parsed data for the region {} and for {} is:\n {}'.format(region, weather_param, parse_data))
        return parse_data

    def csv_write(self, output_data):
        with open('Parse_Data_class1111.csv', 'wb') as csvfile:
            for i in range(0, len(output_data)):
                for ele1, ele2, ele3, ele4, ele5 in (output_data[i]):
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([ele1, ele2, ele3, ele4, ele5])

    def xlsx_write(self, output_data):

        workbook = xlsxwriter.Workbook('Parse_Data_Class1111.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0
        for combined_data_index in range(0, len(output_data)):
            for ele1, ele2, ele3, ele4, ele5 in (output_data[combined_data_index]):
                if ele5 != 'N/A':
                    ele5 = float(ele5)
                ele3 = float(ele3)
                worksheet.write(row, col, ele1)
                worksheet.write(row, col + 1, ele2)
                worksheet.write(row, col + 2, ele3)
                worksheet.write(row, col + 3, ele4)
                worksheet.write(row, col + 4, ele5)
                row += 1

        workbook.close()


if __name__ == '__main__':
    WeatherDataParser().run()
