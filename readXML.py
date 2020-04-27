# Name: readXML
# Author: Reacubeth
# Time: 2020/4/26 22:07
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from xml.dom.minidom import parse


class PaperXML:
    def __init__(self, file_path):
        self.dom = parse(file_path)
        self.data = self.dom.documentElement
        self.paper_title = self.get_paper_title()
        self.paper_year = 0
        self.paper_aff_dict = self.get_affiliation()
        self.author_dict = self.get_author()
        self.ref_dict = self.get_rf()

    def get_paper_title(self):
        return self.data.getElementsByTagName('article-title')[0].childNodes[0].nodeValue

    def get_paper_year(self):
        return self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('year')[0].childNodes[0].nodeValue

    def get_affiliation(self):
        data_range = self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('contrib-group')[0]
        aff_ls = data_range.getElementsByTagName('aff')
        aff_dict = {}
        for item in aff_ls:
            aff_id = item.getElementsByTagName('label')[0].childNodes[0].nodeValue
            aff_name = item.getElementsByTagName('institution')[0].childNodes[0].nodeValue
            aff_dict[aff_id] = {'name': aff_name}
            if item.getElementsByTagName('addr-line'):
                address = item.getElementsByTagName('addr-line')[0].childNodes[0].nodeValue
                aff_dict[aff_id]['address'] = address
            if item.getElementsByTagName('country'):
                country = item.getElementsByTagName('country')[0].childNodes[0].nodeValue
                aff_dict[aff_id]['country'] = country
        return aff_dict

    def get_author(self):
        data_range = self.data.getElementsByTagName('article-meta')[0].getElementsByTagName('contrib-group')[0]
        author_ls = data_range.getElementsByTagName('contrib')
        author_dict = {}
        author_rank = 0
        for item in author_ls:
            author_name = item.getElementsByTagName('string-name')[0].childNodes[0].nodeValue
            email = item.getElementsByTagName('email')[0].childNodes[0].nodeValue
            author_dict[str(author_rank)] = {'authorName': author_name, 'email': email}
            affiliation = []
            xref_ls = item.getElementsByTagName('xref')
            for xref_item in xref_ls:
                xref_val = xref_item.getAttribute('ref-type')
                if xref_val == 'aff':
                    affiliation.append(xref_item.childNodes[0].nodeValue)
            author_dict[str(author_rank)]['affiliation'] = affiliation
            author_rank += 1
        return author_dict

    def get_secs(self):
        secs = self.data.getElementsByTagName('sec')
        for item in secs:
            sec_title = item.getElementsByTagName('title')[0].childNodes[0].nodeValue
            print(sec_title)

    def get_rf(self):
        ref_ls = self.data.getElementsByTagName('ref')
        rf_rank = 0
        ref_dict = {}
        for item in ref_ls:
            article_title = item.getElementsByTagName('mixed-citation')[0]. \
                getElementsByTagName('article-title')[0].childNodes[0].nodeValue
            article_year = item.getElementsByTagName('year')[0].childNodes[0].nodeValue
            ref_dict[str(rf_rank)] = {'paperName': article_title, 'year': article_year}
            rf_rank += 1
        return ref_dict


if __name__ == '__main__':
    paper = PaperXML('8.xml')
    print(paper.get_secs())

