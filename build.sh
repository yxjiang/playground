#!/bin/bash

# build web_service
bazel build //web_service/...

rm -rf ./bazel-bin-cp

# copy bazel-bin to current directory as docker cannot access symlink
python3 utils/utils.py --destination_path bazel-bin-cp --source_path bazel-bin

docker build . -t playground/web_service -f web_service.Dockerfile

# cleanup
