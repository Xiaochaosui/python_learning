import yaml
# 装载yaml文档
with open('fcn8s_camvid.yml') as f:
    cfg= yaml.load(f)

print(cfg["model"])