import os
import shutil
from xml.dom import minidom


def unzip_all():
    cur_dir = os.getcwd()
    cur_dir= cur_dir + '/inter/'
    print('current dir -> {0}'.format(cur_dir))
    f_list = os.listdir(cur_dir)
    print('all file list -> {0}'.format(f_list))
    zf_list = [a for a in f_list if a.endswith('.zip')]
    print('filtered zip files -> {0}'.format(zf_list))
    for f in zf_list:
        print('now unzipping -> {0}'.format(f))
        try:
            shutil.unpack_archive(os.path.join(cur_dir, f), cur_dir)
        except Exception as e:
            print('Failed with this error :{0}'.format(e))
        print('done')

def xml_json():
    cur_dir = os.getcwd()
    cur_dir= cur_dir + '/inter/'
    print('current dir -> {0}'.format(cur_dir))
    f_list = os.listdir(cur_dir)
    print('all file list -> {0}'.format(f_list))
    ff_list = [a for a in f_list if not a.__contains__('.')]
    ff_list = ff_list[:-1]
    print('filtered folders -> {0}'.format(ff_list))
    for ff in ff_list:
        xml_file = os.path.join(cur_dir, ff, "edgesoftware_configuration.xml")
        
        dom:minidom.Document = minidom.parse(xml_file)
        #print(dom.childNodes.)
        dl = dom.childNodes

        j_son = {}
        mj_son = {}

        for i in dl:
            #print(i)
            for e in i.childNodes:
                #print(e.nodeName)
                for s1 in dom.getElementsByTagName(e.nodeName):
                    mj_son[s1.getAttribute('version')] = ''
                    mj_son[s.getAttribute('tag')] = ''

                mj_son.pop('')
                print(mj_son)

                for k, v in mj_son.items():
                    for s in dom.getElementsByTagName(e.nodeName):
                        if s.getAttribute('version') == k:
                            mj_son[s.getAttribute('version')] = ''
                            elements = dom.getElementsByTagName('main')
                            for ele in elements:
                                j_son['main'] = [ele.attributes['label'].value]
                        #print(s.getAttribute('version'))
                    if s.getAttribute('tag') != '':
                        pass
                        #print(s.getAttribute('tag'))
                


                #print(ele.attributes['label'].value)
            elements1 = dom.getElementsByTagName('default')
            for ele1 in elements1:
                j_son['default'] = ele1.attributes['label'].value
                #print(ele1.attributes['label'].value)
            elements2 = dom.getElementsByTagName('project')
            for ele2 in elements2:
                j_son['project'] = ele2.attributes['label'].value
                #print(ele2.attributes['label'].value)
            elements3 = dom.getElementsByTagName('image')
            for ele3 in elements3:
                j_son['image'] = ele3.attributes['label'].value
                #print(ele3.attributes['label'].value)
            
            print(mj_son)


        
xml_json()
#unzip_all()
