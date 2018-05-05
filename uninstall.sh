#pip3 uninstall main
pip3 uninstall xxurl
git rm -r dist
git rm -r build
#git rm -r main.egg-info
git rm -r xxurl.egg-info
rm -r dist
rm -r build
#rm -r main.egg-info
rm -r xxurl.egg-info
git add .
git commit -m "remove old build"
