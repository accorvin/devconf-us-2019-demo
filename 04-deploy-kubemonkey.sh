#! /bin/bash

ansible-playbook deploy.yaml -e kubeconfig=$HOME/.kube/config -e namespace=devconf-demo \
    -e monkey=true \
    -e victim=true
