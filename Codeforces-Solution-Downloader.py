##__author = 'akgarhwal'

from bs4 import BeautifulSoup
import urllib
import os
import re

#remove '/' from file name
def convert(filePath):
    name = ""
    for i in filePath[0:-4]:
        if( i != '/'):
            name += i
    return name+filePath[-4:]

# Code-Forces data scrapping
def codeforces_data_scrap(handle):
    try:
        # Basic Url
        rootPath = os.getcwd() + "/Code-Forces-Submission"
        submission_url = 'http://codeforces.com/submissions/'
        codeforces_url = 'http://codeforces.com'

        #create directory
        if not os.path.exists(rootPath) :
            os.mkdir(rootPath)

        r = urllib.urlopen(submission_url + handle).read()
        soup = BeautifulSoup(r, "lxml")
        # Finding total no of submission page
        pageno = soup.find_all("div", class_="pagination")

        numPage = 1
        if len(pageno) != 1:
            pageno = pageno[1].find("ul")
            pageno = pageno.find_all("li")
            numPage = int(pageno[-2].get_text())
        page_url = '/page/'

        for i in range(1, numPage + 1):
            url = submission_url + handle + page_url + str(i)
            print url

            r = urllib.urlopen(url).read()
            soup = BeautifulSoup(r, "lxml")

            datatable = soup.find_all("table", class_="status-frame-datatable")
            # print len(datatable)

            TR = datatable[0].find_all("tr")
            TR = TR[1:]
            # print TR[1]

            #print "Total Submission : " + str(len(TR))
            #codeforces_data = "\"Code-Forces\" : [\n\t"
            for tr in TR:
                submission_link = tr.find("td", class_="id-cell")
                submission_link = submission_link.a["href"]
                #print(submission_link)

                sourceCode = urllib.urlopen(codeforces_url+submission_link).read()
                sourceCode = BeautifulSoup(sourceCode,"lxml")
                sourceCode = sourceCode.find("div", class_="roundbox ").find("pre").text
                # print(sourceCode)

                problem_name_link = tr.find_all("td", class_="status-small")
                problem_name_link = problem_name_link[1]
                problem_link = (problem_name_link.a["href"]).strip()
                problem_name = (problem_name_link.find("a").get_text()).strip()
                # print(problem_link)
                # print(problem_name)

                submission_id_verdict = tr.find("td", class_="status-cell status-small status-verdict-cell")
                submission_id_verdict = submission_id_verdict.find_all("span")
                submission_id = submission_id_verdict[0]["submissionid"]
                submission_verdict = submission_id_verdict[0]["submissionverdict"]
                print(submission_verdict + "  " + problem_name )

                if submission_verdict != "OK":
                    continue

                #dirPath = rootPath+contestId[0]

                filePath = problem_name + "__" + submission_verdict + ".txt"
                filePath = convert(filePath)
                filePath = rootPath + "/" + filePath


                print (filePath)
                # add problem link to source code
                sourceCode = "/* " + codeforces_url + problem_link + " */\n" + sourceCode

                text_file = open(filePath, "w")
                text_file.write(sourceCode)
                text_file.close()

                print("Done")
        print("Successful :)")
    except :
        print("Failed!! Try Again.")

#call function
handle = raw_input('Enter Codeforces handle : ')
codeforces_data_scrap(handle)
