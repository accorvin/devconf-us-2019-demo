#! /bin/bash

ansible-playbook deploy.yaml -e kubeconfig=$HOME/.kube/config -e namespace=devconf-demo \
    -e monitoring=true \
    -e basic_deployment=true
