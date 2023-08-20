# -*- coding: UTF-8 -*-
'''
@Project ：pycahrm 
@File    ：connectDatabricks.py
@IDE     ：PyCharm 
@Author  ：ouyangqun
@Date    ：2023/8/18 9:22 
'''

from databricks import sql


tokenAndUrlList = [
    ('CORP_dev', 'adb-6141521119240036.0.databricks.azure.cn', 'svc_adb_sa',
     'dapic788329800b6110ad36192d326defa87', 'sql/protocolv1/o/6141521119240036/0901-161346-myrk1xmk'),
    ('FI_dev', 'adb-8985601279512450.2.databricks.azure.cn', 'svc_adb_sa',
     'dapi95f31c46e7eb0f954e50d4b8f2cb7b75', 'sql/protocolv1/o/8985601279512450/0901-161351-n67c5tje'),
    ('MS_dev', 'adb-5595716883787667.3.databricks.azure.cn', 'svc_adb_sa',
     'dapib99e83a5de1af3decb40d80192fc1e3d', 'sql/protocolv1/o/5595716883787667/0901-161347-ep1uv1n0'),
    ('ODS_dev', 'adb-3971825890743195.3.databricks.azure.cn', 'svc_adb_sa',
     'dapi50abe7d1760e034c1eb41f2d084d0c66', 'sql/protocolv1/o/3971825890743195/0901-161344-pewrhx3b'),
    ('SC_dev', 'adb-7248864666503408.0.databricks.azure.cn', 'svc_adb_sa',
     'dapi14c19ccdb8cae08efb64f7027608f75a', 'sql/protocolv1/o/7248864666503408/0901-161349-31tgaj2n'),
    ('SRV_dev', 'adb-5923819007296603.3.databricks.azure.cn', 'svc_adb_sa',
     'dapi8b0f7002fb55a0f2530ee92b63f947d0', 'sql/protocolv1/o/5923819007296603/0901-161352-wc8ovpc0'),
    ('WWSRV_dev', 'adb-387305740285050.2.databricks.azure.cn', 'svc_adb_sa',
     'dapib14cbd1b0ed9d8dc791c7db8e4de8a65', 'sql/protocolv1/o/387305740285050/0901-161354-carbrxot')
]
def get_group_permission(workspace, hostname, http_path, token):
    result = []
    databricks_conn = sql.connect(server_hostname=hostname,
    http_path=http_path,
    access_token=token)
    databricks_cursor = databricks_conn.cursor()
    databricks_cursor.execute('show schemas')
    schemas = [row.databaseName for row in databricks_cursor.fetchall()]
    print(schemas)
    for schema in schemas:
        grants = databricks_cursor.execute(f'show grants on schema `{schema}`').fetchall()
        principal_permissions = {}
        for grant in grants:
            principal = grant.Principal
            permission = grant.ActionType
            principal_permissions.setdefault(principal, []).append(permission)
            for principal in principal_permissions.keys():
                result.append([workspace, principal, schema, str(principal_permissions.get(principal))])

    databricks_cursor.close()
    databricks_conn.close()
    return result

if __name__ == '__main__':

    # workspace_name = tokenAndUrlList[2][0]
    # url = tokenAndUrlList[2][1]
    # username = tokenAndUrlList[2][2]
    # http_path = tokenAndUrlList[2][4]
    # token = tokenAndUrlList[2][3]
    # print(get_group_permission(workspace_name,url,http_path,token))

    hostname = 'adb-5852107264335034.2.databricks.azure.cn'
    http_path = 'sql/protocolv1/o/5852107264335034/0727-070823-zxm07c10'
    token = 'dapi3ed0109626e3501bd866f2eae18e3c0f'

    databricks_conn = sql.connect(server_hostname=hostname,
                                  http_path=http_path,
                                  access_token=token)
    databricks_cursor = databricks_conn.cursor()
    # grants = databricks_cursor.execute(f'show grants on schema `cam_corp`').fetchall()
    databricks_cursor = databricks_cursor.execute('GRANT ALL PRIVILEGES  ON  SCHEMA dwd_srv  TO  `ouyangqun1@lenovo.com`')

    # databricks_cursor = databricks_cursor.execute('show schemas')
    # schemas = [row.databaseName for row in databricks_cursor.fetchall()]
    # print(schemas)
    # print(type(grants[0]))
