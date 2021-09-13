import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
package=re.compile(r'"id": *"pkg:javascript\/.+"',re.IGNORECASE)
package2=re.compile(r'"id": *"pkg:javascript\\\/.+"',re.IGNORECASE)
print("Usage: python jira_scrapper.py /path/to/prettyfied_dependency_check_report_json_file")
input_file = open(sys.argv[1],"r")
bom = ET.Element('bom')
bom.set('xmlns','http://cyclonedx.org/schema/bom/1.3')
components = ET.SubElement(bom, 'components')
for line in input_file:
    if package.search(line):
        purl=package.search(line).group()
        purl=re.sub(r'"id": *"',"",purl)
        purl=re.sub(r'"',"",purl)
        purl=re.sub(r'javascript',"npm",purl)
        purl=re.sub(r'%.*',"",purl)
        print(purl)
        version=re.sub(r'pkg:npm\/.*@',"",purl)
        version=re.sub(r'\.min',"",version)
        version=re.sub(r'%.*',"",version)
        library=re.sub(r'pkg:npm\/',"",purl)
        library=re.sub(r'@.*',"",library)
        print(version)
        print(library)
        component = ET.SubElement(components, 'component')
        ET.SubElement(component,'name').text = library
        
        ET.SubElement(component,'version').text = version
        
        ET.SubElement(component,'purl').text=purl
    elif package2.search(line):
        purl=package2.search(line).group()
        purl=re.sub(r'"id": *"',"",purl)
        purl=re.sub(r'"',"",purl)
        purl=re.sub(r'javascript\\\/',"npm/",purl)
        purl=re.sub(r'%.*',"",purl)
        print(purl)
        version=re.sub(r'pkg:npm\/.*@',"",purl)
        version=re.sub(r'\.min',"",version)
        version=re.sub(r'%.*',"",version)
        library=re.sub(r'pkg:npm\/',"",purl)
        library=re.sub(r'@.*',"",library)
        print(version)
        print(library)
        component = ET.SubElement(components, 'component')
        ET.SubElement(component,'name').text = library
        
        ET.SubElement(component,'version').text = version
        
        ET.SubElement(component,'purl').text=purl
        
        
        

mydata=ET.tostring(bom,'utf-8')
mydata=minidom.parseString(mydata)
mydata=mydata.toprettyxml(indent="  ")
myfile=open("bom.xml","a+")
myfile.write(mydata)