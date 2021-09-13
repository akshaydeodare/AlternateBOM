# AlternateBOM
Software Bill Of Material (bom.xml) generated using CycloneDx is given as input to [Steve Springett's DependencyTrack](https://dependencytrack.org/). 

Creating BOM files from CycloneDx is not always possible because Developers from Organisations dont necessarily use npm for installing third party JS libraries. To create BOM file for npm package using CycloneDx, package.json is required. Here we will not require this file , However dependency-check JSON report is must.

**This Project is completely dependent on Dependency-Check JSON report.**
AlternateBOM will create a BOM file from [dependency-check](https://owasp.org/www-project-dependency-check/) json report of Third Party JS files.

When Creating BOM files using CycloneDx [CycloneDx Project by OWASP](https://cyclonedx.org/tool-center/) , one doesnt have to worry a lot about False Positives, However Dependency-check will pop some false positives so Dependency Track will also have false positives because AlternateBOM will create bom.xml from Dependency-Check JSON report.

# Usage
First Prettyfy the dependency-check-report json file

`python  pretty_report.py path/to/dependency-check-report.json`

Load the pretty json file into alternatebom.py

`python alternatebom.py path/to/pretty/dependency-check-report.json`

A bom.xml file will be generated which can be uploaded to DependencyTrack .

How to import bom into Dependency Track [Video 1](https://www.youtube.com/watch?v=nZakPU0wJMo) [Video 2](https://www.youtube.com/watch?v=FWOCX7wEAzI)



