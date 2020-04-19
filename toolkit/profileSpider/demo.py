from toolkit.profileSpider.profile_class import Profile
import re

url = 'http://www.cs.tsinghua.edu.cn/publish/cs/4616/2013/20130424102559852515182/20130424102559852515182_.html'
# url = 'http://cs.ahu.edu.cn/2018/0329/c11201a163134/page.htm'

url = 'http://cs.ahu.edu.cn/2018/0322/c11201a163135/page.htm'

'''
html, _ = he.extract(url, text_only=False, remove_img=False, save=True)
doc, p_val = he.extract(url, save=True)
'''

profile = Profile(url)
profile.identify()
print(profile.get_email())
print(profile.get_homepage())
print(profile.get_gender())
edu_dict = profile.get_edu_dict()
honor_dict = profile.get_honor_dict()
pub_dict = profile.get_pub_dict()
year_dict = profile.get_year_dict()

for key in edu_dict:
    print('----')
    print('education', edu_dict[key]['prob'], edu_dict[key]['year'], key)

for key in honor_dict:
    print('----')
    print('honor', honor_dict[key]['prob'], honor_dict[key]['year'], key)


for key in pub_dict:
    print('----')
    print('publication', pub_dict[key]['prob'], pub_dict[key]['year'], key)

print('###########')

for i in year_dict:
    print(i, year_dict[i])

