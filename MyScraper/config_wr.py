import oyaml

class TestTing:
    def update_creds_to_config_install_yml_file(self, config_install_file, creds:dict):
        cfg = ''
        with open(config_install_file, 'r+') as f:
            cfg = oyaml.full_load(f)
        with open(config_install_file, 'w') as f1:
            for k, v in creds.items():
                cfg['EII'][k] = v
            oyaml.dump(cfg, f1, indent=4, sort_keys=False)

c = {
    'etcdroot_password': 'eii123',
    'influxdb_username': 'admin',
    'influxdb_password': 'admin123',
    'webvisualizer_username': 'admin',
    'webvisualizer_password': 'admin@123',
    'minio_access_key': 'admin',
    'minio_secret_key': 'password'
}
# c = {'EII':{
#         'etcdroot_password': 'eii123',
#         'influxdb_username': 'admin',
#         'influxdb_password': 'admin123',
#         'webvisualizer_username': 'admin',
#         'webvisualizer_password': 'admin@123',
#         'minio_access_key': 'admin',
#         'minio_secret_key': 'password'
#     }
# }
obj = TestTing()
obj.update_creds_to_config_install_yml_file('config_install.yml',c)