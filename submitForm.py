import re
import mechanize
import html5lib
import urllib2
import sys
reload(sys)  
sys.setdefaultencoding('utf8')



print("start")
br = mechanize.Browser()
response1 = br.open("https://vipmember.tmtd.cpc.com.tw/mbwebs/service_search.aspx")
# follow second link with element text matching regular expression
# response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
# print(br.title())
# print(response1.geturl())
# print(response1.info())  # headers
print(response1.read())  # body

print("submit")

br.select_form(action="./service_search.aspx")
print(br.form)

print("click")
response2 = br.click(id="btnQuery")

print(response2.get_data())
header = response1.info()
request = urllib2.Request("https://vipmember.tmtd.cpc.com.tw/mbwebs/service_search.aspx", response2.get_data(), header)

print("open new")

browser = mechanize.Browser()
print("open new")
rrr = browser.open(request)
print("open new")
print(rrr.read())
print("open new")
# print forms
# br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm.
# br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# Submit current form.  Browser calls .close() on the current response on
# navigation, so this closes response1
# response2 = br.submit()

# print currently selected form (don't call .submit() on this, use br.submit())


# response3 = br.back()  # back to cheese shop (same data as response1)
# the history mechanism returns cached response objects
# we can still use the response, even though it was .close()d
# response3.get_data()  # like .seek(0) followed by .read()
# response4 = br.reload()  # fetches from server

# for form in br.forms():
    # print(form)
# .links() optionally accepts the keyword args of .follow_/.find_link()
# for link in br.links(url_regex="python.org"):
    # print(link)
    # br.follow_link(link)  # takes EITHER Link instance OR keyword args
    # br.back()