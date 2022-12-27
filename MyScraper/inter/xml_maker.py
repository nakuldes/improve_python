import os
import shutil
from xml.dom import minidom
import json


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
    #print('current dir -> {0}'.format(cur_dir))
    f_list = os.listdir(cur_dir)
    #print('all file list -> {0}'.format(f_list))
    ff_list = [a for a in f_list if not a.__contains__('.')]
    ff_list = ff_list[:-2]
    #print('filtered folders -> {0}'.format(ff_list))
    print('\n\n')
    for ff in ff_list:
        print(ff)
        xml_file = os.path.join(cur_dir, ff, "edgesoftware_configuration.xml")
        
        dom:minidom.Document = minidom.parse(xml_file)
        #print(dom.childNodes.)
        dl = dom.childNodes

        mj_son = {}
        att = []
        for i in dl:
            #print(i)
            for e in i.childNodes:
                if str(e.nodeName) == '#text':
                    continue
                print(e.nodeName)
                for s1 in dom.getElementsByTagName(e.nodeName):
                    mj_son[s1.getAttribute('version')] = ''
                    mj_son[s1.getAttribute('tag')] = ''
                    #att.append(e.nodeName)

                if mj_son.get("") is not None:
                    mj_son.pop('')
        att_l = ["project", "image"]
        obj = get_data(dom, mj_son, att_l)
        json_file = os.path.join(cur_dir, 'zipa', "{0}.json".format(ff))

        with open(json_file, "w") as outfile:
            pr = json.dump(obj, outfile, indent=2)
            print(pr)


def get_data(dom, mj_son, att):
    # dl = dom.childNodes
    # i = dl[0]
    # j = i.childNodes

    
    z = dom.getElementsByTagName('main')
    z1 = dom.getElementsByTagName('default')
    for k, v in mj_son.items():
        j_son = {}
        y = z[0]
        y1 = z1[0]
        j_son['main'] = y.attributes['label'].value
        j_son['default'] = [y1.attributes['label'].value]
        for e in att:
        #     if str(e.nodeName) == '#text':
        #         continue

            d=[]
            for s in dom.getElementsByTagName(e):
                if (s.getAttribute('version') == k) or (s.getAttribute('tag') == k):
                    d.append(s.attributes['label'].value)
                    print("v:{0}, node: {1} \nlbl:{2}".format(k, e, d))

            j_son[e+'s'] = d

        mj_son[k] = j_son
    #print(mj_son)

    # json_object = json.dumps(mj_son, indent = 4)
    # print(json_object)
    # return json_object
    return mj_son


            


        
xml_json()
#unzip_all()
