# wake-on-lan
 Docker container to wake on lan with unicast packet

## Build
```
sh build.sh
```
or
```
VERSION=$( cat version.txt )
docker build -t biolekm/wake_on_lan:$VERSION .
```

## Run
```

docker run \
    -d \
    -p 80:8080 \
    --env PORT=<port> \
    --env LOG_LEVEL=<level> \
    biolekm/wake_on_lan:<version>
```