# AlternateBOM
Software Bill Of Material (bom.xml) generated using CycloneDx is given as input to DependencyTrack. 

Creating BOM files from CycloneDx is not always possible because Developers from Organisations dont necessarily use npm for installing third party JS libraries. To create BOM file for npm package using CycloneDx, package.json is required. Here we will not require this file , However dependency-check JSON report is must.

This Project is completely dependent on Dependency-Check JSON report.
AlternateBOM will create a BOM file from dependency-check json report of Third Party JS files.

When Creating BOM files using CycloneDx , one doesnt have to worry a lot about False Positives, However Dependency-check will pop some false positives so Dependency Track will also have false positives because AlternateBOM will create bom.xml from Dependency-Check JSON report.


