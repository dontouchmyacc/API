from flask import Flask, request, send_file
import json as j
import xml.etree.cElementTree as e

app=Flask(__name__)

@app.route('/api/jsontoxml',methods=['POST'])
def jsontoxml(): #127.0.0.1:5000/api/jsontoxml !METHOD POST
    d=request.get_json()
    r=e.Element('Resume')

    e.SubElement(r,'fullname').text=d['fullname']

    ch=e.SubElement(r,'characteristics')
    e.SubElement(ch,'sex').text=d['characteristics']['sex']
    e.SubElement(ch,'age').text=str(d['characteristics']['age'])

    for i in d['skills']:
        e.SubElement(r,'skills').text=i


    exp=e.SubElement(r,'experience')
    for z in d['experience']:
        e.SubElement(exp,'position').text=z['position']
        e.SubElement(exp,'workplace').text=z['workplace']
        try:
            e.SubElement(exp,'salary').text=z['salary']
            e.SubElement(exp,'id_card').text=z['id_card']
            e.SubElement(exp,'Country').text=z['Country']
        except KeyError:
            continue

    a=e.ElementTree(r)
    a.write('json_to_xml.xml')
    return send_file('json_to_xml.xml')


if __name__=='__main__':
    app.run(debug=True,port=5000)