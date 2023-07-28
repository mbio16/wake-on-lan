VERSION=$( cat version.txt )
docker build -t biolekm/wake_on_lan:$VERSION .