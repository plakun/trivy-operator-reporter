# trivy-operator-reporter
Trivy-operator reports exporter written in Python

To run the application, you need to have local kubeconfig on your host for an account with the right permissions in the kubernetes cluster.

Run script:
```
git clone https://github.com/plakun/trivy-operator-reporter
cd trivy-operator-reporter
/bin/python3 ./trivy-reporter.py
```

Then open in browser address:
http://127.0.0.1:5000

![изображение](https://github.com/user-attachments/assets/d36c5a6e-74b0-4f14-b23c-f91b94ae2100)
